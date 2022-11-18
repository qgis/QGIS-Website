const qgis_observer = new IntersectionObserver((entries) => {
    console.log("Animation observer");
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('animation-show');
            entry.target.classList.remove('animation-hide');
        } else {
            entry.target.classList.add('animation-hide');
            entry.target.classList.remove('animation-show');
        }
    })
});
const animationElements = document.querySelectorAll('.animation-hide');
animationElements.forEach((element) => qgis_observer.observe(element));