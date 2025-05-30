function updatePaymentLink() {
    // set href to "Donate" button depending on selected value
    let paymentLink = document
        .getElementById("donate-payrexx")
        .querySelector('input[name="amount"]:checked').value;
    let donateBtn = document.getElementById("payrexx-submit-button");
    donateBtn.href = paymentLink;
}

function updateOptions(freq) {
    // function to toggle set of donate options depending on selected currency
    if (freq != null) {
        document
            .querySelector("#payrexx-donate-frequency-options a.is-active")
            .classList.remove("is-active");
        document
            .querySelector("#payrexx-donate-frequency-options #" + freq)
            .classList.add("is-active");
    }
    let currency = document.getElementById("payrexx-currency").value;
    freq = document.querySelector(
        "#payrexx-donate-frequency-options a.is-active",
    ).id;
    document
        .getElementById("donate-payrexx")
        .querySelectorAll("label")
        .forEach((option) => (option.style.display = "none"));
    let visible = document
        .getElementById("donate-payrexx")
        .querySelectorAll(`[for^="payrexx_${currency}:${freq}:"]`);
    visible.forEach((option) => (option.style.display = "inline-block"));
    // check first visible element
    document.getElementById(visible[0].getAttribute("for")).checked = true;
    updatePaymentLink();
}

let payrexxRadioButtons = document
    .getElementById("donate-payrexx")
    .querySelectorAll('input[name="amount"]');
payrexxRadioButtons.forEach(function (radio) {
    radio.addEventListener("change", updatePaymentLink);
});

updateOptions();
updatePaymentLink();
