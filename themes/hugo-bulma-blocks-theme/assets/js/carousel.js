document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.querySelector('.carousel');
    const items = document.querySelectorAll('.carousel-item');
    const prevBtn = document.querySelector('.carousel-nav-prev');
    const nextBtn = document.querySelector('.carousel-nav-next');
    const indicators = document.querySelectorAll('.carousel-indicator');
    
    let currentIndex = 0;
    let intervalId = null;
    const intervalDuration = 5000; // 5 seconds
    
    // Initialize carousel
    function initCarousel() {
        updateCarousel();
        startAutoSlide();
        
        // Event listeners
        prevBtn.addEventListener('click', () => {
            navigate(-1);
            resetAutoSlide();
        });
        
        nextBtn.addEventListener('click', () => {
            navigate(1);
            resetAutoSlide();
        });
        
        // Indicator clicks
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                if (index !== currentIndex) {
                    currentIndex = index;
                    updateCarousel();
                    resetAutoSlide();
                }
            });
        });
    }
    
    // Navigate through items
    function navigate(direction) {
        currentIndex = (currentIndex + direction + items.length) % items.length;
        updateCarousel();
    }
    
    // Update carousel display
    function updateCarousel() {
        // Hide all items
        items.forEach(item => item.classList.remove('is-active'));
        
        // Show current item
        items[currentIndex].classList.add('is-active');
        
        // Update indicators
        indicators.forEach((indicator, index) => {
            if (index === currentIndex) {
                indicator.classList.add('is-active');
            } else {
                indicator.classList.remove('is-active');
            }
        });
    }
    
    // Auto slide functionality
    function startAutoSlide() {
        intervalId = setInterval(() => {
            navigate(1);
        }, intervalDuration);
    }
    
    function resetAutoSlide() {
        clearInterval(intervalId);
        startAutoSlide();
    }
    
    // Initialize
    initCarousel();
});