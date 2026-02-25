(function() {
    try {
        if (typeof window === 'undefined' || typeof navigator === 'undefined') { return; }

        var LOG_ENABLED = false;
        try {
            var qs = (window.location && window.location.search) ? window.location.search : '';
            LOG_ENABLED = (qs.indexOf('langredirdebug=1') !== -1);
        } catch (e) { /* ignore */ }
        function log() {
            if (!LOG_ENABLED || typeof console === 'undefined' || typeof console.log !== 'function') { return; }
            var args = Array.prototype.slice.call(arguments);
            args.unshift('[lang-redirect]');
            try { console.log.apply(console, args); } catch (e) { /* ignore */ }
        }

        var path = window.location.pathname || '/';
        if (path === '') { path = '/'; }
        path = path.replace(/\s+$/, '');
        log('path', path);

        // Gate by config param (from Hugo .Site.Params.langRedirectEnabled)
        var REDIRECT_ENABLED = {{ with .Site.Params.langRedirectEnabled }}{{ . }}{{ else }}true{{ end }};
        if (!REDIRECT_ENABLED) { log('skip: disabled by config'); return; }

        // Coverage data and threshold from Hugo data/params
        var COVERAGE = {{- with .Site.Data.tx_coverage -}}{{- . | jsonify -}}{{- else -}}{}{{- end -}};
        var THRESHOLD = {{ with .Site.Params.langRedirectThreshold }}{{ . }}{{ else }}80{{ end }};
        log('threshold', THRESHOLD);

        // Redirect from any non-prefixed path (not only root)

        // Supported language slugs from site languages (reflect URL prefixes)
        var LANG_SLUGS = {{- $slugs := slice -}}{{- range .Site.Languages -}}{{- $slugs = $slugs | append .Lang -}}{{- end -}}{{- $slugs | jsonify -}};
        log('LANG_SLUGS', LANG_SLUGS);
        if (!Array.isArray(LANG_SLUGS) || LANG_SLUGS.length === 0) { return; }

        // If already under a supported language prefix, do nothing
        var alreadyPrefixed = LANG_SLUGS.some(function(slug) {
            if (!slug) { return false; }
            var s = String(slug).replace(/^\/+|\/+$/g, '');
            if (!s) { return false; }
            if (path === '/' + s || path.indexOf('/' + s + '/') === 0) { return true; }
            return false;
        });
        log('alreadyPrefixed', alreadyPrefixed);
        if (alreadyPrefixed) { return; }

        var userLangs = Array.isArray(navigator.languages) && navigator.languages.length ? navigator.languages.slice() : [];
        if (navigator.language) { userLangs.push(navigator.language); }
        log('navigator.languages', navigator.languages, 'navigator.language', navigator.language);
        log('userLangs', userLangs);
        if (userLangs.length === 0) { return; }

        function normalize(s) { return String(s || '').toLowerCase(); }
        function matchesSlug(slug, candidate) {
            var s = String(slug || '');
            var c = String(candidate || '');
            if (!s || !c) { return false; }
            if (s.toLowerCase() === c.toLowerCase()) { return true; }
            if (s.replace(/[_-]/g, '').toLowerCase() === c.replace(/[_-]/g, '').toLowerCase()) { return true; }
            return false;
        }

        function pickSlug() {
            // Special handling for Chinese and Portuguese regional variants
            for (var i = 0; i < userLangs.length; i++) {
                var ul = normalize(userLangs[i]);
                log('check regional/base', ul);
                if (ul.indexOf('zh') === 0) {
                    var hasHans = /hans|\bzh-cn\b|\bzh_sg\b|\bzh-sg\b/.test(ul);
                    var hasHant = /hant|\bzh-tw\b|\bzh_hk\b|\bzh-hk\b|\bzh-mo\b/.test(ul);
                    if (hasHans && LANG_SLUGS.indexOf('zh-hans') !== -1) { log('pick zh-hans for', ul); return 'zh-hans'; }
                    if (hasHant && LANG_SLUGS.indexOf('zh-hant') !== -1) { log('pick zh-hant for', ul); return 'zh-hant'; }
                }
                if (ul.indexOf('pt') === 0) {
                    if (/pt-br/.test(ul) && LANG_SLUGS.indexOf('pt_br') !== -1) { log('pick pt_br for', ul); return 'pt_br'; }
                    if (/pt-pt/.test(ul) && LANG_SLUGS.indexOf('pt_pt') !== -1) { log('pick pt_pt for', ul); return 'pt_pt'; }
                }
            }

            // Exact match attempts
            for (var j = 0; j < userLangs.length; j++) {
                for (var k = 0; k < LANG_SLUGS.length; k++) {
                    if (matchesSlug(LANG_SLUGS[k], userLangs[j])) { log('exact match', LANG_SLUGS[k], 'for', userLangs[j]); return LANG_SLUGS[k]; }
                }
            }

            // Base language match (e.g. en-US -> en)
            for (var m = 0; m < userLangs.length; m++) {
                var base = userLangs[m].split(/[-_]/)[0];
                for (var n = 0; n < LANG_SLUGS.length; n++) {
                    var slug = String(LANG_SLUGS[n]);
                    if (matchesSlug(slug, base) || slug.toLowerCase().indexOf(base.toLowerCase() + '_') === 0 || slug.toLowerCase().indexOf(base.toLowerCase() + '-') === 0) {
                        log('base match', slug, 'for base', base);
                        return slug;
                    }
                }
            }

            // Fallback to English if available
            if (LANG_SLUGS.indexOf('en') !== -1) { log('fallback to en'); return 'en'; }
            log('fallback to first', LANG_SLUGS[0]);
            return LANG_SLUGS[0];
        }

        var targetSlug = pickSlug();
        log('targetSlug', targetSlug);
        if (!targetSlug) { log('no targetSlug'); return; }

        var normalizedSlug = String(targetSlug).replace(/^\/+|\/+$/g, '');
        // Do not redirect to English; keep English content at root
        if (normalizedSlug.toLowerCase() === 'en') { log('skip: target is en'); return; }

        // Check coverage threshold for chosen language
        function normalizeKey(k) { return String(k || '').toLowerCase().replace(/[_-]/g, ''); }
        function getCoverageForSlug(slug) {
            var key = normalizeKey(slug);
            // Exact normalized match
            for (var lang in COVERAGE) {
                if (!Object.prototype.hasOwnProperty.call(COVERAGE, lang)) { continue; }
                if (normalizeKey(lang) === key) { return Number(COVERAGE[lang]); }
            }
            // Grouped variants
            var altMap = {
                'ptbr': ['pt_BR','pt-br','pt_br'],
                'ptpt': ['pt_PT','pt-pt','pt_pt'],
                'zhhans': ['zh_CN','zh_SG','zh-hans','zh_hans'],
                'zhhant': ['zh_TW','zh_HK','zh_MO','zh-hant','zh_hant']
            };
            var alt = altMap[key] || [];
            if (alt.length) {
                var wanted = {};
                for (var i = 0; i < alt.length; i++) { wanted[normalizeKey(alt[i])] = true; }
                var best = NaN;
                for (var lang2 in COVERAGE) {
                    if (!Object.prototype.hasOwnProperty.call(COVERAGE, lang2)) { continue; }
                    if (wanted[normalizeKey(lang2)]) {
                        var v = Number(COVERAGE[lang2]);
                        if (!isNaN(v)) { best = Math.max(isNaN(best) ? v : best, v); }
                    }
                }
                return best;
            }
            return NaN;
        }
        var coverage = getCoverageForSlug(normalizedSlug);
        log('coverage', normalizedSlug, coverage);
        if (isNaN(coverage) || coverage < Number(THRESHOLD)) { log('skip: below threshold', coverage, '<', THRESHOLD); return; }
        var prefix = '/' + normalizedSlug + '/';
        var newPath = path === '/' ? prefix : prefix + path.replace(/^\/+/, '');
        var newUrl = window.location.origin + newPath + (window.location.search || '') + (window.location.hash || '');
        if (newUrl !== window.location.href) { log('redirect', { from: window.location.href, to: newUrl }); window.location.replace(newUrl); }
    } catch (e) {
        // fail silently
    }
})();



