from flask import Blueprint

from controllers.stripe import *

stripe_test = Blueprint('stripe_test', __name__)

stripe_test.route('/',  methods =['GET', 'POST'])(index)
stripe_test.route('/checkout',  methods =['POST'])(checkout)