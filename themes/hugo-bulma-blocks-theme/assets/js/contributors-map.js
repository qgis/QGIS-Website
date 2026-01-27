// Contributors Map JavaScript - Using MapLibre GL (Globe) and OpenLayers (Flat Map)

class ContributorsMap {
  constructor(contributorsData) {
    this.contributorsData = contributorsData;
    this.currentView = 'globe';
    this.globeMap = null;
    this.flatMap = null;
    this.vectorLayer = null;
    this.markers = [];
    this.isRotating = false;
    this.rotationAnimation = null;
    
    this.init();
  }
  
  init() {
    this.setupEventListeners();
    this.initGlobeView();
  }
  
  setupEventListeners() {
    // View toggle buttons
    document.getElementById('globe-view-btn')?.addEventListener('click', () => {
      this.switchView('globe');
    });
    
    document.getElementById('flat-view-btn')?.addEventListener('click', () => {
      this.switchView('flat');
    });
    
    // Popup close
    document.getElementById('popup-close')?.addEventListener('click', () => {
      this.closePopup();
    });
    
    document.getElementById('popup-overlay')?.addEventListener('click', () => {
      this.closePopup();
    });
  }
  
  switchView(view) {
    this.currentView = view;
    
    const globeView = document.getElementById('globe-view');
    const flatView = document.getElementById('flat-map-view');
    const globeBtn = document.getElementById('globe-view-btn');
    const flatBtn = document.getElementById('flat-view-btn');
    
    if (view === 'globe') {
      globeView.style.display = 'block';
      flatView.style.display = 'none';
      globeBtn?.classList.add('active');
      flatBtn?.classList.remove('active');
      
      if (!this.globeMap) {
        this.initGlobeView();
      } else {
        this.globeMap.resize();
      }
    } else {
      globeView.style.display = 'none';
      flatView.style.display = 'block';
      globeBtn?.classList.remove('active');
      flatBtn?.classList.add('active');
      
      if (!this.flatMap) {
        this.initFlatMap();
      } else {
        this.flatMap.updateSize();
      }
    }
  }
  
  initGlobeView() {
    // Use MapLibre GL v5.16.0 with globe projection
    this.globeMap = new maplibregl.Map({
      container: 'globe-view',
      zoom: 2.2,
      center: [150, 10], // Australia coordinates
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
        // light: {
        //   anchor: 'viewport',
        //   position: [1.15, 210, 50]
        // },
        // glyphs: 'https://demotiles.maplibre.org/font/{fontstack}/{range}.pbf'
      },
      maxZoom: 18,
      minZoom: 0
    });
    
    this.globeMap.on('load', () => {
      this.addContributorsToMapLibre();
    });
    
