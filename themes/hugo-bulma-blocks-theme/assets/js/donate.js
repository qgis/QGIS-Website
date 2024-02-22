function updatePaymentLink() {
  // set href to "Donate" button depending on selected value
  let paymentLink = document.getElementById('donate-stripe').querySelector('input[name="amount"]:checked').value;
  let donateBtn = document.getElementById('submit-button');
  donateBtn.href = "https://donate.stripe.com/" + paymentLink;
};

function updateCurrency() {
  // function to toggle set of donate options depending on selected currency
  let toShow = document.getElementById('currency').value;
  let toHide = toShow == 'usd' ? 'eur' : 'usd';
  document.getElementById('donate-stripe')
    .querySelectorAll(`[for^="${toHide}:"]`)
    .forEach(option => option.style.display = "none");
  let visible = document.getElementById('donate-stripe')
    .querySelectorAll(`[for^="${toShow}:"]`);
  visible.forEach(option => option.style.display = "inline-block");
  // check first visible element
  document.getElementById(visible[0].getAttribute('for')).checked = true;
}

let radioButtons = document.getElementById('donate-stripe').querySelectorAll('input[name="amount"]');
radioButtons.forEach(function(radio) {
  radio.addEventListener('change', updatePaymentLink);
});

updateCurrency();
updatePaymentLink();
