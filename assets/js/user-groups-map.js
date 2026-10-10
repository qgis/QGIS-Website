// User Groups Map - Using MapLibre GL (Globe) and OpenLayers (Flat Map)
// Highlights every country with an active QGIS user group and shows the
// group logos as markers. The shared globe/flat behaviour lives in
// globe-flat-map.js (GlobeFlatMap).
//
// Data:
// - groups: fetched from /data/user_groups/user_groups.json, the published
//   GeoJSON built from data/user_groups/groups.json (as the contributors map
//   fetches /data/contributors/contributors_map.json)
// - country outlines: embedded by the shortcode in #user-groups-countries
//   (data/user_groups/countries.json, not published as a file)

const GROUP_LAYER = 'groups';
const MARKER_SIZE = 48;
const COUNTRY_FILL = '#589632';
const COUNTRY_LINE = '#3d6b22';

// Regional indicator symbols, e.g. "CH" -> 🇨🇭
function flagEmoji(countryCode) {
  if (!/^[A-Z]{2}$/.test(countryCode || '')) return '';
  return String.fromCodePoint(...[...countryCode].map(c => 0x1F1E6 + c.charCodeAt(0) - 65));
}

class UserGroupsMap extends GlobeFlatMap {
  constructor(groupsData, countriesData, strings) {
    super({
      globeCenter: [10, 30],
      popupIds: ['user-group-popup']
    });
    this.strings = strings;
    this.groups = groupsData.features
      .filter(f => f.properties.active && f.geometry && f.geometry.coordinates)
      .map(f => ({ ...f.properties, coords: f.geometry.coordinates }));
    this.groupsByCountry = new Map();
    this.groups.forEach(group => {
      if (!this.groupsByCountry.has(group.country)) this.groupsByCountry.set(group.country, []);
      this.groupsByCountry.get(group.country).push(group);
    });
    // Groups in the same country share its label point: lay their logos
    // side by side, centred on the point.
    this.groupsByCountry.forEach(groups => {
      groups.forEach((group, i) => {
        group.offset = [(i - (groups.length - 1) / 2) * (MARKER_SIZE + 6), 0];
      });
    });
    // Only draw countries that still have an active group
    this.countriesData = {
      type: 'FeatureCollection',
      features: countriesData.features.filter(f => this.groupsByCountry.has(f.properties.iso_a2))
    };
    this.activeGroupSlug = null;
    this.activeCountry = null;
    this.hoveredCountry = null;

    this.init();
  }

  // ─── Globe ──────────────────────────────────────────────────────────────────

  onGlobeLoad() {
    this.globeMap.addSource('user-group-countries', {
      type: 'geojson',
      data: this.countriesData,
      promoteId: 'iso_a2'
    });
    this.globeMap.addLayer({
      id: 'user-group-countries-fill',
      type: 'fill',
      source: 'user-group-countries',
      paint: {
        'fill-color': COUNTRY_FILL,
        'fill-opacity': ['case', ['boolean', ['feature-state', 'hover'], false], 0.75, 0.5]
      }
    });
    this.globeMap.addLayer({
      id: 'user-group-countries-line',
      type: 'line',
      source: 'user-group-countries',
      paint: { 'line-color': COUNTRY_LINE, 'line-width': 1.5 }
    });

    this.globeMap.on('mousemove', 'user-group-countries-fill', (e) => {
      const code = e.features[0]?.properties.iso_a2;
      if (code === this.hoveredCountry) return;
      this._setGlobeHover(code);
      this.globeMap.getCanvas().style.cursor = 'pointer';
    });
    this.globeMap.on('mouseleave', 'user-group-countries-fill', () => {
      this._setGlobeHover(null);
      this.globeMap.getCanvas().style.cursor = '';
    });
    this.globeMap.on('click', 'user-group-countries-fill', (e) => {
      const code = e.features[0]?.properties.iso_a2;
      if (code) {
        this.stopRotation();
        this.showCountryPopup(code);
      }
    });

    this.groups.forEach(group => {
      this.addGlobeMarker(this._logoMarker(group), group.coords, GROUP_LAYER, group.offset);
    });
  }

  _setGlobeHover(code) {
    if (this.hoveredCountry) {
      this.globeMap.setFeatureState({ source: 'user-group-countries', id: this.hoveredCountry }, { hover: false });
    }
    this.hoveredCountry = code;
    if (code) {
      this.globeMap.setFeatureState({ source: 'user-group-countries', id: code }, { hover: true });
    }
  }

  // ─── Flat map ───────────────────────────────────────────────────────────────

  onFlatLoad() {
    const fillFor = (opacity) => new ol.style.Style({
      fill: new ol.style.Fill({ color: this._rgba(COUNTRY_FILL, opacity) }),
      stroke: new ol.style.Stroke({ color: COUNTRY_LINE, width: 1.5 })
    });
    const normal = fillFor(0.5);
    const hover = fillFor(0.75);

    this.countryLayer = new ol.layer.Vector({
      source: new ol.source.Vector({
        features: new ol.format.GeoJSON().readFeatures(this.countriesData, {
          featureProjection: this.flatProjection
        })
      }),
      style: (feature) => feature.get('iso_a2') === this.hoveredCountry ? hover : normal
    });
    this.flatMap.addLayer(this.countryLayer);

    this.flatMap.on('pointermove', (evt) => {
      if (evt.dragging) return;
      const code = this._countryAtPixel(evt.pixel);
      if (code !== this.hoveredCountry) {
        this.hoveredCountry = code;
        this.countryLayer.changed();
      }
      this.flatMap.getTargetElement().style.cursor = code ? 'pointer' : '';
    });

    this.groups.forEach(group => {
      this.addFlatMarker(this._logoMarker(group), group.coords, GROUP_LAYER, 2, group.offset);
    });
  }

