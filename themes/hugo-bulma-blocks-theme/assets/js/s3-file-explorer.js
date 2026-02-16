/**
 * S3 File Explorer
 * Interactive file browser for S3 bucket contents with search
 */

(function() {
    'use strict';
    
    // Cache DOM elements
    const searchInput = document.getElementById('s3-search-input');
    const resultsCount = document.getElementById('s3-results-count');
    const resultsInfo = document.getElementById('s3-results-info');
    const noResults = document.getElementById('s3-no-results');
    const searchClear = document.getElementById('search-clear');
    const resetButton = document.getElementById('reset-filters');
    const resetButtonNoResults = document.getElementById('reset-filters-no-results');
    const breadcrumbNav = document.getElementById('s3-breadcrumb');
    const fileList = document.getElementById('s3-files-tbody');
    
    // Store tree data
    let treeData = null;
    let totalFiles = 0;
    let currentPath = [];
    let currentNode = null;
    let currentSort = { field: 'name', order: 'asc' };
    let isSearching = false;
    
    let searchTimeout = null;
    
    // Use core utilities
    const core = window.S3ExplorerCore;
    
    // Public initialization function
    window.initS3Explorer = function(data) {
        // Parse tree if it's a string
        if (typeof data.tree === 'string') {
            try {
                treeData = JSON.parse(data.tree);
            } catch (e) {
                console.error('S3 Explorer: Failed to parse tree data', e);
                treeData = data.tree;
            }
        } else {
            treeData = data.tree;
        }
        
        totalFiles = data.totalFiles;
        currentNode = treeData;
        init();
    };
    
    function init() {
        if (!searchInput || !fileList) {
            console.error('S3 Explorer: Required elements not found');
            return;
        }
        
        attachEventListeners();
        core.updateSortIcons(currentSort);
        
        // Initialize from URL hash
        loadFromUrl();
    }
    
    function attachEventListeners() {
        // Search with debounce - global tree search
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const searchTerm = searchInput.value.trim().toLowerCase();
                if (searchTerm) {
                    isSearching = true;
                    renderSearchResults(searchTerm);
                } else {
                    isSearching = false;
                    renderCurrentDirectory();
                }
            }, 300);
            
            // Show/hide clear button
            searchClear.style.display = this.value ? 'flex' : 'none';
        });
        
        // Clear search
        searchClear.addEventListener('click', function() {
            searchInput.value = '';
            searchClear.style.display = 'none';
            isSearching = false;
            renderCurrentDirectory();
        });
        
        // Reset buttons
        resetButton.addEventListener('click', resetFilters);
        resetButtonNoResults.addEventListener('click', resetFilters);
        
        // Column header sorting
        const sortableHeaders = document.querySelectorAll('th.sortable');
        sortableHeaders.forEach(header => {
            header.style.cursor = 'pointer';
            header.addEventListener('click', function() {
                const field = this.getAttribute('data-sort');
                
                // Toggle order if clicking same column
                if (currentSort.field === field) {
                    currentSort.order = currentSort.order === 'asc' ? 'desc' : 'asc';
                } else {
                    currentSort.field = field;
                    currentSort.order = 'asc';
                }
                
                core.updateSortIcons(currentSort);
                
                // Re-render based on current mode
                if (isSearching) {
                    renderSearchResults(searchInput.value.trim().toLowerCase());
                } else {
                    renderCurrentDirectory();
                }
            });
        });
        
        // Row click handler for navigation and download
        fileList.addEventListener('click', function(e) {
            const row = e.target.closest('tr');
            if (!row) return;
            
            const type = row.dataset.type;
            
            if (type === 'folder') {
                const folderName = row.dataset.folderName;
                const newPath = [...currentPath, folderName];
                navigateToPath(newPath);
            } else if (type === 'file') {
                const key = row.dataset.fileKey;
                const name = row.dataset.fileName;
                // Trigger download
                const downloadUrl = core.getDownloadUrl(key);
                const a = document.createElement('a');
                a.href = downloadUrl;
                a.download = name;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }
        });
        
        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            // Ctrl/Cmd + K to focus search
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                searchInput.focus();
            }
            // Escape to clear search
            if (e.key === 'Escape' && searchInput.value) {
                searchInput.value = '';
                searchClear.style.display = 'none';
                isSearching = false;
                renderCurrentDirectory();
            }
        });
        
        // Browser back/forward button support
        window.addEventListener('popstate', function(e) {
            loadFromUrl();
        });
    }
    
    function navigateToPath(pathArray, updateUrl = true) {
        currentPath = pathArray;
        currentNode = treeData;
        
        // Traverse the tree to find the current node (case-sensitive)
        for (let i = 0; i < pathArray.length; i++) {
            const folderName = pathArray[i];
            const found = currentNode.children.find(child => child.name === folderName && child.type === 'folder');
            if (found) {
                currentNode = found;
            } else {
                console.error('Folder not found:', folderName);
                currentPath = [];
                currentNode = treeData;
                break;
            }
        }
        
        // Update URL hash
        if (updateUrl) {
            updateUrlHash();
        }
        
        renderBreadcrumb();
        renderCurrentDirectory();
    }
    
    function updateUrlHash() {
        const hash = currentPath.length > 0 ? '#' + currentPath.join('/') : '#';
        history.pushState({ path: currentPath }, '', hash);
    }
    
    function loadFromUrl() {
        const hash = window.location.hash.substring(1); // Remove '#'
        
        if (!hash) {
            // Root path
            navigateToPath([], false);
            return;
        }
        
        // Split path and filter empty segments
        const pathArray = hash.split('/').filter(segment => segment.length > 0);
        navigateToPath(pathArray, false);
    }
    
    function renderBreadcrumb() {
        if (!breadcrumbNav) return;
        
        let html = '<ul>';
        
        // Root/Home
        html += `<li><a href="#" data-path="" class="breadcrumb-item">
            <span class="icon is-small"><i class="fas fa-home"></i></span>
            <span>Home</span>
        </a></li>`;
        
        // Path segments
        currentPath.forEach((segment, index) => {
            const isLast = index === currentPath.length - 1;
            const pathStr = currentPath.slice(0, index + 1).join('|');
            
            if (isLast) {
                html += `<li class="is-active"><a href="#" aria-current="page">${segment}</a></li>`;
            } else {
                html += `<li><a href="#" data-path="${pathStr}" class="breadcrumb-item">${segment}</a></li>`;
            }
        });
        
        html += '</ul>';
        breadcrumbNav.innerHTML = html;
        
        // Attach click handlers
        const breadcrumbLinks = breadcrumbNav.querySelectorAll('.breadcrumb-item');
        breadcrumbLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const pathStr = this.getAttribute('data-path');
                const pathArray = pathStr ? pathStr.split('|') : [];
                navigateToPath(pathArray);
            });
        });
    }
    
    function renderCurrentDirectory() {
        // Get folders and files in current directory
        let folders = currentNode.children ? currentNode.children.filter(child => child.type === 'folder') : [];
        let files = currentNode.files || [];
        
        // Sort folders alphabetically
        folders.sort((a, b) => {
            return currentSort.order === 'asc' ? 
                a.name.localeCompare(b.name) : 
                b.name.localeCompare(a.name);
        });
        
        // Sort files
        files = core.sortFiles(files, currentSort.field, currentSort.order);
        
        // Render the list
        let html = '';
        
        // Render folders first
        folders.forEach(folder => {
            html += core.renderFolderRow(folder, currentPath);
        });
        
        // Render files
        files.forEach(file => {
            html += core.renderFileRow(file, false);
        });
        
        fileList.innerHTML = html;
        
        // Update count
        const totalItems = folders.length + files.length;
        resultsCount.textContent = totalItems;
        resultsInfo.textContent = `Showing ${totalItems} item${totalItems !== 1 ? 's' : ''}`;
        
        // Show/hide no results
        if (totalItems === 0) {
            noResults.style.display = 'block';
            resultsInfo.style.display = 'none';
        } else {
            noResults.style.display = 'none';
            resultsInfo.style.display = 'block';
        }
    }
    
    // Search across entire tree
    function renderSearchResults(searchTerm) {
        const results = core.searchTree(treeData, searchTerm);
        
        // Sort results
        const sortedResults = core.sortFiles(results, currentSort.field, currentSort.order);
        
        // Update results info
        resultsInfo.textContent = `Found ${results.length} file${results.length !== 1 ? 's' : ''}`;
        resultsCount.textContent = results.length;
        
        // Clear file list
        fileList.innerHTML = '';
        
        if (results.length === 0) {
            noResults.style.display = 'block';
            resultsInfo.style.display = 'none';
            return;
        }
        
        noResults.style.display = 'none';
        resultsInfo.style.display = 'block';
        
        // Render results
        let html = '';
        sortedResults.forEach(file => {
            html += core.renderFileRow(file, true);
        });
        
        fileList.innerHTML = html;
    }
    
    function resetFilters() {
        searchInput.value = '';
        searchClear.style.display = 'none';
        currentSort = { field: 'name', order: 'asc' };
        isSearching = false;
        core.updateSortIcons(currentSort);
        renderCurrentDirectory();
    }
    
})();
