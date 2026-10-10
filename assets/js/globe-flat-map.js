// Globe + Flat Map base class - MapLibre GL (Globe) and OpenLayers (Flat Map)
//
// The flat map uses the Equal Earth projection (EPSG:8857 style, sphere
// R = 6371008.7714 m), so countries keep their true relative size.
//
// Shared by the contributors map and the user groups map. It owns everything
// that is not specific to what is drawn: the two map views and the toggle
// between them, globe rotation, hiding markers on the far side of the globe,
// popup open/close plumbing and the `view` URL parameter.
//
// The flat map is the default view. The globe is only built the first time
// the reader switches to it, or when the URL asks for it (?view=globe).
//
// Subclasses set their own state, then call `this.init()`, and implement:
//   onGlobeLoad()                 add sources, layers and markers to this.globeMap
//   onFlatLoad()                  add layers and overlays to this.flatMap
//   restorePopup()                reopen the popup named in the URL, if any
//   clearActivePopup()            forget which popup is open
//   readExtraUrlState(params)     read subclass URL parameters
//   writeExtraUrlState(params)    write subclass URL parameters
//   isLayerVisible(layer)         whether markers of a given layer are shown

// ─── Equal Earth projection ───────────────────────────────────────────────────
// Šavrič, Patterson & Jenny (2018), "The Equal Earth map projection".
// Registered once with OpenLayers, with transforms to and from EPSG:4326 and
// EPSG:3857 so OSM tiles and lon/lat data are reprojected on the fly.

const EQUAL_EARTH_CODE = 'EqualEarth';
const EQUAL_EARTH_EXTENT = [-17243959.06, -8392927.6, 17243959.06, 8392927.6];

function equalEarthProjection() {
  const existing = ol.proj.get(EQUAL_EARTH_CODE);
  if (existing) return existing;

  const A1 = 1.340264, A2 = -0.081106, A3 = 0.000893, A4 = 0.003796;
  const M = Math.sqrt(3) / 2;
  const R = 6371008.7714;
  const DEG = Math.PI / 180;

  const forward = ([lon, lat]) => {
    const theta = Math.asin(M * Math.sin(lat * DEG));
    const t2 = theta * theta, t6 = t2 * t2 * t2;
    const x = R * lon * DEG * Math.cos(theta) / (M * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)));
    const y = R * theta * (A1 + A2 * t2 + t6 * (A3 + A4 * t2));
    return [x, y];
  };

  const inverse = ([x, y]) => {
    const target = y / R;
    let theta = target;
    for (let i = 0; i < 12; i++) {
      const t2 = theta * theta, t6 = t2 * t2 * t2;
      const delta = (theta * (A1 + A2 * t2 + t6 * (A3 + A4 * t2)) - target) /
                    (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2));
      theta -= delta;
      if (Math.abs(delta) < 1e-12) break;
    }
    const t2 = theta * theta, t6 = t2 * t2 * t2;
    const lon = M * x * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)) / (R * Math.cos(theta)) / DEG;
    const lat = Math.asin(Math.max(-1, Math.min(1, Math.sin(theta) / M))) / DEG;
    return [lon, lat];
  };

  const projection = new ol.proj.Projection({
    code: EQUAL_EARTH_CODE,
    units: 'm',
    extent: EQUAL_EARTH_EXTENT,
    worldExtent: [-180, -90, 180, 90],
    global: false
  });
  ol.proj.addProjection(projection);
  ol.proj.addCoordinateTransforms('EPSG:4326', projection, forward, inverse);
  ol.proj.addCoordinateTransforms(
    'EPSG:3857', projection,
    (c) => forward(ol.proj.toLonLat(c)),
    (c) => ol.proj.fromLonLat(inverse(c))
  );
  return projection;
}

