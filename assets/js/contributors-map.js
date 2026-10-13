// Contributors Map JavaScript - Using MapLibre GL (Globe) and OpenLayers (Flat Map)
// The shared globe/flat behaviour lives in globe-flat-map.js (GlobeFlatMap).
// This site file overrides the theme's assets/js/contributors-map.js.

const CODE_LAYER = 'code';
const SUPPORTING_LAYER = 'supporting';

class ContributorsMap extends GlobeFlatMap {
  constructor(contributorsData, supportingData) {
    super({
      globeCenter: [150, 10], // Australia coordinates
      popupIds: ['contributor-popup', 'supporting-contributor-popup']
    });
    this.contributorsData = contributorsData;
    this.supportingData = supportingData || { features: [] };
    // Filter state
    this.showCodeContributors = true;
    this.showSupportingContributors = true;
    // Active popup tracking (for URL state)
    this.activeContributorId = null;
    this.activeSupportingId = null;

    this.init();
  }

  setupEventListeners() {
    super.setupEventListeners();

    // Category filter checkboxes
    document.getElementById('filter-code')?.addEventListener('change', (e) => {
      this.showCodeContributors = e.target.checked;
      this.updateAllMarkersVisibility();
      this.updateUrlState();
    });

    document.getElementById('filter-supporting')?.addEventListener('change', (e) => {
      this.showSupportingContributors = e.target.checked;
      this.updateAllMarkersVisibility();
      this.updateUrlState();
    });
  }

  isLayerVisible(layer) {
    if (layer === CODE_LAYER) return this.showCodeContributors;
    if (layer === SUPPORTING_LAYER) return this.showSupportingContributors;
    return true;
  }

  onGlobeLoad() {
    // Add supporting first so code contributors render on top
    this._supportingWithValidCoords().forEach(({ contributor, coords }) => {
      this.addGlobeMarker(this._supportingMarker(contributor.properties), coords, SUPPORTING_LAYER);
    });

    const contributorsWithLocation = this._contributorsWithLocation()
      .sort((a, b) => a.properties.total_contributions - b.properties.total_contributions);

    this.globeMap.addSource('contributors', {
      type: 'geojson',
      data: { type: 'FeatureCollection', features: contributorsWithLocation }
    });

    contributorsWithLocation.forEach((contributor) => {
      this.addGlobeMarker(this._codeMarker(contributor.properties), contributor.geometry.coordinates, CODE_LAYER);
    });
  }

  onFlatLoad() {
    // Add supporting first so code contributors render on top
    this._supportingWithValidCoords().forEach(({ contributor, coords }) => {
      this.addFlatMarker(this._supportingMarker(contributor.properties), coords, SUPPORTING_LAYER, 1);
    });
    this._contributorsWithLocation().forEach((contributor) => {
      this.addFlatMarker(this._codeMarker(contributor.properties), contributor.geometry.coordinates, CODE_LAYER, 2);
    });
  }

  // ─── Code Contributors ──────────────────────────────────────────────────────

  _contributorsWithLocation() {
    return this.contributorsData.features
      .filter(f => f.geometry && f.geometry.coordinates);
  }

  _codeMarker(props) {
    const isHonorary = props.is_honorary || false;
    const honoraryIcon = props.honorary_icon || '';

    let badge = null;
    if (isHonorary && honoraryIcon) {
      badge = document.createElement('div');
      badge.style.position = 'absolute';
      badge.style.top = '-4px';
      badge.style.left = '-4px';
      badge.style.fontSize = '1rem';
      badge.style.filter = 'drop-shadow(1px 1px 2px rgba(0,0,0,0.3))';
      badge.style.zIndex = '10';
      badge.textContent = honoraryIcon;
    }

    const { el } = this.createImageMarker({
      src: props.avatar_url || '/img/default-avatar.png',
      size: this.getMarkerSize(props.total_contributions) * 3,
      border: isHonorary ? '3px solid #ee7913' : '2px solid #589632',
      glow: isHonorary ? '0 0 15px rgba(238,121,19,0.8)' : '0 0 10px rgba(88,150,50,0.8)',
      hoverGlow: isHonorary ? '0 0 20px rgba(238,121,19,0.9)' : '0 0 15px rgba(88,150,50,0.9)',
      badge
    });
    this.onMarkerActivate(el, (e) => this.showContributorPopup(props, e));
    return el;
  }

