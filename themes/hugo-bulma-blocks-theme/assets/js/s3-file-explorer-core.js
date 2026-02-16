/**
 * S3 File Explorer Core
 * Shared utilities and logic for S3 file explorers
 */

(function() {
    'use strict';
    
    // Helper function to generate download URL from key
    function getDownloadUrl(key) {
        const baseUrl = window.location.origin + '/downloads';
        const cleanUrl = baseUrl.endsWith('/') ? baseUrl.slice(0, -1) : baseUrl;
        return cleanUrl + '/' + key;
    }
    
    // Helper function to count files in folder recursively
    function countFilesInFolder(folder) {
        let count = folder.files ? folder.files.length : 0;
        if (folder.children) {
            folder.children.forEach(child => {
                count += countFilesInFolder(child);
            });
        }
        return count;
    }
    
    // Format date to human-readable format
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
    
    // Get icon class for file category
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
    
    // Get color for file category
    function getCategoryColor(category) {
        const colors = {
            'installer': 'primary1',
            'archive': 'info',
            'document': 'link',
            'image': 'danger',
            'video': 'danger',
            'data': 'warning',
            'source': 'grey',
            'other': 'grey-light'
        };
        return colors[category] || colors['other'];
    }
    
    // Sort files based on field and order
    function sortFiles(files, sortField, sortOrder) {
        return [...files].sort((a, b) => {
            let valueA, valueB;
            
            switch (sortField) {
                case 'name':
                    valueA = a.name.toLowerCase();
                    valueB = b.name.toLowerCase();
                    return sortOrder === 'asc' ? 
                        valueA.localeCompare(valueB) : 
                        valueB.localeCompare(valueA);
                case 'size':
                    valueA = a.size || 0;
                    valueB = b.size || 0;
                    return sortOrder === 'asc' ? valueA - valueB : valueB - valueA;
                case 'date':
                    valueA = a.last_modified_timestamp || 0;
                    valueB = b.last_modified_timestamp || 0;
                    return sortOrder === 'asc' ? valueA - valueB : valueB - valueA;
                default:
                    return 0;
            }
        });
    }
    
    // Render file row HTML
    function renderFileRow(file, showPath = false) {
        const icon = getCategoryIcon(file.category);
        const color = getCategoryColor(file.category);
        const downloadUrl = getDownloadUrl(file.key);
        
        let html = `
            <tr style="cursor: pointer;" data-type="file" data-file-key="${file.key}" data-file-name="${file.name}">
                <td>
                    <span class="icon-text">
                        <span class="icon has-text-${color}">
                            <i class="${icon}"></i>
                        </span>
                        <span><a href="${downloadUrl}" class="file-link" title="${downloadUrl}">${file.name}</a></span>
                    </span>`;
        
        if (showPath && file.path) {
            html += `
                    <br>
                    <small class="has-text-grey">${file.path}</small>`;
        }
        
        html += `
                </td>
                <td class="is-hidden-mobile">${file.size_formatted}</td>
                <td class="is-hidden-mobile">${formatDate(file.last_modified)}</td>
            </tr>
        `;
        
        return html;
    }
    
    // Render folder row HTML
    function renderFolderRow(folder, currentPath = []) {
        const fileCount = countFilesInFolder(folder);
        const folderHash = [...currentPath, folder.name].join('/');
        const folderUrl = '#' + folderHash;
        
        return `
            <tr style="cursor: pointer;" data-type="folder" data-folder-name="${folder.name}">
                <td>
                    <span class="icon-text">
                        <span class="icon has-text-primary2">
                            <i class="fas fa-folder"></i>
                        </span>
                        <span><a href="${folderUrl}" class="file-link" title="Navigate to ${folder.name}">${folder.name}</a></span>
                    </span>
                    <br><small class="has-text-grey">${fileCount} item${fileCount !== 1 ? 's' : ''}</small>
                </td>
                <td class="is-hidden-mobile">—</td>
                <td class="is-hidden-mobile">—</td>
            </tr>
        `;
    }
    
    // Search tree recursively
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
    
    // Update sort icons in table headers
    function updateSortIcons(currentSort) {
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
    
    // Export utilities
    window.S3ExplorerCore = {
        getDownloadUrl,
        countFilesInFolder,
        formatDate,
        getCategoryIcon,
        getCategoryColor,
        sortFiles,
        renderFileRow,
        renderFolderRow,
        searchTree,
        updateSortIcons
    };
    
})();
