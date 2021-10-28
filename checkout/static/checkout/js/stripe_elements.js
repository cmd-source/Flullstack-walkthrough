/* Javascript needed to create a card payment method for the checkout page */

var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var stripe_secret_key = $('#id_stripe_secret_key').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = { 
    base: {
      color: '#000',
      fontWeight: '500',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      '::placeholder': {
        color: '#aab7c4',
      },
    },
    invalid: {
      iconColor: '#dc3545',
      color: '#dc3545',
    },
  };

var card = elements.create('card', {style: style});

card.mount('#card-element');