  // ─── Supporting Contributors ─────────────────────────────────────────────────

  _supportingWithValidCoords() {
    const valid = [];
    this.supportingData.features
      .filter(f => f.geometry && f.geometry.coordinates)
      .forEach((contributor) => {
        let coords = [...contributor.geometry.coordinates];
        // Auto-fix swapped [lat, lng] → [lng, lat] (GeoJSON requires [lng, lat])
        if (coords[1] > 90 || coords[1] < -90) {
          console.warn(`Auto-fixing swapped coordinates for "${contributor.properties.name}": [${coords[0]}, ${coords[1]}] → [${coords[1]}, ${coords[0]}]`);
          coords = [coords[1], coords[0]];
        }
        if (coords[1] > 90 || coords[1] < -90 || coords[0] > 180 || coords[0] < -180) {
          console.warn(`Skipping "${contributor.properties.name}": invalid coordinates [${coords[0]}, ${coords[1]}]`);
          return;
        }
        valid.push({ contributor, coords });
      });
    return valid;
  }

  _supportingMarker(props) {
    const isOrg = props.is_organization || false;

    // "S" badge — top-right corner
    const badge = document.createElement('div');
    badge.className = 'supporting-s-badge-marker';
    badge.textContent = 'S';

    const { el } = this.createImageMarker({
      src: props.avatar_img || '/img/default-avatar.png',
      size: 36,
      shape: isOrg ? 'rounded' : 'circle',
      className: 'supporting-globe-marker',
      border: '2px solid #f39c12',
      glow: '0 0 10px rgba(243,156,18,0.7)',
      hoverGlow: '0 0 18px rgba(243,156,18,0.9)',
      badge
    });
    this.onMarkerActivate(el, (e) => this.showSupportingContributorPopup(props, e));
    return el;
  }

  // ─── Size helper ─────────────────────────────────────────────────────────────

  getMarkerSize(contributions) {
    if (contributions > 10000) return 28;
    if (contributions > 5000) return 22;
    if (contributions > 1000) return 18;
    if (contributions > 500) return 14;
    return 12;
  }

  // ─── Popups ──────────────────────────────────────────────────────────────────