class GlobeFlatMap {
  constructor(options = {}) {
    this.globeCenter = options.globeCenter || [150, 10];
    this.globeZoom = options.globeZoom || 2.2;
    this.flatCenter = options.flatCenter || [0, 20];
    this.flatZoom = options.flatZoom || 2;
    this.popupIds = options.popupIds || [];

    this.currentView = 'flat';
    this.globeMap = null;
    this.flatMap = null;
    this.isRotating = false;
    this.rotationAnimation = null;
    // { marker, coords, element, layer } and { overlay, element, layer }
    this.globeMarkers = [];
    this.flatMarkers = [];
  }

  init() {
    this.readUrlState();
    this.setupEventListeners();
    this._showView(this.currentView);
  }

  // ─── Hooks (overridden by subclasses) ───────────────────────────────────────

  onGlobeLoad() {}
  onFlatLoad() {}
  restorePopup() {}
  clearActivePopup() {}
  readExtraUrlState(params) {}
  writeExtraUrlState(params) {}
  isLayerVisible(layer) { return true; }

  // ─── Events and view switching ──────────────────────────────────────────────

  setupEventListeners() {
    document.getElementById('globe-view-btn')?.addEventListener('click', () => {
      this.switchView('globe');
    });

    document.getElementById('flat-view-btn')?.addEventListener('click', () => {
      this.switchView('flat');
    });

    this.popupIds.forEach(id => {
      document.getElementById(id)?.querySelector('.tooltip-close')?.addEventListener('click', () => {
        this.closePopup();
      });
    });

    document.getElementById('popup-overlay')?.addEventListener('click', () => {
      this.closePopup();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.closePopup();
    });
  }

  switchView(view) {
    this.currentView = view;
    this.updateUrlState();
    this._showView(view);
  }

  // Show one view, building its map the first time it is needed.
  _showView(view) {
    const globeView = document.getElementById('globe-view');
    const flatView = document.getElementById('flat-map-view');
    const globeBtn = document.getElementById('globe-view-btn');
    const flatBtn = document.getElementById('flat-view-btn');

    if (view === 'globe') {
      globeView.style.display = 'block';
      flatView.style.display = 'none';
      this._setToggleState(globeBtn, true);
      this._setToggleState(flatBtn, false);

      if (!this.globeMap) {
        this.initGlobeView();
      } else {
        this.globeMap.resize();
        this.updateMarkerVisibility();
      }
    } else {
      globeView.style.display = 'none';
      flatView.style.display = 'block';
      this._setToggleState(globeBtn, false);
      this._setToggleState(flatBtn, true);

      if (!this.flatMap) {
        this.initFlatMap();
      } else {
        this.flatMap.updateSize();
        this.updateAllMarkersVisibility();
      }
    }
  }

  _setToggleState(button, active) {
    if (!button) return;
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', String(active));
  }

  // ─── Globe ──────────────────────────────────────────────────────────────────

  initGlobeView() {
    // Use MapLibre GL v5.16.0 with globe projection
    this.globeMap = new maplibregl.Map({
      container: 'globe-view',
      zoom: this.globeZoom,
      center: this.globeCenter,
      style: {
        version: 8,
        projection: {
          type: 'globe'
        },
        sources: {
          'osm': {
            type: 'raster',
            tiles: ['https://tile.openstreetmap.org/{z}/{x}/{y}.png'],
            tileSize: 256,
            attribution: '© OpenStreetMap contributors',
            maxzoom: 19
          }
        },
        layers: [{
          id: 'osm',
          type: 'raster',
          source: 'osm',
        }],
        sky: {
          'atmosphere-blend': [
              'interpolate',
              ['linear'],
              ['zoom'],
              0, 1,
              5, 1,
              7, 0
          ]
        },
      },
      maxZoom: 18,
      minZoom: 0
    });

    this.globeMap.on('load', () => {
      this.onGlobeLoad();

      this.globeMap.on('move', () => this.updateMarkerVisibility());
      this.globeMap.on('moveend', () => this.updateMarkerVisibility());
      this.globeMap.on('click', (e) => {
        const features = this.globeMap.queryRenderedFeatures(e.point);
        if (features.length === 0) this.closePopup();
      });
      this.updateMarkerVisibility();

      // The reader may have switched back to the flat map while the globe loaded
      if (this.currentView === 'globe') {
        this.restorePopup();
        setTimeout(() => this.startRotation(), 500);
      }
    });

    // Stop rotation on any user interaction
    this.globeMap.on('mousedown', () => this.stopRotation());
    this.globeMap.on('touchstart', () => this.stopRotation());
    this.globeMap.on('wheel', () => this.stopRotation());
    this.globeMap.on('dblclick', () => this.stopRotation());
  }

