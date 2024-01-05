document.addEventListener('DOMContentLoaded', () => {
    // Get all "navbar-burger" elements
    const $toggles = Array.prototype.slice.call(
        document.querySelectorAll('.pulldown-toggle'), 0);

    // Add a click event on each of them
    $toggles.forEach( el => {
        el.addEventListener('click', () => {
            console.log("Card expander clicked");
            // Get the target from the "data-contentid" attribute
            const target = el.dataset.contentid;
            const $target = document.getElementById(target);
            $target.classList.toggle("is-hidden");
            let child = el.firstChild.nextElementSibling.childNodes[1];
            const $child = document.getElementById(child);
            if (child.classList.contains("fa-angle-down"))
            {
                child.classList.remove("fa-angle-down");
                child.classList.add("fa-angle-up");
            }
            else
            {
                child.classList.remove("fa-angle-up");
                child.classList.add("fa-angle-down");
            }            
        })
    })
}); 