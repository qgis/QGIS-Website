/**
 * Contributors Filter and Search
 * Provides filtering and search functionality for the individual contributors page
 * Features:
 * - URL parameter support for sharing filtered views
 * - Multiple thematic filters (checkboxes)
 * - Real-time search
 * - Better no-results handling
 */

class ContributorsFilter {
    constructor() {
        this.contributors = [];
        this.filteredContributors = [];
        this.activeThematicFilters = new Set();
        this.searchQuery = '';
        
        this.init();
    }

    init() {
        this.cacheElements();
        this.parseContributors();
        this.loadFromURL();
        this.attachEventListeners();
        this.applyFilters();
    }

    cacheElements() {
        this.searchInput = document.getElementById('contributor-search');
        this.filterButtons = document.querySelectorAll('.filter-button');
        this.resetButton = document.getElementById('reset-filters');
        this.contributorsContainer = document.querySelector('.columns.is-multiline');
        this.statsShowing = document.getElementById('stats-showing');
        this.statsTotal = document.getElementById('stats-total');
        this.noResultsElement = document.querySelector('.contributors-no-results');
    }

    parseContributors() {
        // Parse all contributor cards from the DOM
        const cards = document.querySelectorAll('.contributor-card.individual');
        
        cards.forEach(card => {
            const contributor = {
                element: card.closest('.column'),
                login: card.querySelector('.title.is-4 a.external-link')?.textContent.trim() || '',
                isHonorary: card.classList.contains('honorary-member'),
                thematics: [],
                searchText: ''
            };

            // Extract thematics from badges
            const badges = card.querySelectorAll('.contributor-badge');
            badges.forEach(badge => {
                const classes = Array.from(badge.classList);
                const thematicClass = classes.find(cls => cls.startsWith('contributor-badge-'));
                if (thematicClass) {
                    const thematic = thematicClass.replace('contributor-badge-', '');
                    contributor.thematics.push(thematic);
                }
            });

            // Build search text (login + thematics for better searching)
            contributor.searchText = [
                contributor.login,
                ...contributor.thematics.map(t => t.replace(/_/g, ' '))
            ].join(' ').toLowerCase();

            this.contributors.push(contributor);
        });

        this.filteredContributors = [...this.contributors];
    }

    loadFromURL() {
        const params = new URLSearchParams(window.location.search);
        
        // Load search query
        const searchParam = params.get('search');
        if (searchParam) {
            this.searchQuery = searchParam.toLowerCase().trim();
            if (this.searchInput) {
                this.searchInput.value = searchParam;
            }
        }
        
        // Load filters
        const filtersParam = params.get('filters');
        if (filtersParam) {
            const filters = filtersParam.split(',').filter(f => f.trim());
            filters.forEach(filter => {
                this.activeThematicFilters.add(filter.trim());
            });
        }
        
        // Update UI to match loaded state
        this.updateFilterButtonsUI();
    }

    updateFilterButtonsUI() {
        this.filterButtons.forEach(button => {
            const thematic = button.dataset.thematic;
            if (this.activeThematicFilters.has(thematic)) {
                button.classList.add('is-active');
            } else {
                button.classList.remove('is-active');
            }
        });
    }

    updateURL() {
        const params = new URLSearchParams();
        
        // Add search parameter
        if (this.searchQuery) {
            params.set('search', this.searchQuery);
        }
        
        // Add filters parameter
        if (this.activeThematicFilters.size > 0) {
            params.set('filters', Array.from(this.activeThematicFilters).join(','));
        }
        
        // Update URL without reloading page
        const newURL = params.toString() 
            ? `${window.location.pathname}?${params.toString()}`
            : window.location.pathname;
        
        window.history.replaceState({}, '', newURL);
    }

    attachEventListeners() {
        // Search input
        if (this.searchInput) {
            this.searchInput.addEventListener('input', (e) => {
                this.searchQuery = e.target.value.toLowerCase().trim();
                this.applyFilters();
                this.updateURL();
            });
        }

        // Thematic filter buttons (multiple selection)
        this.filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                const thematic = button.dataset.thematic;
                
                // Toggle filter
                if (this.activeThematicFilters.has(thematic)) {
                    this.activeThematicFilters.delete(thematic);
                    button.classList.remove('is-active');
                } else {
                    this.activeThematicFilters.add(thematic);
                    button.classList.add('is-active');
                }
                
                this.applyFilters();
                this.updateURL();
            });
        });

        // Reset button
        if (this.resetButton) {
            this.resetButton.addEventListener('click', () => {
                this.resetFilters();
            });
        }
    }

    applyFilters() {
        this.filteredContributors = this.contributors.filter(contributor => {
            // Apply thematic filter (multiple)
            let thematicMatch = true;
            if (this.activeThematicFilters.size > 0) {
                // Contributor must have at least one of the selected thematics
                thematicMatch = contributor.thematics.some(t => 
                    this.activeThematicFilters.has(t)
                );
            }

            // Apply search filter
            let searchMatch = true;
            if (this.searchQuery) {
                searchMatch = contributor.searchText.includes(this.searchQuery);
            }

            return thematicMatch && searchMatch;
        });

        this.updateDisplay();
        this.updateStats();
    }

    updateDisplay() {
        // Hide all contributors first
        this.contributors.forEach(contributor => {
            contributor.element.style.display = 'none';
        });

        // Show filtered contributors
        if (this.filteredContributors.length > 0) {
            this.filteredContributors.forEach(contributor => {
                contributor.element.style.display = '';
            });
            this.hideNoResults();
        } else {
            this.showNoResults();
        }
    }

    updateStats() {
        if (this.statsShowing) {
            this.statsShowing.textContent = this.filteredContributors.length;
        }
        if (this.statsTotal) {
            this.statsTotal.textContent = this.contributors.length;
        }
    }

    showNoResults() {
        if (this.noResultsElement) {
            this.noResultsElement.style.display = 'block';
        }
        // Keep the container visible but empty
        if (this.contributorsContainer) {
            this.contributorsContainer.style.display = '';
        }
    }

    hideNoResults() {
        if (this.noResultsElement) {
            this.noResultsElement.style.display = 'none';
        }
        if (this.contributorsContainer) {
            this.contributorsContainer.style.display = '';
        }
    }

    resetFilters() {
        // Reset search
        if (this.searchInput) {
            this.searchInput.value = '';
        }
        this.searchQuery = '';

        // Reset thematic filters
        this.activeThematicFilters.clear();
        this.filterButtons.forEach(btn => btn.classList.remove('is-active'));

        // Apply filters and update URL
        this.applyFilters();
        this.updateURL();

        // Scroll to top of filter section
        const filterSection = document.querySelector('.contributors-filter-section');
        if (filterSection) {
            filterSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Check if we're on the contributors page
    const contributorsContainer = document.querySelector('.contributor-card.individual');
    if (contributorsContainer) {
        new ContributorsFilter();
    }
});