    // Stop rotation on any user interaction
    this.globeMap.on('mousedown', () => this.stopRotation());
    this.globeMap.on('touchstart', () => this.stopRotation());
    this.globeMap.on('wheel', () => this.stopRotation());
    this.globeMap.on('dblclick', () => this.stopRotation());
  }
  
  addContributorsToMapLibre() {
    const contributorsWithLocation = this.contributorsData.features
      .filter(f => f.geometry && f.geometry.coordinates)
      .sort((a, b) => a.properties.total_contributions - b.properties.total_contributions); // Smallest first
    
    // Add source for contributors
    this.globeMap.addSource('contributors', {
      type: 'geojson',
      data: {
        type: 'FeatureCollection',
        features: contributorsWithLocation
      }
    });
    
    // Load avatar images and create markers
    contributorsWithLocation.forEach((contributor, index) => {
      const coords = contributor.geometry.coordinates;
      const size = this.getMarkerSize(contributor.properties.total_contributions) * 3;
      const avatarUrl = contributor.properties.avatar_url || '/img/default-avatar.png';
      
      // Create marker element
      const el = document.createElement('div');
      el.className = 'maplibre-marker';
      el.style.width = `${size}px`;
      el.style.height = `${size}px`;
      el.style.cursor = 'pointer';
      el.style.transition = 'opacity 0.3s ease';
      
      const img = document.createElement('img');
      img.src = avatarUrl;
      img.style.width = '100%';
      img.style.height = '100%';
      img.style.borderRadius = '50%';
      img.style.border = '2px solid #589632';
      img.style.boxShadow = '0 0 10px rgba(88,150,50,0.8)';
      img.style.objectFit = 'cover';
      img.style.background = 'white';
      img.style.display = 'block';
      img.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
      
      el.appendChild(img);
      
      // Add hover effect
      el.addEventListener('mouseenter', () => {
        img.style.transform = 'scale(1.15)';
        img.style.boxShadow = '0 0 15px rgba(88,150,50,0.9)';
      });
      
      el.addEventListener('mouseleave', () => {
        img.style.transform = 'scale(1)';
        img.style.boxShadow = '0 0 10px rgba(88,150,50,0.8)';
      });
      
      // Add click handler
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        this.showContributorPopup(contributor.properties, e);
      });
      
      // Create and add marker
      const marker = new maplibregl.Marker({
        element: el,
        anchor: 'center'
      })
        .setLngLat(coords)
        .addTo(this.globeMap);
      
      this.markers.push({ marker, coords, element: el });
    });
    
    // Hide markers on the back side of the globe
    this.globeMap.on('move', () => {
      this.updateMarkerVisibility();
    });
    
    this.globeMap.on('moveend', () => {
      this.updateMarkerVisibility();
    });
    
    // Close tooltip on map click (outside markers)
    this.globeMap.on('click', (e) => {
      // Check if click was on canvas (not on a marker)
      const features = this.globeMap.queryRenderedFeatures(e.point);
      if (features.length === 0) {
        this.closePopup();
      }
    });
    
    // Initial visibility update
    this.updateMarkerVisibility();
    
    // Start rotation after a delay to ensure everything is fully loaded
    setTimeout(() => {
      this.startRotation();
    }, 500);
  }
  
  updateMarkerVisibility() {
    if (!this.globeMap || this.markers.length === 0) return;
    
    const center = this.globeMap.getCenter();
    const centerLng = center.lng;
    const centerLat = center.lat;
    
    this.markers.forEach(({ marker, coords, element }) => {
      const [lng, lat] = coords;
      
      // Calculate angular distance from center using proper spherical distance
      const dLng = lng - centerLng;
      const dLat = lat - centerLat;
      
      // Normalize longitude difference to -180 to 180
      let normalizedDLng = dLng;
      while (normalizedDLng > 180) normalizedDLng -= 360;
      while (normalizedDLng < -180) normalizedDLng += 360;
      
      // Convert to radians for accurate calculation
      const lat1Rad = centerLat * Math.PI / 180;
      const lat2Rad = lat * Math.PI / 180;
      const dLngRad = normalizedDLng * Math.PI / 180;
      
      // Haversine formula for great circle distance
      const a = Math.sin(dLat * Math.PI / 360) ** 2 +
                Math.cos(lat1Rad) * Math.cos(lat2Rad) *
                Math.sin(dLngRad / 2) ** 2;
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      const distance = c * 180 / Math.PI; // Convert back to degrees
      
      // Hide markers on the back hemisphere (> 90 degrees away)
      if (distance > 85) {
        element.style.opacity = '0';
        element.style.pointerEvents = 'none';
        element.style.visibility = 'hidden';
      } else {
        element.style.opacity = '1';
        element.style.pointerEvents = 'auto';
        element.style.visibility = 'visible';
      }
    });
  }
  
  initFlatMap() {
    // Define extent for Web Mercator projection (world bounds)
    const extent = ol.proj.transformExtent(
      [-180, -85, 180, 85],
      'EPSG:4326',
      'EPSG:3857'
    );
    
    const view = new ol.View({
      center: ol.proj.fromLonLat([0, 20]),
      zoom: 2,
      extent: extent,
      constrainOnlyCenter: false
    });
    
    this.flatMap = new ol.Map({
      target: 'flat-map-view',
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM()
        })
      ],
      view: view
    });
    
    // Close tooltip on map click (outside markers)
    this.flatMap.on('click', (evt) => {
      const pixel = this.flatMap.getEventPixel(evt.originalEvent);
      const hasFeature = this.flatMap.hasFeatureAtPixel(pixel);
      
      // Only close if not clicking on a contributor overlay
      let clickedOnOverlay = false;
      this.flatMap.getOverlays().forEach(overlay => {
        const element = overlay.getElement();
        if (element && element.contains(evt.originalEvent.target)) {
          clickedOnOverlay = true;
        }
      });
      
      if (!clickedOnOverlay) {
        this.closePopup();
      }
    });
    
    this.addContributorsToOpenLayers();
  }
  
  addContributorsToOpenLayers() {
    const contributorsWithLocation = this.contributorsData.features
      .filter(f => f.geometry && f.geometry.coordinates);
    
    // Data is already sorted by contribution (smallest first) from the script
    // Create overlays for each contributor (similar to MapLibre markers)
    contributorsWithLocation.forEach((contributor, index) => {
      const coords = contributor.geometry.coordinates;
      const size = this.getMarkerSize(contributor.properties.total_contributions) * 3;
      const avatarUrl = contributor.properties.avatar_url || '/img/default-avatar.png';
      
      // Create marker element
      const el = document.createElement('div');
      el.className = 'ol-marker';
      el.style.width = `${size}px`;
      el.style.height = `${size}px`;
      el.style.cursor = 'pointer';
      
      const img = document.createElement('img');
      img.src = avatarUrl;
      img.style.width = '100%';
      img.style.height = '100%';
      img.style.borderRadius = '50%';
      img.style.border = '2px solid #589632';
      img.style.boxShadow = '0 0 10px rgba(88,150,50,0.8)';
      img.style.objectFit = 'cover';
      img.style.background = 'white';
      img.style.display = 'block';
      img.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
      
      el.appendChild(img);
      
      // Add hover effect
      el.addEventListener('mouseenter', () => {
        img.style.transform = 'scale(1.15)';
        img.style.boxShadow = '0 0 15px rgba(88,150,50,0.9)';
      });
      
      el.addEventListener('mouseleave', () => {
        img.style.transform = 'scale(1)';
        img.style.boxShadow = '0 0 10px rgba(88,150,50,0.8)';
      });
      
      // Add click handler
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        this.showContributorPopup(contributor.properties, e);
      });
      
      // Create overlay
      const overlay = new ol.Overlay({
        position: ol.proj.fromLonLat(coords),
        positioning: 'center-center',
        element: el,
        stopEvent: false
      });
      
      this.flatMap.addOverlay(overlay);
    });
  }
  
  getMarkerSize(contributions) {
    // Size based on contributions (base sizes)
    if (contributions > 10000) return 28;
    if (contributions > 5000) return 22;
    if (contributions > 1000) return 18;
    if (contributions > 500) return 14;
    return 12;
  }
  
  showContributorPopup(contributor, event) {
    const popup = document.getElementById('contributor-popup');
    
    if (!popup) return;
    
    // Populate card content
    document.getElementById('popup-avatar').src = contributor.avatar_url || '/img/default-avatar.png';
    
    const usernameLink = document.getElementById('popup-username-link');
    usernameLink.textContent = contributor.login;
    usernameLink.href = `https://github.com/${contributor.login}`;
    
    document.getElementById('popup-total-contributions').textContent = 
      contributor.total_contributions.toLocaleString();
    
    // Populate thematics as badges
    const thematicsList = document.getElementById('popup-thematics-list');
    thematicsList.innerHTML = '';
    
    // Get thematics (excluding standard properties) and sort by count
    const standardProps = ['login', 'avatar_url', 'total_contributions', 'has_github_account'];
    const thematics = [];
    Object.keys(contributor).forEach(key => {
      if (!standardProps.includes(key) && typeof contributor[key] === 'number' && contributor[key] > 0) {
        thematics.push({ name: key, count: contributor[key] });
      }
    });
    
    // Sort by count descending
    thematics.sort((a, b) => b.count - a.count);
    
    // Create badges
    thematics.forEach(thematic => {
      const badge = document.createElement('span');
      badge.className = `contributor-badge contributor-badge-${thematic.name}`;
      
      let icon = '';
      let label = '';
      if (thematic.name === 'documentation') {
        icon = '<i class="fas fa-book mr-1"></i>';
        label = 'QGIS Documentation';
      } else if (thematic.name === 'qgis_core') {
        icon = '<i class="fas fa-code mr-1"></i>';
        label = 'QGIS Core';
      } else if (thematic.name === 'web_sites') {
        icon = '<i class="fas fa-globe mr-1"></i>';
        label = 'QGIS Web Sites';
      } else if (thematic.name === 'community_activities') {
        icon = '<i class="fas fa-users mr-1"></i>';
        label = 'Community';
      } else if (thematic.name === 'qgis_infrastructure') {
        icon = '<i class="fas fa-server mr-1"></i>';
        label = 'Infrastructure';
      }
      
      badge.innerHTML = `
        <span>${icon}${label}</span>
        <span class="contribution-count">
          <i class="fab fa-git-alt"></i>
          ${thematic.count}
        </span>
      `;
      
      thematicsList.appendChild(badge);
    });
    
    // Show popup (centered on screen)
    popup.classList.add('active');
    const overlay = document.getElementById('popup-overlay');
    overlay?.classList.add('active');
  }
  
  closePopup() {
    const popup = document.getElementById('contributor-popup');
    const overlay = document.getElementById('popup-overlay');
    
    popup?.classList.remove('active');
    overlay?.classList.remove('active');
  }
  
  formatThematicName(name) {
    return name
      .split('_')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(' ');
  }
  
  startRotation() {
    if (this.isRotating || !this.globeMap) return;
    
    this.isRotating = true;
    const secondsPerRevolution = 30; // 30 seconds for full rotation
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
        center.lng -= distancePerSecond / 60; // Assuming 60 fps
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

// Initialize map when DOM is loaded AND libraries are ready
function initContributorsMap() {
  // Check if libraries are loaded
  if (typeof maplibregl === 'undefined') {
    console.error('MapLibre GL not loaded yet, retrying...');
    setTimeout(initContributorsMap, 100);
    return;
  }
  
  if (typeof ol === 'undefined') {
    console.error('OpenLayers not loaded yet, retrying...');
    setTimeout(initContributorsMap, 100);
    return;
  }
  
  console.log('Libraries loaded, initializing map...');
  
  // Fetch contributors data
  const dataPath = '/data/contributors/contributors_map.json';
  
  fetch(dataPath)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      console.log('Contributors data loaded:', data.features.length, 'contributors');
      new ContributorsMap(data);
      
      // Hide loading spinner
      const spinner = document.querySelector('.loading-spinner');
      if (spinner) spinner.style.display = 'none';
    })
    .catch(error => {
      console.error('Error loading contributors data:', error);
      const spinner = document.querySelector('.loading-spinner');
      if (spinner) {
        spinner.textContent = 'Error loading contributors data. Please try refreshing the page.';
        spinner.style.color = '#ee7913';
      }
    });
}

// Start initialization when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initContributorsMap);
} else {
  initContributorsMap();
}