  showContributorPopup(contributor, event) {
    const popup = document.getElementById('contributor-popup');
    const popupCard = document.getElementById('popup-card');
    
    if (!popup) return;
    
    const isHonorary = contributor.is_honorary || false;
    const honoraryIcon = contributor.honorary_icon || '';
    const honoraryTitle = contributor.honorary_title || '';
    
    if (isHonorary) {
      popupCard.classList.add('honorary-member');
    } else {
      popupCard.classList.remove('honorary-member');
    }
    
    document.getElementById('popup-avatar').src = contributor.avatar_url || '/img/default-avatar.png';
    
    const avatarContainer = popup.querySelector('.avatar-container');
    let honoraryBadge = avatarContainer.querySelector('.honorary-badge');
    let honoraryInfo = avatarContainer.querySelector('.honorary-info');
    
    if (isHonorary) {
      if (!honoraryBadge) {
        honoraryBadge = document.createElement('span');
        honoraryBadge.className = 'honorary-badge';
        avatarContainer.appendChild(honoraryBadge);
      }
      honoraryBadge.textContent = honoraryIcon;
      if (!honoraryInfo) {
        honoraryInfo = document.createElement('div');
        honoraryInfo.className = 'honorary-info';
        avatarContainer.appendChild(honoraryInfo);
      }
      honoraryInfo.innerHTML = `<p class="is-size-6 has-text-grey">${honoraryTitle}</p>`;
    } else {
      if (honoraryBadge) honoraryBadge.remove();
      if (honoraryInfo) honoraryInfo.remove();
    }
    
    const usernameLink = document.getElementById('popup-username-link');
    usernameLink.textContent = contributor.login;
    usernameLink.href = `https://github.com/${contributor.login}`;
    
    document.getElementById('popup-total-contributions').textContent = 
      contributor.total_contributions.toLocaleString();
    
    const thematicsList = document.getElementById('popup-thematics-list');
    thematicsList.innerHTML = '';
    
    const standardProps = ['login', 'avatar_url', 'total_contributions', 'has_github_account'];
    const thematics = [];
    Object.keys(contributor).forEach(key => {
      if (!standardProps.includes(key) && typeof contributor[key] === 'number' && contributor[key] > 0) {
        thematics.push({ name: key, count: contributor[key] });
      }
    });
    thematics.sort((a, b) => b.count - a.count);
    
    thematics.forEach(thematic => {
      const badge = document.createElement('span');
      badge.className = `contributor-badge contributor-badge-${thematic.name}`;
      
      let icon = '', label = '';
      if (thematic.name === 'documentation') { icon = '<i class="fas fa-book mr-1"></i>'; label = 'QGIS Documentation'; }
      else if (thematic.name === 'qgis_core') { icon = '<i class="fas fa-code mr-1"></i>'; label = 'QGIS Core'; }
      else if (thematic.name === 'web_sites') { icon = '<i class="fas fa-globe mr-1"></i>'; label = 'QGIS Web Sites'; }
      else if (thematic.name === 'community_activities') { icon = '<i class="fas fa-users mr-1"></i>'; label = 'Community'; }
      else if (thematic.name === 'qgis_infrastructure') { icon = '<i class="fas fa-server mr-1"></i>'; label = 'Infrastructure'; }
      
      badge.innerHTML = `<span>${icon}${label}</span><span class="contribution-count"><i class="fab fa-git-alt"></i>${thematic.count}</span>`;
      thematicsList.appendChild(badge);
    });
    
    this.activeContributorId = contributor.login;
    this.activeSupportingId = null;
    this.openPopup('contributor-popup');
  }

  showSupportingContributorPopup(props, event) {
    const popup = document.getElementById('supporting-contributor-popup');
    if (!popup) return;

    const isOrg = props.is_organization || false;
    const isActive = props.is_active !== false;

    // Avatar
    const avatarEl = document.getElementById('supporting-popup-avatar');
    avatarEl.src = props.avatar_img || '/img/default-avatar.png';
    avatarEl.style.borderRadius = isOrg ? '10%' : '50%';

    // Name / link
    const nameLink = document.getElementById('supporting-popup-name-link');
    const nameText = document.getElementById('supporting-popup-name-text');
    if (props.link) {
      nameLink.textContent = props.name;
      nameLink.href = props.link;
      nameLink.style.display = '';
      nameText.style.display = 'none';
    } else {
      nameText.textContent = props.name;
      nameText.style.display = '';
      nameLink.style.display = 'none';
    }

    // Status badge
    const statusEl = document.getElementById('supporting-popup-status');
    if (isActive) {
      statusEl.innerHTML = '<span class="tag is-success is-light is-small"><i class="fas fa-circle mr-1"></i>Active</span>';
    } else {
      statusEl.innerHTML = '<span class="tag is-light is-small has-text-grey"><i class="fas fa-circle mr-1"></i>Past contributor</span>';
    }

    // Date range
    const datesEl = document.getElementById('supporting-popup-dates');
    if (props.start_date || props.end_date) {
      const start = props.start_date ? new Date(props.start_date).getFullYear() : '?';
      const end = props.end_date ? new Date(props.end_date).getFullYear() : 'present';
      datesEl.innerHTML = `<i class="fas fa-calendar-alt mr-1"></i>${start} – ${end}`;
      datesEl.style.display = '';
    } else {
      datesEl.style.display = 'none';
    }

    // Description
    const descEl = document.getElementById('supporting-popup-description');
    if (props.contribution_description) {
      descEl.textContent = props.contribution_description;
      descEl.style.display = '';
    } else {
      descEl.style.display = 'none';
    }

    // Roles
    const rolesEl = document.getElementById('supporting-popup-roles');
    rolesEl.innerHTML = '';
    (props.roles || []).forEach(role => {
      const badge = document.createElement('span');
      badge.className = 'contributor-badge contributor-badge-community_activities';
      badge.innerHTML = `<span><i class="fas fa-award mr-1"></i>${role}</span>`;
      rolesEl.appendChild(badge);
    });

    this.activeSupportingId = props.name;
    this.activeContributorId = null;
    this.openPopup('supporting-contributor-popup');
  }
  
