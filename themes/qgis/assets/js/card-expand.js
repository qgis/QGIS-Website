document.addEventListener('DOMContentLoaded', function () {
    let cardToggles = document.getElementsByClassName('pulldown-toggle');
    for (let i = 0; i < cardToggles.length; i++) {
        cardToggles[i].addEventListener('click', e => {
            console.log("Card expander clicked");
            getElementsById(e.currentTarget.data-content-block-id).classList.toggle('is-hidden');
        });
    }
});