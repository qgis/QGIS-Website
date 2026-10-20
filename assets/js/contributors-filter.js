/**
 * Contributors Filter, Search, View Toggle and Table Sort
 *
 * This site file overrides the theme's assets/js/contributors-filter.js. It
 * also drives the local user groups list (layouts/shortcodes/user-groups-list.html).
 * Provides filtering, search, grid/table view toggle, and sortable table
 * for the individual contributors page.
 * Features:
 * - URL parameter support for sharing filtered/sorted views
 * - Multiple thematic filters
 * - Real-time search
 * - Grid / Table view toggle
 * - Sortable table columns
 * - Clickable badges to activate thematic filters
 *
 * Grid cards and table rows are matched on their `data-login` attribute so
 * both views are driven by a single filtered list.
 *
 * Other lists (e.g. local user groups) reuse this script with the same DOM
 * hooks. They configure it through attributes on #contributors-table-view:
 * - data-default-sort="col:dir"   default table sort (default "total:desc")
 * - data-text-cols="a b"          columns sorted as text (default "login")
 * and, optionally, an #include-inactive checkbox: items with
 * data-active="false" stay hidden unless it is checked.
 */

class ContributorsFilter {
    constructor() {
        this.contributors = [];
        this.filteredContributors = [];
        this.activeThematicFilters = new Set();
        this.searchQuery = '';
        this.currentView = 'grid';
        this.includeInactive = false;

        this.init();
    }

    init() {
        this.cacheElements();
        this.readConfig();
        this.parseContributors();
        this.loadFromURL();
        this.attachEventListeners();
        this.applyFilters();
    }

    cacheElements() {
        this.searchInput = document.getElementById('contributor-search');
        this.filterButtons = document.querySelectorAll('.filter-button');
        this.resetButton = document.getElementById('reset-filters');
        this.gridContainer = document.getElementById('contributors-grid-view');
        this.gridDivider = document.getElementById('contributors-grid-divider');
        this.tableContainer = document.getElementById('contributors-table-view');
        this.tableBody = document.getElementById('contributors-table-body');
        this.statsShowing = document.getElementById('stats-showing');
        this.statsTotal = document.getElementById('stats-total');
        this.noResultsElement = document.querySelector('.contributors-no-results');
        this.gridBtn = document.getElementById('view-grid-btn');
        this.tableBtn = document.getElementById('view-table-btn');
        this.sortableHeaders = document.querySelectorAll('#contributors-table-view th.sortable');
        this.inactiveToggle = document.getElementById('include-inactive');
    }

    readConfig() {
        const config = this.tableContainer ? this.tableContainer.dataset : {};
        const [col, dir] = (config.defaultSort || 'total:desc').split(':');
        this.defaultSortCol = col || 'total';
        this.defaultSortDir = dir === 'asc' ? 'asc' : 'desc';
        this.textCols = new Set((config.textCols || 'login').split(' ').filter(Boolean));
        this.sortCol = this.defaultSortCol;
        this.sortDir = this.defaultSortDir;
    }

    parseContributors() {
        const rowsByLogin = new Map();
        document.querySelectorAll('.contributor-table-row').forEach(row => {
            rowsByLogin.set(row.dataset.login, row);
        });

        document.querySelectorAll('.contributor-card-column').forEach(column => {
            const login = column.dataset.login || '';
            const thematics = (column.dataset.thematics || '').split(' ').filter(Boolean);
            // Extra searchable text (names, countries...) beyond the login
            const extraSearch = column.dataset.search || '';

            this.contributors.push({
                element: column,
                row: rowsByLogin.get(login) || null,
                login: login,
                isPinned: column.dataset.pinned === 'true',
                isActive: column.dataset.active !== 'false',
                thematics: thematics,
                searchText: [login, extraSearch, ...thematics.map(t => t.replace(/[_-]/g, ' '))]
                    .join(' ')
                    .toLowerCase()
            });
        });

        this.filteredContributors = [...this.contributors];
    }

