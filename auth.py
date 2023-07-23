import jwt
import typing as t
from functools import wraps
from flask import request, jsonify, current_app, g
from datetime import datetime
import inspect


def create_api_token(user_id: t.Optional[int] = None):
    token_dict = dict()
    if user_id is not None:
        token_dict['user_id'] = user_id
    return jwt.encode(token_dict, current_app.config['API_JWT_SECRET'], algorithm="HS256")


def decode_api_token(token):
    try:
        api_jwt_secret = current_app.config.get('API_JWT_SECRET')
        if api_jwt_secret is None:
            raise RuntimeError("API_JWT_SECRET is not set. Please set it before using this function.")
            
        return jwt.decode(token, api_jwt_secret, algorithms=["HS256"])
    
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError("API token has expired!!")
        
    except jwt.InvalidTokenError as e:
        raise jwt.InvalidTokenError("Invalid API token: " + str(e))
        
    except Exception as e:
        raise Exception("Something went wrong with the API token: " + str(e))



def check_jwt_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'message': 'Bearer token is missing!!'}), 401

        token = auth_header.replace('Bearer ', '')

        try:
            # Verify and decode the API token using the decode_api_token function
            decoded_token = decode_api_token(token)
            user_id = decoded_token.get('user_id')

            if user_id is None:
                raise jwt.InvalidTokenError("Invalid token payload: Missing 'user_id'.")

            if 'user_id' in inspect.signature(f).parameters:
                # Pass the user_id as an argument to the decorated function
                return f(user_id, *args, **kwargs)
            else:
                # Call the decorated function without the user_id argument
                return f(*args, **kwargs)

        except jwt.ExpiredSignatureError as e:
            return jsonify({'message': str(e)}), 401

        except jwt.InvalidTokenError as e:
            return jsonify({'message': str(e)}), 401

        except Exception as e:
            return jsonify({'message': str(e)}), 401

    return decorated