const qgis_observer = new IntersectionObserver((entries) => {
    console.log("Animation observer");
    entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
            entry.target.classList.add('animated-show');
        } else {
            entry.target.classList.add('animated-hidden');
        }
    })
});
const animationElements = document.querySelectorAll('.animated-hidden');
animationElements.forEach((element) => qgis_observer.observe(element));