    loadFromURL() {
        const params = new URLSearchParams(window.location.search);

        const searchParam = params.get('search');
        if (searchParam) {
            this.searchQuery = searchParam.toLowerCase().trim();
            if (this.searchInput) this.searchInput.value = searchParam;
        }

        const filtersParam = params.get('filters');
        if (filtersParam) {
            filtersParam.split(',').filter(f => f.trim()).forEach(f => {
                this.activeThematicFilters.add(f.trim());
            });
        }

        const viewParam = params.get('view');
        if (viewParam === 'table') this.currentView = 'table';

        if (this.inactiveToggle && params.get('inactive') === '1') {
            this.includeInactive = true;
            this.inactiveToggle.checked = true;
        }

        const sortParam = params.get('sort');
        if (sortParam) {
            const [col, dir] = sortParam.split(':');
            if (col) this.sortCol = col;
            if (dir === 'asc' || dir === 'desc') this.sortDir = dir;
        }

        this.updateFilterButtonsUI();
    }

    updateFilterButtonsUI() {
        this.filterButtons.forEach(button => {
            const thematic = button.dataset.thematic;
            button.classList.toggle('is-active', this.activeThematicFilters.has(thematic));
        });

        document.querySelectorAll('.badge-filter-btn').forEach(badge => {
            const active = this.activeThematicFilters.has(badge.dataset.thematic);
            badge.classList.toggle('is-filter-active', active);
            badge.setAttribute('aria-pressed', String(active));
        });
    }

    applyViewToggle() {
        const isTable = this.currentView === 'table';
        const hasResults = this.filteredContributors.length > 0;

        if (this.gridContainer) {
            this.gridContainer.style.display = (!isTable && hasResults) ? '' : 'none';
        }
        if (this.tableContainer) {
            this.tableContainer.style.display = (isTable && hasResults) ? '' : 'none';
        }
        this.setViewButtonState(this.gridBtn, !isTable);
        this.setViewButtonState(this.tableBtn, isTable);
    }

    setViewButtonState(button, isSelected) {
        if (!button) return;
        button.classList.toggle('is-active', isSelected);
        button.classList.toggle('is-primary3', isSelected);
        button.setAttribute('aria-pressed', String(isSelected));
    }

    updateURL() {
        const params = new URLSearchParams();

        if (this.searchQuery) params.set('search', this.searchQuery);
        if (this.activeThematicFilters.size > 0) {
            params.set('filters', Array.from(this.activeThematicFilters).join(','));
        }
        if (this.currentView === 'table') params.set('view', 'table');
        if (this.includeInactive) params.set('inactive', '1');
        if (this.sortCol !== this.defaultSortCol || this.sortDir !== this.defaultSortDir) {
            params.set('sort', `${this.sortCol}:${this.sortDir}`);
        }

        const newURL = params.toString()
            ? `${window.location.pathname}?${params.toString()}`
            : window.location.pathname;

        window.history.replaceState({}, '', newURL);
    }

