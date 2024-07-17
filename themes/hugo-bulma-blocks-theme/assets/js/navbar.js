// first handler for hide / show of search box when magnifying glass is clicked
document.addEventListener("DOMContentLoaded", () => {
    const $toggles = Array.prototype.slice.call(
        document.querySelectorAll(".search-icon"),
        0,
    );

    $toggles.forEach((el) => {
        el.addEventListener("click", () => {
            console.log("Search icon clicked");
            // Get the target from the "data-target" attribute
            const $target = document.getElementById("search-control");
            // Toggle the search control
            el.classList.toggle("is-hidden");
            $target.classList.toggle("is-hidden");
        });
    });
});

document.addEventListener("DOMContentLoaded", () => {
    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(
        document.querySelectorAll(".navbar-burger"),
        0,
    );

    // Add a click event on each of them
    $navbarBurgers.forEach((el) => {
        el.addEventListener("click", () => {
            // Get the target from the "data-target" attribute
            const target = el.dataset.target;
            const $target = document.getElementById(target);

            // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
            el.classList.toggle("is-active");
            $target.classList.toggle("is-active");
        });
    });
});

var prevScrollpos = window.scrollY;
var isTyping = false;

// Get the input element
var searchInput = document.getElementById("search-query");

// Add focus and blur event listeners to the input
searchInput.addEventListener("focus", function() {
    isTyping = true;
});

searchInput.addEventListener("blur", function() {
    isTyping = false;
});

window.onscroll = function () {
    var currentScrollPos = window.scrollY;

    if (prevScrollpos > currentScrollPos || isTyping) {
        // Show the news&search bar
        document.getElementById("context").style.top = "4rem";
    } else {
        // Hide the news&search bar
        document.getElementById("context").style.top = "-2em";
    }
    prevScrollpos = currentScrollPos;
};
