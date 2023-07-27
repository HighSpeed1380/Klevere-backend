from flask import Blueprint

from controllers.auth_controller import *

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/',  methods =['GET', 'POST'])(index)
auth_bp.route('/login',  methods =['GET', 'POST'])(login)
auth_bp.route('/signup',  methods =['POST'])(signup)
auth_bp.route('/user_all',  methods =['GET'])(get_all_users)
auth_bp.route('/verify_token',  methods =['POST'])(get_user)
auth_bp.route('/logout',  methods =['GET', 'POST'])(logout)
auth_bp.route('/callback',  methods =['GET', 'POST'])(callback)
auth_bp.route('/protected_area',  methods =['GET', 'POST'])(protected_area)