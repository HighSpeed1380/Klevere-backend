# pseudo code
from flask import request, jsonify
from config import SECRET_KEY
from models import User

import json
import jwt
from functools import wraps

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        # if 'x-access-token' in request.headers:
        #     token = request.headers['x-access-token']
        # return 401 if token is not passed
        data = json.loads(request.data)
        # jwt is passed in the request data
        if 'api_token' in data:
            token = data['api_token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = User.query.filter_by(public_id = data['public_id']).first()
        except Exception as err:
            print(err)
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated