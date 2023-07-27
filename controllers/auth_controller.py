from math import ceil
import os
import pathlib
from sqlalchemy import String, or_, func
from flask import redirect, request, jsonify, session, make_response, abort
from app import db
from config import SECRET_KEY
from models import User

import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from controllers.token_validation import token_required
from google_auth_oauthlib.flow import Flow

GOOGLE_CLIENT_ID = "503591789014-6s7h9cg5dc590ht7lecp4buiepotmakf.apps.googleusercontent.com"
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "../client_secret.json")

flow = Flow.from_client_secrets_file(client_secrets_file=client_secrets_file, scopes=[
                                     'https://www.googleapis.com/auth/userinfo.email'], redirect_uri="http://127.0.0.1:5000/api/auth/callback")


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)
        else:
            return function()
    return wrapper


def index():
    # return jsonify({'message': "Authentication API"})
    return "Hello World <a href='login'><button>Login</button></a>"


@token_required
def get_user(current_user):
    return jsonify(current_user.serialize)

# @token_required


def get_all_users():
    # querying the database
    # for all the entries in it

    page = int(request.args.get('page'))
    items_per_page = int(request.args.get('items_per_page'))
    search = request.args.get('search', None)
    sort = request.args.get('sort', None)
    order = request.args.get('order', 'asc')
    if search:
        search = search.lower()
        if sort:
            if order == 'asc':
                users = User.query.filter(
                    or_(
                        func.lower(User.company_name).ilike(f'%{search}%'),
                        func.lower(User.name).ilike(f'%{search}%'),
                        func.lower(User.email).ilike(f'%{search}%'),
                        func.lower(func.cast(User.status, String)
                                   ).ilike(f'%{search}%')
                    )
                ).order_by(getattr(User, sort)).all()
            else:
                users = User.query.filter(
                    or_(
                        func.lower(User.company_name).ilike(f'%{search}%'),
                        func.lower(User.name).ilike(f'%{search}%'),
                        func.lower(User.email).ilike(f'%{search}%'),
                        func.lower(func.cast(User.status, String)
                                   ).ilike(f'%{search}%')
                    )
                ).order_by(getattr(User, sort).desc()).all()
            count = len(users)
            if items_per_page * page > count:
                users = users[(page - 1) * items_per_page:]
            else:
                users = users[(page - 1) *
                              items_per_page: items_per_page * page]
        else:
            users = User.query.filter(
                or_(
                    func.lower(User.company_name).ilike(f'%{search}%'),
                    func.lower(User.name).ilike(f'%{search}%'),
                    func.lower(User.email).ilike(f'%{search}%'),
                    func.lower(func.cast(User.status, String)
                               ).ilike(f'%{search}%')
                )
            ).all()
            count = len(users)
            if items_per_page * page > count:
                users = users[(page - 1) * items_per_page:]
            else:
                users = users[(page - 1) *
                              items_per_page: items_per_page * page]
    else:
        if sort:
            if order == 'asc':
                users = User.query.order_by(getattr(User, sort)).all()
            else:
                users = User.query.order_by(getattr(User, sort).desc()).all()
            count = len(users)
            if items_per_page * page > count:
                users = users[(page - 1) * items_per_page:]
            else:
                users = users[(page - 1) *
                              items_per_page: items_per_page * page]
        else:
            users = User.query.paginate(
                page=int(page), per_page=int(items_per_page))
            count = users.total
    page_count = ceil(count / items_per_page)
    # converting the query objects
    # to list of jsons
    prev_page = page - 1
    prev_url = f"/?page={prev_page}"
    if prev_page == 0:
        prev_page = None
        prev_url = None
    links = [
        {
            "url": prev_url,
            "page": prev_page,
            "label": "&laquo; Previous",
            "activate": False
        }
    ]
    for i in range(1, page_count + 1):
        links.append({
            "url": f"page={i}",
            "page": i,
            "label": f"{i}",
            "activate": False
        })
    next_page = page + 1
    next_url = f"/?page={next_page}"
    if next_page == page_count + 1:
        next_page = None
        next_url = None
    links.append({
        "url": next_url,
        "page": next_page,
        "label": "Next &raquo;",
        "activate": False
    })
    from_page = (page - 1) * items_per_page + 1
    to_page = from_page + items_per_page
    if to_page > count:
        to_page = count
    pagination = {
        "first_page_url": "/?page=1",
        "from": from_page,
        "to": to_page,
        "items_per_page": str(items_per_page),
        "last_page": page_count,
        "prev_page_url": prev_url,
        "next_page_url": next_url,
        "page": page,
        "prev_page_url": prev_url,
        "total": count,
        "links": links,
        "total": count
    }
    data = []
    for user in users:
        # appending the user data json
        # to the response list
        data.append(user.serialize)

    return jsonify({
        'data': data,
        'payload': {
            "pagination": pagination
        }
    })


def login():
    # authorization_url, state = flow.authorization_url()
    # session['state'] = state
    # return redirect(authorization_url)

    # creates dictionary of form data
    auth = request.get_json()

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

    user = User.query\
        .filter_by(email=auth.get('email'))\
        .first()

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'public_id': user.public_id
        }, SECRET_KEY)
        # session['user'] = token
        return make_response(jsonify({'api_token': token}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
    )


def signup():
    # creates a dictionary of the form data
    data = request.get_json()

    # gets name, email and password
    name, email, company_name = data.get('name'), data.get(
        'email'), data.get('company_name')
    password = data.get('password')

    # checking for existing user
    user = User.query\
        .filter_by(email=email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            public_id=str(uuid.uuid4()),
            company_name=company_name,
            name=name,
            email=email,
            password=generate_password_hash(password)
        )
        # insert user
        db.session.add(user)
        db.session.commit()
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, SECRET_KEY)
        # return make_response('Successfully registered.', 201)
        return make_response(jsonify({'api_token': token}), 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)

# @token_required


def logout():
    session.clear()
    return redirect("/api/auth")


def callback():
    pass


@login_is_required
def protected_area():
    return "protectec_area <a href='logout'><button>Logout</button></a>"
