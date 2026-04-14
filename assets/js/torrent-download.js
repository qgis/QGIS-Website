(function () {
  'use strict';

  // Cached after first click — subsequent buttons don't re-import.
  var _WebTorrent = null;

  async function loadWebTorrent() {
    if (_WebTorrent) return _WebTorrent;
    // dynamic import() works in a classic script (Chrome 63+, Firefox 67+, Safari 11.1+)
    // and correctly handles the ES module export at the end of webtorrent.min.js.
    await import('/js/webtorrent.min.js');
    // The UMD bundle sets window.WebTorrent as a side effect; mod.default is
    // unreliable because the appended "export default WebTorrent" references a
    // name that isn't in module scope when the file runs as an ES module.
    _WebTorrent = window.WebTorrent;
    if (!_WebTorrent) throw new Error('WebTorrent did not initialise');
    return _WebTorrent;
  }

  function formatSpeed(bytesPerSec) {
    if (bytesPerSec > 1024 * 1024) return (bytesPerSec / 1024 / 1024).toFixed(1) + ' MB/s';
    if (bytesPerSec > 1024) return (bytesPerSec / 1024).toFixed(0) + ' KB/s';
    return bytesPerSec + ' B/s';
  }

  function torrentUrlFromHttp(httpUrl) {
    return httpUrl.replace('https://download.qgis.org', 'https://dl1.qgis.org') + '.torrent';
  }

  async function startTorrentDownload(btn) {
    var httpUrl = btn.dataset.http;
    var platform = btn.dataset.platform; // 'windows' or 'macos'
    var filename = btn.dataset.filename;
    var wrap = btn.closest('.qgis-torrent-wrap');
    var statusEl = wrap.querySelector('.qgis-torrent-status');
    var torrentUrl = torrentUrlFromHttp(httpUrl);

    // Load WebTorrent on first click, then check WebRTC availability.
    var WebTorrent;
    try {
      WebTorrent = await loadWebTorrent();
    } catch (e) {
      window.location = httpUrl;
      return;
    }
    if (!WebTorrent.WEBRTC_SUPPORT) {
      window.location = httpUrl;
      return;
    }

    // showSaveFilePicker prompts for a single file destination — no "system files"
    // restriction that showDirectoryPicker can trigger on Chrome.
    var hasFSAPI = typeof window.showSaveFilePicker === 'function';

    // macOS installers are ~1.5 GB — without the File System Access API we cannot
    // stream to disk, and a 1.5 GB Blob in memory will crash the tab.
    // Fall back to the plain HTTP download (e.g. Firefox on macOS).
    if (platform === 'macos' && !hasFSAPI) {
      window.location = httpUrl;
      return;
    }

    var fileHandle = null;
    if (hasFSAPI) {
      try {
        statusEl.textContent = 'Choose where to save the file…';
        var accept = platform === 'windows'
          ? { 'application/x-msdownload': ['.msi'] }
          : { 'application/x-apple-diskimage': ['.dmg'] };
        fileHandle = await window.showSaveFilePicker({
          suggestedName: filename,
          startIn: 'downloads',
          types: [{ description: 'QGIS Installer', accept: accept }]
        });
        statusEl.textContent = '';
      } catch (e) {
        // User dismissed the picker
        statusEl.textContent = '';
        return;
      }
    }

    btn.disabled = true;
    btn.classList.add('is-loading');
    statusEl.innerHTML = '<progress class="progress is-small is-primary mb-1" value="0" max="100"></progress>Connecting to peers…';

    // Always use the default store (IndexedDB); pieces arrive out of order so we
    // cannot write them sequentially to the FileSystemWritableFileStream during
    // download. We stream to disk in one pass after the torrent is complete.
    var client = new WebTorrent();

    // Stall detection: if no download progress for 30 s (e.g. web seeds blocked by
    // CORS and no P2P peers available), destroy the client and fall back to HTTP.
    var STALL_MS = 30 * 1000;
    var lastProgressAt = Date.now();
    var stallTimer = null;

    function clearStall() {
      if (stallTimer) { clearInterval(stallTimer); stallTimer = null; }
    }

    function fallbackHttp() {
      clearStall();
      statusEl.textContent = '';
      btn.disabled = false;
      btn.classList.remove('is-loading');
      try { client.destroy(); } catch (_) {}
      window.location = httpUrl;
    }

    client.on('error', function (err) {
      console.error('[QGIS torrent] client error', err);
      fallbackHttp();
    });

    client.add(torrentUrl, {}, function (torrent) {
      // Start stall timer once torrent metadata is ready.
      lastProgressAt = Date.now();
      stallTimer = setInterval(function () {
        if (torrent.progress < 1 && Date.now() - lastProgressAt > STALL_MS) {
          console.warn('[QGIS torrent] stalled — falling back to HTTP');
          fallbackHttp();
        }
      }, 5000);

      torrent.on('download', function () {
        lastProgressAt = Date.now();
        var pct = Math.round(torrent.progress * 100);
        var speed = formatSpeed(torrent.downloadSpeed);
        var peers = torrent.numPeers;
        statusEl.innerHTML =
          '<progress class="progress is-small is-primary mb-1" value="' + pct + '" max="100"></progress>' +
          pct + '% &mdash; ' + speed + ' &mdash; ' + peers + ' peer' + (peers !== 1 ? 's' : '');
      });

      torrent.on('done', async function () {
        clearStall();
        btn.classList.remove('is-loading');
        statusEl.innerHTML = '<progress class="progress is-small is-primary mb-1" value="100" max="100"></progress>Saving file…';

        var file = torrent.files[0];

        if (fileHandle) {
          // Stream from IndexedDB directly to the chosen file — no full-file memory spike.
          try {
            var writable = await fileHandle.createWritable();
            await file.stream().pipeTo(writable);
          } catch (e) {
            console.error('[QGIS torrent] stream-to-disk error', e);
            try { client.destroy(); } catch (_) {}
            window.location = httpUrl;
            return;
          }
        } else {
          // Firefox / no File System Access API: materialise Blob.
          // Only reached for Windows (~500 MB) — macOS already falls back to HTTP above.
          try {
            var blob = await file.blob();
            var url = URL.createObjectURL(blob);
            var a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            setTimeout(function () { URL.revokeObjectURL(url); }, 60000);
          } catch (e) {
            console.error('[QGIS torrent] blob download error', e);
            try { client.destroy(); } catch (_) {}
            window.location = httpUrl;
            return;
          }
        }

        statusEl.innerHTML =
          '<span class="has-text-success">' +
          '<i class="fas fa-check-circle mr-1"></i>' +
          'Download complete! Thank you for helping seed QGIS to other users.' +
          '</span>';

        // Keep seeding for 30 minutes to contribute to the swarm, then clean up.
        setTimeout(function () {
          try { client.destroy(); } catch (_) {}
          statusEl.textContent = '';
          btn.disabled = false;
        }, 30 * 60 * 1000);
      });

      torrent.on('error', function (err) {
        console.error('[QGIS torrent] torrent error', err);
        fallbackHttp();
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.qgis-torrent-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        startTorrentDownload(btn);
      });
    });
  });
})();