  // offset: [x, y] in pixels, to keep markers that share a point apart
  addGlobeMarker(element, coords, layer, offset = [0, 0]) {
    const marker = new maplibregl.Marker({ element, anchor: 'center', offset })
      .setLngLat(coords)
      .addTo(this.globeMap);
    this.globeMarkers.push({ marker, coords, element, layer });
    return marker;
  }

  // ─── Flat map ───────────────────────────────────────────────────────────────

  initFlatMap() {
    this.flatProjection = equalEarthProjection();

    const view = new ol.View({
      projection: this.flatProjection,
      center: ol.proj.fromLonLat(this.flatCenter, this.flatProjection),
      extent: EQUAL_EARTH_EXTENT,
      constrainOnlyCenter: true,
      showFullExtent: true
    });

    const outline = this._equalEarthOutline();

    // OSM tiles reprojected from Web Mercator to Equal Earth. Tiles stop at
    // ±85° and reprojected edges come out jagged, so mask the layer to the
    // Equal Earth outline: the ocean coloured outline below shows instead.
    const tiles = new ol.layer.Tile({ source: new ol.source.OSM() });
    const mask = new ol.style.Style({ fill: new ol.style.Fill({ color: 'black' }) });
    tiles.on('postrender', (event) => {
      const context = event.context;
      context.globalCompositeOperation = 'destination-in';
      ol.render.getVectorContext(event).drawFeature(outline, mask);
      context.globalCompositeOperation = 'source-over';
    });

    this.flatMap = new ol.Map({
      target: 'flat-map-view',
      layers: [
        // The world outline in OSM's ocean colour, so the map reads as a whole world
        new ol.layer.Vector({
          source: new ol.source.Vector({ features: [outline] }),
          style: new ol.style.Style({
            fill: new ol.style.Fill({ color: '#aad3df' }),
            stroke: new ol.style.Stroke({ color: '#8fb8c4', width: 1 })
          })
        }),
        tiles
      ],
      view: view
    });
    // Fit the whole world, then never zoom out further than that
    view.fit(EQUAL_EARTH_EXTENT, { padding: [8, 8, 8, 8] });
    view.setMinZoom(view.getZoom());

    this.flatMap.on('click', (evt) => {
      let clickedOnOverlay = false;
      this.flatMap.getOverlays().forEach(overlay => {
        const element = overlay.getElement();
        if (element && element.contains(evt.originalEvent.target)) {
          clickedOnOverlay = true;
        }
      });
      if (!clickedOnOverlay && !this.onFlatMapClick(evt)) this.closePopup();
    });

    this.onFlatLoad();
    // Apply current filter state to freshly-added markers
    this.updateAllMarkersVisibility();
    this.restorePopup();
  }

  // Return true when the click was handled (keeps the popup open).
  onFlatMapClick(evt) { return false; }

  // Outline of the Equal Earth world: the meridians ±180° joined at the poles.
  _equalEarthOutline() {
    const ring = [];
    for (let lat = -90; lat <= 90; lat += 1) ring.push([180, lat]);
    for (let lat = 90; lat >= -90; lat -= 1) ring.push([-180, lat]);
    const projected = ring.map(c => ol.proj.fromLonLat(c, this.flatProjection));
    return new ol.Feature(new ol.geom.Polygon([projected]));
  }