  clearActivePopup() {
    this.activeContributorId = null;
    this.activeSupportingId = null;
  }

  // ─── URL State ───────────────────────────────────────────────────────────────

  readExtraUrlState(params) {
    if (params.has('showCode')) {
      this.showCodeContributors = params.get('showCode') !== 'false';
      const cb = document.getElementById('filter-code');
      if (cb) cb.checked = this.showCodeContributors;
    }

    if (params.has('showSupporting')) {
      this.showSupportingContributors = params.get('showSupporting') !== 'false';
      const cb = document.getElementById('filter-supporting');
      if (cb) cb.checked = this.showSupportingContributors;
    }

    this.activeContributorId = params.get('contributor') || null;
    this.activeSupportingId = params.get('supportingContributor') || null;
  }

  writeExtraUrlState(params) {
    if (!this.showCodeContributors) {
      params.set('showCode', 'false');
    } else {
      params.delete('showCode');
    }

    if (!this.showSupportingContributors) {
      params.set('showSupporting', 'false');
    } else {
      params.delete('showSupporting');
    }

    if (this.activeContributorId) {
      params.set('contributor', this.activeContributorId);
      params.delete('supportingContributor');
    } else if (this.activeSupportingId) {
      params.set('supportingContributor', this.activeSupportingId);
      params.delete('contributor');
    } else {
      params.delete('contributor');
      params.delete('supportingContributor');
    }
  }

  restorePopup() {
    if (this.activeContributorId) {
      const feature = this.contributorsData.features.find(
        f => f.properties.login === this.activeContributorId
      );
      if (feature) this.showContributorPopup(feature.properties, null);
    } else if (this.activeSupportingId) {
      const feature = this.supportingData.features.find(
        f => f.properties.name === this.activeSupportingId
      );
      if (feature) this.showSupportingContributorPopup(feature.properties, null);
    }
  }
}

// ─── Bootstrap ────────────────────────────────────────────────────────────────

function initContributorsMap() {
  const spinner = document.querySelector('.loading-spinner');

  Promise.all([
    fetch('/data/contributors/contributors_map.json').then(r => {
      if (!r.ok) throw new Error(`contributors_map.json: HTTP ${r.status}`);
      return r.json();
    }),
    fetch('/data/contributors/supporting_map.json').then(r => {
      if (!r.ok) {
        console.warn('supporting_map.json not found, skipping.');
        return { features: [] };
      }
      return r.json();
    })
  ])
    .then(([contributorsData, supportingData]) => {
      console.log(
        'Data loaded:',
        contributorsData.features.length, 'code contributors,',
        supportingData.features.length, 'supporting contributors'
      );
      new ContributorsMap(contributorsData, supportingData);
      if (spinner) spinner.style.display = 'none';
    })
    .catch(error => {
      console.error('Error loading contributors data:', error);
      if (spinner) {
        spinner.textContent = 'Error loading contributors data. Please try refreshing the page.';
        spinner.style.color = '#ee7913';
      }
    });
}

whenMapLibsReady(initContributorsMap);
