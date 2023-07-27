import stripe
from flask import jsonify, request, render_template
import config

stripe_keys = {
  'secret_key': config.STRIPE_SECRET_KEY,
  'publishable_key': config.STRIPE_PUBLISHABLE_KEY
}

stripe.api_key = stripe_keys['secret_key']


# @app.route('/')
def index():
    return render_template('index.html',key=stripe_keys['publishable_key'])

# @app.route('/checkout', methods=['POST'])
def checkout():

    amount = 500

    customer = stripe.Customer.create(
        email='sample@customer.com',
        source=request.form['stripeToken']
    )

    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('checkout.html', amount=amount)