    attachEventListeners() {
        if (this.searchInput) {
            this.searchInput.addEventListener('input', (e) => {
                this.searchQuery = e.target.value.toLowerCase().trim();
                this.applyFilters();
                this.updateURL();
            });
        }

        this.filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                this.toggleThematicFilter(button.dataset.thematic);
            });
        });

        if (this.resetButton) {
            this.resetButton.addEventListener('click', () => this.resetFilters());
        }

        if (this.gridBtn) {
            this.gridBtn.addEventListener('click', () => this.switchView('grid'));
        }

        if (this.inactiveToggle) {
            this.inactiveToggle.addEventListener('change', () => {
                this.includeInactive = this.inactiveToggle.checked;
                this.applyFilters();
                this.updateURL();
            });
        }

        if (this.tableBtn) {
            this.tableBtn.addEventListener('click', () => this.switchView('table'));
        }

        this.sortableHeaders.forEach(th => {
            th.addEventListener('click', () => {
                const col = th.dataset.col;
                if (this.sortCol === col) {
                    this.sortDir = this.sortDir === 'asc' ? 'desc' : 'asc';
                } else {
                    this.sortCol = col;
                    this.sortDir = this.textCols.has(col) ? 'asc' : 'desc';
                }
                this.sortTable();
                this.updateURL();
            });
        });

        document.querySelectorAll('.badge-filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                this.toggleThematicFilter(btn.dataset.thematic);
            });
        });
    }

    toggleThematicFilter(thematic) {
        if (!thematic) return;

        if (this.activeThematicFilters.has(thematic)) {
            this.activeThematicFilters.delete(thematic);
        } else {
            this.activeThematicFilters.add(thematic);
        }
        this.updateFilterButtonsUI();
        this.applyFilters();
        this.updateURL();
    }

    switchView(view) {
        this.currentView = view;
        this.applyViewToggle();
        if (view === 'table') this.sortTable();
        this.updateURL();
    }

    applyFilters() {
        this.filteredContributors = this.contributors.filter(contributor => {
            const thematicMatch = this.activeThematicFilters.size === 0
                || contributor.thematics.some(t => this.activeThematicFilters.has(t));

            const searchMatch = !this.searchQuery
                || contributor.searchText.includes(this.searchQuery);

            const activeMatch = this.includeInactive || contributor.isActive;

            return thematicMatch && searchMatch && activeMatch;
        });

        this.updateDisplay();
        this.updateStats();
        this.applyViewToggle();
        if (this.currentView === 'table') this.sortTable();
    }

    updateDisplay() {
        const visible = new Set(this.filteredContributors);

        this.contributors.forEach(contributor => {
            const display = visible.has(contributor) ? '' : 'none';
            contributor.element.style.display = display;
            if (contributor.row) contributor.row.style.display = display;
        });

        // The divider only makes sense when the pinned founder and at least one
        // other contributor are both visible.
        if (this.gridDivider) {
            const pinnedVisible = this.filteredContributors.some(c => c.isPinned);
            const othersVisible = this.filteredContributors.some(c => !c.isPinned);
            this.gridDivider.style.display = (pinnedVisible && othersVisible) ? '' : 'none';
        }

        if (this.filteredContributors.length > 0) {
            this.hideNoResults();
        } else {
            this.showNoResults();
        }
    }

    sortTable() {
        if (!this.tableBody) return;

        const rows = Array.from(this.tableBody.querySelectorAll('.contributor-table-row'));
        const pinnedRows = rows.filter(r => r.dataset.pinned);
        const sortableRows = rows.filter(r => !r.dataset.pinned);

        const col = this.sortCol;
        const dir = this.sortDir;

        sortableRows.sort((a, b) => {
            const aVal = a.dataset[col] || '';
            const bVal = b.dataset[col] || '';

            if (this.textCols.has(col)) {
                return dir === 'asc' ? aVal.localeCompare(bVal) : bVal.localeCompare(aVal);
            }

            const aNum = parseFloat(aVal) || 0;
            const bNum = parseFloat(bVal) || 0;
            return dir === 'asc' ? aNum - bNum : bNum - aNum;
        });

        const fragment = document.createDocumentFragment();
        [...pinnedRows, ...sortableRows].forEach(row => fragment.appendChild(row));
        this.tableBody.appendChild(fragment);

        this.updateSortIcons();
    }

    updateSortIcons() {
        this.sortableHeaders.forEach(th => {
            const icon = th.querySelector('.sort-icon i');
            if (!icon) return;
            icon.className = 'fas fa-sort';
            if (th.dataset.col === this.sortCol) {
                icon.className = this.sortDir === 'asc' ? 'fas fa-sort-up' : 'fas fa-sort-down';
            }
        });
    }

    updateStats() {
        const total = this.includeInactive
            ? this.contributors.length
            : this.contributors.filter(c => c.isActive).length;
        if (this.statsShowing) this.statsShowing.textContent = this.filteredContributors.length;
        if (this.statsTotal) this.statsTotal.textContent = total;
    }

    showNoResults() {
        if (this.noResultsElement) this.noResultsElement.style.display = 'block';
    }

    hideNoResults() {
        if (this.noResultsElement) this.noResultsElement.style.display = 'none';
    }

    resetFilters() {
        if (this.searchInput) this.searchInput.value = '';
        this.searchQuery = '';
        this.activeThematicFilters.clear();
        this.updateFilterButtonsUI();
        this.applyFilters();
        this.updateURL();

        const filterSection = document.querySelector('.contributors-filter-section');
        if (filterSection) filterSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    if (document.querySelector('.contributor-card-column')) {
        new ContributorsFilter();
    }
});
