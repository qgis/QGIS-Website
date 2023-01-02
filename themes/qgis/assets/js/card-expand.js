document.addEventListener('DOMContentLoaded', function () {
    let cardToggles = document.getElementsByClassName('pulldown-content');
    for (let i = 0; i < cardToggles.length; i++) {
        cardToggles[i].addEventListener('click', e => {
            console.log("Card expander clicked");
            e.currentTarget.parentElement.parentElement.parentElement.parentElement.getElementsByClassName("content")[0].classList.toggle('is-hidden');
        });
    }
});