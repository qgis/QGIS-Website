let stripe = null;
let stripeBaseUrl = 'https://192.168.1.8:1313/stripe';
//let stripeBaseUrl = 'https://qgis.org/stripe';
let stripeKeyUrl =  stripeBaseUrl + '/stripe-key';
let recaptchaKeyUrl =  stripeBaseUrl + '/recaptcha-key';
let stripeCheckoutUrl = stripeBaseUrl + '/create-checkout-session';

let recaptchaToken = null;

(function () {
  setTimeout(function () {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const success = urlParams.get('payment_success')
    if (success && success === 'True') {
      window.history.pushState("object or string", "Title", '{{- "{{ donation_url }}" -}}');
      document.getElementById('thankyou').style.display = 'block';
    }
  }, 500)

  /*
  // Render recaptcha
  fetch(recaptchaKeyUrl).then(response => response.json()).then(
    json => {
      const key = json['key'];
tTimeout(function () {
      grecaptcha.render('recaptcha-container', {
'jsUrl': 'https://www.google.com/recaptcha/api.js?render=explicit',
        'sitekey': key,
        'callback': 'enableSubmitBtn'
      });
 1000);
    }
  )
  */
  
  // Initialize Stripe
  fetch(stripeKeyUrl).then(function (response) {
    return response.json();
  }).then(function(json) {
    const key = json['key'];
    if (key.includes("test")) {
      $('.testText').show();
    }
    stripe = Stripe(key);
    let elements = stripe.elements();
  })
})();

let checkoutButton = document.getElementById('submit-button');

checkoutButton.addEventListener('click', function () {
  //if (!isCaptchaChecked) {
  //  return;
  //}
  let donationValue = document.getElementById('donate-stripe').querySelector('input[name="amount"]:checked').value.split(':');
  let donationCurrency = donationValue[0];
  let donationAmount = donationValue[1];
  const postData = {
    donationCurrency: donationCurrency,
    donationAmount: donationAmount,
  //  recaptchaToken: recaptchaToken
  }

  alert('aaaaaaaaa');
  fetch(stripeCheckoutUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(postData)
  })
    .then(function (response) {
      console.log(response);
      if (response.ok) {
        return response.json();
      } else {
        document.getElementById('stripeErrorMessage').style.display = 'block';
        document.getElementById('stripeErrorMessage').innerHTML = response.statusText;
      }
    })
    .then(function (session) {
      console.log(session);
      return stripe.redirectToCheckout({ sessionId: session.id });
    })
    .then(function (result) {
      console.log(result);
      // If `redirectToCheckout` fails due to a browser or network
      // error, you should display the localized error message to your
      // customer using `error.message`.
      if (result.error) {
        document.getElementById('stripeErrorMessage').style.display = 'block';
        document.getElementById('stripeErrorMessage').innerHTML = result.error.message;
      }
    })
    .catch(function (error) {
      console.log(error);
    });
});

/*
function enableSubmitBtn(response) {
  document.getElementById("submit-button").disabled = false;
  recaptchaToken = response;
}

function isCaptchaChecked() {
  return grecaptcha && grecaptcha.getResponse().length !== 0 && recaptchaToken;
}
*/

function updateCurrency() {
  let toShow = document.getElementById('currency').value;
  let toHide = toShow == 'usd' ? 'eur' : 'usd';
  document.getElementById('donate-stripe')
    .querySelectorAll(`[for^="${toHide}:"]`)
    .forEach(option => option.style.display = "none");
  document.getElementById('donate-stripe')
    .querySelectorAll(`[for^="${toShow}:"]`)
    .forEach(option => option.style.display = "inline-block");
}

updateCurrency();
