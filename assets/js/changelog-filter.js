// Count and filter visual changelog features by level two category.
// Loaded by the changelog-filter shortcode; categories come from changelog-category-start.

function changelogCategoryName(category) {
    const heading = category.querySelector('h2');
    if (!heading) return category.id;
    const label = heading.cloneNode(true);
    label.querySelectorAll('.heading-anchor').forEach((anchor) => anchor.remove());
    return label.textContent.trim();
}

function changelogFilterOption(name, count) {
    const option = document.createElement('label');
    option.className = 'dropdown-item changelog-filter-option is-flex is-align-items-center';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    const label = document.createElement('span');
    label.textContent = name;
    const badge = document.createElement('span');
    badge.className = 'tag is-rounded ml-auto';
    badge.textContent = count;
    option.append(checkbox, label, badge);
    return option;
}

function initChangelogFilter() {
    const panel = document.querySelector('.changelog-filter');
    const categories = Array.from(document.querySelectorAll('.changelog-category'));
    if (!panel || categories.length === 0) return;

    const dropdown = panel.querySelector('.dropdown');
    const trigger = panel.querySelector('.dropdown-trigger .button');
    const menu = panel.querySelector('.dropdown-content');
    const selectedCount = panel.querySelector('.changelog-filter-selected');
    const resetButton = panel.querySelector('.changelog-filter-reset');
    const showingCount = panel.querySelector('.changelog-filter-showing');
    const totalCount = panel.querySelector('.changelog-filter-total');
    const featureCounts = new Map(
        categories.map((category) => [category.id, category.querySelectorAll('h3').length])
    );
    const params = new URLSearchParams(window.location.search);
    const active = new Set(
        (params.get('filters') || '').split(',').filter((id) => featureCounts.has(id))
    );

    const checkboxes = categories.map((category) => {
        const option = changelogFilterOption(changelogCategoryName(category), featureCounts.get(category.id));
        const checkbox = option.querySelector('input');
        checkbox.addEventListener('change', () => {
            if (checkbox.checked) {
                active.add(category.id);
            } else {
                active.delete(category.id);
            }
            update();
        });
        menu.append(option);
        return checkbox;
    });

    function setOpen(open) {
        dropdown.classList.toggle('is-active', open);
        trigger.setAttribute('aria-expanded', String(open));
    }

    function update() {
        let showing = 0;
        categories.forEach((category, index) => {
            const selected = active.has(category.id);
            const visible = active.size === 0 || selected;
            category.hidden = !visible;
            if (visible) showing += featureCounts.get(category.id);
            checkboxes[index].checked = selected;
        });
        showingCount.textContent = showing;
        selectedCount.textContent = active.size;
        selectedCount.classList.toggle('is-hidden', active.size === 0);
        resetButton.disabled = active.size === 0;

        if (active.size > 0) {
            params.set('filters', Array.from(active).join(','));
        } else {
            params.delete('filters');
        }
        const query = params.toString();
        const url = `${window.location.pathname}${query ? `?${query}` : ''}${window.location.hash}`;
        window.history.replaceState(null, '', url);
    }

    trigger.addEventListener('click', () => setOpen(!dropdown.classList.contains('is-active')));
    document.addEventListener('click', (event) => {
        if (!dropdown.contains(event.target)) setOpen(false);
    });
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && dropdown.classList.contains('is-active')) {
            setOpen(false);
            trigger.focus();
        }
    });
    resetButton.addEventListener('click', () => {
        active.clear();
        update();
    });

    totalCount.textContent = Array.from(featureCounts.values()).reduce((sum, count) => sum + count, 0);
    update();
    panel.classList.remove('is-hidden');
}

initChangelogFilter();
