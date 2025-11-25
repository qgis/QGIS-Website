/**
 * S3 File Explorer
 * Interactive file browser for S3 bucket contents
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
        updateSortIcons();
        renderCurrentDirectory();
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
                
                updateSortIcons();
                
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
                const url = row.dataset.downloadUrl;
                const name = row.dataset.fileName;
                // Trigger download
                const a = document.createElement('a');
                a.href = url;
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
    }
    
    function updateSortIcons() {
        const sortableHeaders = document.querySelectorAll('th.sortable');
        sortableHeaders.forEach(header => {
            const icon = header.querySelector('.sort-icon i');
            const field = header.getAttribute('data-sort');
            
            if (field === currentSort.field) {
                icon.className = currentSort.order === 'asc' ? 'fas fa-sort-up' : 'fas fa-sort-down';
            } else {
                icon.className = 'fas fa-sort';
            }
        });
    }
    
    function navigateToPath(pathArray) {
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
        
        renderBreadcrumb();
        renderCurrentDirectory();
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
        files = sortFiles(files);
        
        // Render the list
        let html = '';
        
        // Render folders first
        folders.forEach(folder => {
            const fileCount = countFilesInFolder(folder);
            html += `
                <tr style="cursor: pointer;" data-type="folder" data-folder-name="${folder.name}">
                    <td>
                        <span class="icon-text">
                            <span class="icon has-text-warning">
                                <i class="fas fa-folder"></i>
                            </span>
                            <span>${folder.name}</span>
                        </span>
                        <br><small class="has-text-grey">${fileCount} item${fileCount !== 1 ? 's' : ''}</small>
                    </td>
                    <td class="is-hidden-mobile">—</td>
                    <td class="is-hidden-mobile">—</td>
                </tr>
            `;
        });
        
        // Render files
        files.forEach(file => {
            const icon = getCategoryIcon(file.category);
            const color = getCategoryColor(file.category);
            html += `
                <tr style="cursor: pointer;" data-type="file" data-download-url="${file.download_url}" data-file-name="${file.name}">
                    <td>
                        <span class="icon-text">
                            <span class="icon has-text-${color}">
                                <i class="${icon}"></i>
                            </span>
                            <span><a href="${file.download_url}" class="file-link" title="${file.download_url}">${file.name}</a></span>
                        </span>
                    </td>
                    <td class="is-hidden-mobile">${file.size_formatted}</td>
                    <td class="is-hidden-mobile">${formatDate(file.last_modified)}</td>
                </tr>
            `;
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
    function searchTree(node, searchTerm, results = [], currentPath = '') {
        // Search files in current node
        if (node.files) {
            node.files.forEach(file => {
                if (file.name.toLowerCase().includes(searchTerm)) {
                    results.push({
                        ...file,
                        path: currentPath || file.path
                    });
                }
            });
        }
        
        // Recursively search children
        if (node.children) {
            node.children.forEach(child => {
                const childPath = currentPath ? `${currentPath}/${child.name}` : child.name;
                searchTree(child, searchTerm, results, childPath);
            });
        }
        
        return results;
    }
    
    // Render search results
    function renderSearchResults(searchTerm) {
        const results = searchTree(treeData, searchTerm);
        
        // Sort results
        const sortedResults = sortFiles(results);
        
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
            const icon = getCategoryIcon(file.category);
            const color = getCategoryColor(file.category);
            html += `
                <tr style="cursor: pointer;" data-type="file" data-download-url="${file.download_url}" data-file-name="${file.name}">
                    <td>
                        <span class="icon-text">
                            <span class="icon has-text-${color}">
                                <i class="${icon}"></i>
                            </span>
                            <span><a href="${file.download_url}" class="file-link" title="${file.download_url}">${file.name}</a></span>
                        </span>
                        <br>
                        <small class="has-text-grey">${file.path}</small>
                    </td>
                    <td class="is-hidden-mobile">${file.size_formatted}</td>
                    <td class="is-hidden-mobile">${formatDate(file.last_modified)}</td>
                </tr>
            `;
        });
        
        fileList.innerHTML = html;
    }
    
    function sortFiles(files) {
        return [...files].sort((a, b) => {
            let valueA, valueB;
            
            switch (currentSort.field) {
                case 'name':
                    valueA = a.name.toLowerCase();
                    valueB = b.name.toLowerCase();
                    return currentSort.order === 'asc' ? 
                        valueA.localeCompare(valueB) : 
                        valueB.localeCompare(valueA);
                case 'size':
                    valueA = a.size || 0;
                    valueB = b.size || 0;
                    return currentSort.order === 'asc' ? valueA - valueB : valueB - valueA;
                case 'date':
                    valueA = a.last_modified_timestamp || 0;
                    valueB = b.last_modified_timestamp || 0;
                    return currentSort.order === 'asc' ? valueA - valueB : valueB - valueA;
                default:
                    return 0;
            }
        });
    }
    
    function countFilesInFolder(folder) {
        let count = folder.files ? folder.files.length : 0;
        if (folder.children) {
            folder.children.forEach(child => {
                count += countFilesInFolder(child);
            });
        }
        return count;
    }
    
    function resetFilters() {
        searchInput.value = '';
        searchClear.style.display = 'none';
        currentSort = { field: 'name', order: 'asc' };
        isSearching = false;
        updateSortIcons();
        renderCurrentDirectory();
    }
    
    function formatDate(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const diffTime = Math.abs(now - date);
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        
        if (diffDays < 1) {
            return 'Today';
        } else if (diffDays < 2) {
            return 'Yesterday';
        } else if (diffDays < 7) {
            return `${diffDays} days ago`;
        } else {
            return date.toLocaleDateString('en-US', { 
                year: 'numeric', 
                month: 'short', 
                day: 'numeric' 
            });
        }
    }
    
    function getCategoryIcon(category) {
        const icons = {
            'installer': 'fas fa-box-open',
            'archive': 'fas fa-file-archive',
            'document': 'fas fa-file-alt',
            'image': 'fas fa-file-image',
            'video': 'fas fa-file-video',
            'data': 'fas fa-database',
            'source': 'fas fa-file-code',
            'other': 'fas fa-file'
        };
        return icons[category] || icons['other'];
    }
    
    function getCategoryColor(category) {
        const colors = {
            'installer': 'primary',
            'archive': 'info',
            'document': 'link',
            'image': 'success',
            'video': 'danger',
            'data': 'warning',
            'source': 'grey',
            'other': 'grey-light'
        };
        return colors[category] || colors['other'];
    }
    
})();
