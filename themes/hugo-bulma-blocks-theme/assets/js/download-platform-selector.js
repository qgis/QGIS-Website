// Platform Selector - Bulma-based Download Page
(function() {
    'use strict';

    // Detect user's operating system
    function detectOS() {
        const userAgent = navigator.userAgent.toLowerCase();
        
        if (/Mobile|iP(hone|od|ad)|Android|BlackBerry|IEMobile|Kindle|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune/i.test(userAgent)) {
            return 'mobile';
        } else if (userAgent.includes('mac')) {
            return 'macos';
        } else if (userAgent.includes('linux')) {
            return 'linux';
        }
        return 'windows';
    }

    // Get platform display name with FontAwesome icon
    function getPlatformDisplayName(platform) {
        const names = {
            'windows': '<span class="icon"><i class="fab fa-windows"></i></span><span>Windows - Desktop OS</span>',
            'macos': '<span class="icon"><i class="fab fa-apple"></i></span><span>macOS - Apple Desktop</span>',
            'linux': '<span class="icon"><i class="fab fa-linux"></i></span><span>Linux - Open Source OS</span>',
            'bsd': '<span class="icon"><i class="fab fa-freebsd"></i></span><span>BSD</span>',
            'container': '<span class="icon"><i class="fab fa-docker"></i></span><span>Container Images</span>',
            'mobile': '<span class="icon"><i class="fas fa-mobile-alt"></i></span><span>Mobile & Tablet - Android & iOS</span>',
            'source': '<span class="icon"><i class="fas fa-code"></i></span><span>Source Code</span>',
            'example': '<span class="icon"><i class="fas fa-database"></i></span><span>Example Datasets</span>'
        };
        return names[platform] || '<span class="icon"><i class="fab fa-windows"></i></span><span>Windows - Desktop OS</span>';
    }

    // Initialize platform selector on page load
    function initPlatformSelector() {
        const dropdown = document.getElementById('platform-dropdown');
        const selectedPlatformText = document.getElementById('selected-platform-text');
        const platformOptions = document.querySelectorAll('.platform-option');
        const platformContents = document.querySelectorAll('.platform-content');
        const bannerButtons = document.querySelectorAll('.platform-buttons');
        
        if (!dropdown) {
            return; // Not on download page
        }

        // Detect and set default platform
        const defaultPlatform = checkStoredPreference() || detectOS();
        
        // Set up Bulma dropdown click handlers
        platformOptions.forEach(option => {
            option.addEventListener('click', function(e) {
                e.preventDefault();
                const platform = this.dataset.platform;
                
                // Update selected platform text
                if (selectedPlatformText) {
                    selectedPlatformText.innerHTML = getPlatformDisplayName(platform);
                }
                
                // Activate platform content
                activatePlatform(platform);
                
                // Update banner download buttons
                updateBannerButtons(platform);
                
                // Close dropdown (Bulma will handle this, but we can force it)
                dropdown.classList.remove('is-active');
            });
        });

        // Initial setup
        if (selectedPlatformText) {
            selectedPlatformText.innerHTML = getPlatformDisplayName(defaultPlatform);
        }
        activatePlatform(defaultPlatform);
        updateBannerButtons(defaultPlatform);

        // Update banner download buttons for current platform
        function updateBannerButtons(platform) {
            // Hide all platform buttons
            bannerButtons.forEach(btn => {
                btn.style.display = 'none';
            });
            
            // Show buttons for selected platform
            const activePlatformButtons = document.querySelector(`.platform-buttons[data-platform="${platform}"]`);
            if (activePlatformButtons) {
                activePlatformButtons.style.display = 'block';
            }
        }

        // Make dropdown work with click
        const dropdownTrigger = dropdown.querySelector('.dropdown-trigger');
        if (dropdownTrigger) {
            dropdownTrigger.addEventListener('click', function(e) {
                e.stopPropagation();
                dropdown.classList.toggle('is-active');
            });
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            if (!dropdown.contains(e.target)) {
                dropdown.classList.remove('is-active');
            }
        });
    }

    // Activate a specific platform
    function activatePlatform(platform) {
        const platformContents = document.querySelectorAll('.platform-content');

        // Update content visibility
        platformContents.forEach(content => {
            if (content.dataset.platform === platform) {
                content.classList.add('active');
                content.setAttribute('aria-hidden', 'false');
            } else {
                content.classList.remove('active');
                content.setAttribute('aria-hidden', 'true');
            }
        });

        // Store preference
        try {
            localStorage.setItem('qgis-preferred-platform', platform);
        } catch (e) {
            // localStorage might not be available
        }
    }

    // Check for stored preference on load
    function checkStoredPreference() {
        try {
            const storedPlatform = localStorage.getItem('qgis-preferred-platform');
            if (storedPlatform) {
                const validPlatforms = ['windows', 'macos', 'linux', 'bsd', 'container', 'mobile', 'source', 'example'];
                if (validPlatforms.includes(storedPlatform)) {
                    return storedPlatform;
                }
            }
        } catch (e) {
            // localStorage might not be available
        }
        return null;
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initPlatformSelector);
    } else {
        initPlatformSelector();
    }

    // Expose function globally for potential external use
    window.qgisPlatformSelector = {
        activatePlatform: activatePlatform,
        detectOS: detectOS
    };
})();


function thanks(element) {
    event.preventDefault();
    window.open(element.href);
    // Redirect to thank you page after a short delay
    setTimeout(function() {
        window.location.href = '/download/thank-you';
    }, 500);
}