  // offset: [x, y] in pixels, to keep markers that share a point apart
  addFlatMarker(element, coords, layer, zIndex, offset = [0, 0]) {
    const overlay = new ol.Overlay({
      position: ol.proj.fromLonLat(coords, this.flatProjection),
      positioning: 'center-center',
      offset,
      element,
      stopEvent: false
    });
    this.flatMap.addOverlay(overlay);
    // z-index on the OL wrapper decides which layer is drawn on top
    const wrapper = overlay.getElement()?.parentElement;
    if (wrapper && zIndex !== undefined) wrapper.style.zIndex = String(zIndex);
    this.flatMarkers.push({ overlay, element, layer });
    return overlay;
  }

  // ─── Markers ────────────────────────────────────────────────────────────────

  // Build a marker element showing an image with a coloured border and glow.
  // shape: 'circle' | 'rounded' (10% radius, organisations and logos)
  // fit: 'cover' (photos, cropped) or 'contain' (logos, whole image shown)
  // padding: white space in px between the border and the image
  // badge: optional element placed over the image (honorary icon, "S" badge)
  createImageMarker({ src, size, shape = 'circle', fit = 'cover', padding = 0, className = '', border, glow, hoverGlow, badge, label }) {
    const el = document.createElement('div');
    el.className = className;
    el.style.width = `${size}px`;
    el.style.height = `${size}px`;
    el.style.cursor = 'pointer';
    el.style.transition = 'opacity 0.3s ease';
    if (label) {
      el.setAttribute('role', 'button');
      el.setAttribute('tabindex', '0');
      el.setAttribute('aria-label', label);
      el.title = label;
    }

    const wrapper = document.createElement('div');
    wrapper.style.position = 'relative';
    wrapper.style.width = '100%';
    wrapper.style.height = '100%';

    const img = document.createElement('img');
    img.src = src;
    img.alt = '';
    img.style.width = '100%';
    img.style.height = '100%';
    img.style.borderRadius = shape === 'rounded' ? '10%' : '50%';
    img.style.border = border;
    img.style.boxShadow = glow;
    img.style.objectFit = fit;
    img.style.padding = `${padding}px`;
    img.style.boxSizing = 'border-box';
    img.style.background = 'white';
    img.style.display = 'block';
    img.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
    wrapper.appendChild(img);

    if (badge) wrapper.appendChild(badge);
    el.appendChild(wrapper);

    el.addEventListener('mouseenter', () => {
      img.style.transform = 'scale(1.15)';
      img.style.boxShadow = hoverGlow || glow;
    });
    el.addEventListener('mouseleave', () => {
      img.style.transform = 'scale(1)';
      img.style.boxShadow = glow;
    });

    return { el, img };
  }

