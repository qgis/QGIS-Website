/**
 * Linux Packages Explorer
 * Simplified file browser for Linux packages (Ubuntu/Debian)
 * No search functionality for performance with large file lists
 */

(function() {
    'use strict';
    
    // Cache DOM elements
    const resultsCount = document.getElementById('linux-results-count');
    const resultsInfo = document.getElementById('linux-results-info');
    const noResults = document.getElementById('linux-no-results');
    const breadcrumbNav = document.getElementById('linux-breadcrumb');
    const fileList = document.getElementById('linux-files-tbody');
    
    // Store tree data
    let treeData = null;
    let totalFiles = 0;
    let currentPath = [];
    let currentNode = null;
    let currentSort = { field: 'name', order: 'asc' };
    
    // Use core utilities
    const core = window.S3ExplorerCore;
    
    // Public initialization function
    window.initLinuxPackagesExplorer = function(data) {
        if (!data || !data.tree) {
            console.error('Linux Packages Explorer: Invalid data provided', data);
            return;
        }
        
        // Parse tree if it's a string
        if (typeof data.tree === 'string') {
            try {
                treeData = JSON.parse(data.tree);
            } catch (e) {
                console.error('Linux Packages Explorer: Failed to parse tree data', e);
                return;
            }
        } else {
            treeData = data.tree;
        }
        
        totalFiles = data.totalFiles || 0;
        currentNode = treeData;
        
        try {
            init();
        } catch (e) {
            console.error('Linux Packages Explorer: Initialization failed', e);
        }
    };
    
    function init() {
        if (!fileList) {
            console.error('Linux Packages Explorer: Required elements not found');
            return;
        }
        
        attachEventListeners();
        core.updateSortIcons(currentSort);
        
        // Initialize from URL hash
        loadFromUrl();
    }
    
    function attachEventListeners() {
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
                renderCurrentDirectory();
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
        
        // Browser back/forward button support
        window.addEventListener('popstate', function(e) {
            loadFromUrl();
        });
    }
    
    function navigateToPath(pathArray, updateUrl = true) {
        currentPath = pathArray;
        currentNode = treeData;
        
        // Traverse the tree to find the current node
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
        const hash = window.location.hash.substring(1);
        
        if (!hash) {
            navigateToPath([], false);
            return;
        }
        
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
        if (resultsCount) {
            resultsCount.textContent = totalItems;
        }
        if (resultsInfo) {
            resultsInfo.textContent = `Showing ${totalItems} item${totalItems !== 1 ? 's' : ''}`;
        }
        
        // Show/hide no results
        if (totalItems === 0) {
            if (noResults) noResults.style.display = 'block';
            if (resultsInfo) resultsInfo.style.display = 'none';
        } else {
            if (noResults) noResults.style.display = 'none';
            if (resultsInfo) resultsInfo.style.display = 'block';
        }
    }
    
})();
