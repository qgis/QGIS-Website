function updatePaymentLink() {
  // set href to "Donate" button depending on selected value
  let paymentLink = document.getElementById('donate-stripe').querySelector('input[name="amount"]:checked').value;
  let donateBtn = document.getElementById('submit-button');
  donateBtn.href = paymentLink;
};

function updateOptions(freq) {
  // function to toggle set of donate options depending on selected currency
  if (freq != null) {
    document.querySelector('#donate-frequency-options a.is-active').classList.remove("is-active");
    document.querySelector('#donate-frequency-options #' + freq).classList.add("is-active");
  }
  let currency = document.getElementById('currency').value;
  freq = document.querySelector('#donate-frequency-options a.is-active').id;
  document.getElementById('donate-stripe')
    .querySelectorAll('label')
    .forEach(option => option.style.display = "none");
  let visible = document.getElementById('donate-stripe')
    .querySelectorAll(`[for^="${currency}:${freq}:"]`);
  visible.forEach(option => option.style.display = "inline-block");
  // check first visible element
  document.getElementById(visible[0].getAttribute('for')).checked = true;
}

let radioButtons = document.getElementById('donate-stripe').querySelectorAll('input[name="amount"]');
radioButtons.forEach(function(radio) {
  radio.addEventListener('change', updatePaymentLink);
});

updateOptions();
updatePaymentLink();