  onFlatMapClick(evt) {
    const code = this._countryAtPixel(evt.pixel);
    if (!code) return false;
    this.showCountryPopup(code);
    return true;
  }

  _countryAtPixel(pixel) {
    const feature = this.flatMap.forEachFeatureAtPixel(pixel, f => f, {
      layerFilter: layer => layer === this.countryLayer
    });
    return feature ? feature.get('iso_a2') : null;
  }

  _rgba(hex, alpha) {
    const n = parseInt(hex.slice(1), 16);
    return `rgba(${(n >> 16) & 255}, ${(n >> 8) & 255}, ${n & 255}, ${alpha})`;
  }

  // ─── Markers ────────────────────────────────────────────────────────────────

  _logoMarker(group) {
    const { el } = this.createImageMarker({
      src: this._logoUrl(group),
      size: MARKER_SIZE,
      shape: 'circle',
      fit: 'contain',
      padding: 7,
      className: 'user-group-marker',
      border: `2px solid ${COUNTRY_FILL}`,
      glow: '0 0 10px rgba(88,150,50,0.8)',
      hoverGlow: '0 0 16px rgba(88,150,50,0.95)',
      label: group.name
    });
    this.onMarkerActivate(el, () => {
      this.stopRotation();
      this.showGroupPopup(group.slug);
    });
    return el;
  }

  _logoUrl(group) {
    return '/' + (group.logo || this.strings.defaultLogo);
  }

  // ─── Popup ──────────────────────────────────────────────────────────────────

  showGroupPopup(slug) {
    const group = this.groups.find(g => g.slug === slug);
    if (!group) return;
    this.activeGroupSlug = slug;
    this.activeCountry = null;
    this._renderPopup(group.country_name, [group]);
  }

  showCountryPopup(code) {
    const groups = this.groupsByCountry.get(code);
    if (!groups) return;
    // A single group: share the group link rather than the country one
    if (groups.length === 1) {
      this.showGroupPopup(groups[0].slug);
      return;
    }
    this.activeGroupSlug = null;
    this.activeCountry = code;
    this._renderPopup(groups[0].country_name, groups);
  }

  _renderPopup(countryName, groups) {
    const title = document.getElementById('user-group-popup-title');
    const flag = document.createElement('span');
    flag.className = 'flag-emoji mr-2';
    flag.setAttribute('aria-hidden', 'true');
    flag.textContent = flagEmoji(groups[0].country);
    title.replaceChildren(flag, document.createTextNode(countryName));

    const body = document.getElementById('user-group-popup-body');
    const template = document.getElementById('user-group-entry-template');
    body.replaceChildren(...groups.map(group => {
      const entry = template.content.firstElementChild.cloneNode(true);
      const logo = entry.querySelector('.user-group-entry-logo');
      logo.src = this._logoUrl(group);

      const nameLink = entry.querySelector('.user-group-entry-name');
      nameLink.textContent = group.name;
      if (group.website) {
        nameLink.href = group.website;
      } else {
        nameLink.removeAttribute('href');
      }

      entry.querySelector('.user-group-entry-since').textContent =
        this.strings.since.replace('__YEAR__', group.year);

      const contacts = entry.querySelector('.user-group-entry-contacts');
      if (group.contacts && group.contacts.length) {
        contacts.textContent = this.strings.contact.replace('__NAMES__', group.contacts.join(', '));
      } else {
        contacts.remove();
      }

      const visit = entry.querySelector('.user-group-entry-visit');
      if (group.website) {
        visit.href = group.website;
      } else {
        visit.remove();
      }
      return entry;
    }));

    this.openPopup('user-group-popup');
  }

  clearActivePopup() {
    this.activeGroupSlug = null;
    this.activeCountry = null;
  }

  restorePopup() {
    if (this.activeGroupSlug) {
      this.showGroupPopup(this.activeGroupSlug);
    } else if (this.activeCountry) {
      this.showCountryPopup(this.activeCountry);
    }
  }

  // ─── URL State ──────────────────────────────────────────────────────────────

  readExtraUrlState(params) {
    this.activeGroupSlug = params.get('group') || null;
    this.activeCountry = params.get('country') || null;
  }

  writeExtraUrlState(params) {
    params.delete('group');
    params.delete('country');
    if (this.activeGroupSlug) params.set('group', this.activeGroupSlug);
    else if (this.activeCountry) params.set('country', this.activeCountry);
  }
}

// ─── Bootstrap ────────────────────────────────────────────────────────────────

function initUserGroupsMap() {
  const container = document.querySelector('.user-groups-map');
  const spinner = container?.querySelector('.loading-spinner');
  const countriesEl = document.getElementById('user-groups-countries');
  if (!container || !countriesEl) return;

  const strings = {
    since: container.dataset.since,
    contact: container.dataset.contact,
    defaultLogo: container.dataset.defaultLogo
  };

  fetch(container.dataset.groupsUrl)
    .then(r => {
      if (!r.ok) throw new Error(`user_groups.json: HTTP ${r.status}`);
      return r.json();
    })
    .then(groupsData => {
      new UserGroupsMap(groupsData, JSON.parse(countriesEl.textContent), strings);
      if (spinner) spinner.style.display = 'none';
    })
    .catch(error => {
      console.error('Error loading user groups map:', error);
      if (spinner) {
        spinner.textContent = container.dataset.loadError;
        spinner.style.color = '#ee7913';
      }
    });
}

whenMapLibsReady(initUserGroupsMap);
