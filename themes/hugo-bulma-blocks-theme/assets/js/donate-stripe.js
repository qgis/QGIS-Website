function updateStripePaymentLink() {
    // set href to "Donate" button depending on selected value
    let paymentLink = document
        .getElementById("donate-stripe")
        .querySelector('input[name="amount"]:checked').value;
    let donateBtn = document.getElementById("stripe-submit-button");
    donateBtn.href = paymentLink;
}

function updateStripeOptions(freq) {
    // function to toggle set of donate options depending on selected currency
    if (freq != null) {
        document
            .querySelector("#stripe-donate-frequency-options a.is-active")
            .classList.remove("is-active");
        document
            .querySelector("#stripe-donate-frequency-options #" + freq)
            .classList.add("is-active");
    }
    let currency = document.getElementById("stripe-currency").value;
    freq = document.querySelector(
        "#stripe-donate-frequency-options a.is-active",
    ).id;
    document
        .getElementById("donate-stripe")
        .querySelectorAll("label")
        .forEach((option) => (option.style.display = "none"));
    let visible = document
        .getElementById("donate-stripe")
        .querySelectorAll(`[for^="stripe_${currency}:${freq}:"]`);
    visible.forEach((option) => (option.style.display = "inline-block"));
    // check first visible element
    document.getElementById(visible[0].getAttribute("for")).checked = true;
    updateStripePaymentLink();
}

let stripeRadioButtons = document
    .getElementById("donate-stripe")
    .querySelectorAll('input[name="amount"]');
stripeRadioButtons.forEach(function (radio) {
    radio.addEventListener("change", updateStripePaymentLink);
});

updateStripeOptions();
updateStripePaymentLink();
