var spoilerLabels = document.querySelectorAll('.spoiler-label');
spoilerLabels.forEach(function(label) {
    label.addEventListener('click', function() {
        var content = this.parentElement.querySelector('.content');
        content.classList.toggle('active');
    });
});