  // Click and keyboard activation for a marker element.
  onMarkerActivate(el, handler) {
    el.addEventListener('click', (e) => {
      e.stopPropagation();
      handler(e);
    });
    el.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        handler(e);
      }
    });
  }

  _isOnVisibleHemisphere(coords) {
    const center = this.globeMap.getCenter();
    const [lng, lat] = coords;
    const centerLng = center.lng;
    const centerLat = center.lat;

    let normalizedDLng = lng - centerLng;
    while (normalizedDLng > 180) normalizedDLng -= 360;
    while (normalizedDLng < -180) normalizedDLng += 360;

    const lat1Rad = centerLat * Math.PI / 180;
    const lat2Rad = lat * Math.PI / 180;
    const dLat = lat - centerLat;
    const dLngRad = normalizedDLng * Math.PI / 180;

    const a = Math.sin(dLat * Math.PI / 360) ** 2 +
              Math.cos(lat1Rad) * Math.cos(lat2Rad) *
              Math.sin(dLngRad / 2) ** 2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    const distance = c * 180 / Math.PI;
    return distance <= 85;
  }

  updateMarkerVisibility() {
    if (!this.globeMap) return;

    this.globeMarkers.forEach(({ coords, element, layer }) => {
      const visible = this.isLayerVisible(layer) && this._isOnVisibleHemisphere(coords);
      element.style.opacity = visible ? '1' : '0';
      element.style.pointerEvents = visible ? 'auto' : 'none';
      element.style.visibility = visible ? 'visible' : 'hidden';
    });
  }

  updateAllMarkersVisibility() {
    if (this.currentView === 'globe') {
      this.updateMarkerVisibility();
    } else {
      this.flatMarkers.forEach(({ element, layer }) => {
        element.style.display = this.isLayerVisible(layer) ? 'block' : 'none';
      });
    }
  }

  // ─── Popups ─────────────────────────────────────────────────────────────────

  // Show one popup (by id) and hide the others.
  openPopup(id) {
    this.popupIds.forEach(other => {
      if (other !== id) document.getElementById(other)?.classList.remove('active');
    });
    this.updateUrlState();
    const popup = document.getElementById(id);
    popup?.classList.add('active');
    document.getElementById('popup-overlay')?.classList.add('active');
    popup?.querySelector('.tooltip-close')?.focus({ preventScroll: true });
  }

  closePopup() {
    this.popupIds.forEach(id => document.getElementById(id)?.classList.remove('active'));
    document.getElementById('popup-overlay')?.classList.remove('active');
    this.clearActivePopup();
    this.updateUrlState();
  }

  // ─── URL State ──────────────────────────────────────────────────────────────

  readUrlState() {
    const params = new URLSearchParams(window.location.search);

    const view = params.get('view');
    if (view === 'flat' || view === 'globe') {
      this.currentView = view;
      // Sync button active states immediately
      this._setToggleState(document.getElementById('globe-view-btn'), view === 'globe');
      this._setToggleState(document.getElementById('flat-view-btn'), view === 'flat');
    }

    this.readExtraUrlState(params);
  }

  updateUrlState() {
    const params = new URLSearchParams(window.location.search);
    params.set('view', this.currentView);
    this.writeExtraUrlState(params);

    const newUrl = `${window.location.pathname}?${params.toString()}${window.location.hash}`;
    history.replaceState(null, '', newUrl);
  }

  // ─── Rotation ───────────────────────────────────────────────────────────────

  startRotation() {
    if (this.isRotating || !this.globeMap) return;

    this.isRotating = true;
    const secondsPerRevolution = 30;
    const maxSpinZoom = 5;
    const slowSpinZoom = 3;

    const rotateCamera = (timestamp) => {
      if (!this.isRotating) return;

      const zoom = this.globeMap.getZoom();
      if (zoom < maxSpinZoom) {
        let distancePerSecond = 360 / secondsPerRevolution;
        if (zoom > slowSpinZoom) {
          const zoomDif = (maxSpinZoom - zoom) / (maxSpinZoom - slowSpinZoom);
          distancePerSecond *= zoomDif;
        }
        const center = this.globeMap.getCenter();
        center.lng -= distancePerSecond / 60;
        this.globeMap.easeTo({ center, duration: 1000 / 60, easing: (t) => t });
      }

      this.rotationAnimation = requestAnimationFrame(rotateCamera);
    };

    this.rotationAnimation = requestAnimationFrame(rotateCamera);
  }

  stopRotation() {
    this.isRotating = false;
    if (this.rotationAnimation) {
      cancelAnimationFrame(this.rotationAnimation);
      this.rotationAnimation = null;
    }
  }
}

// Wait for MapLibre and OpenLayers, then call `start`.
function whenMapLibsReady(start) {
  if (typeof maplibregl === 'undefined' || typeof ol === 'undefined') {
    setTimeout(() => whenMapLibsReady(start), 100);
    return;
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
}
