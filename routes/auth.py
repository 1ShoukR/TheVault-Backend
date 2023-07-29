from flask import Blueprint, request, jsonify, g
from models import db
from utils.errorhandling import UserAlreadyExistsError, UserCreationError
from auth import create_api_token, check_jwt_token
import models
import bcrypt
import typing as t
import json



bp = Blueprint('auth', __name__)



@bp.route('/login', methods=["POST"])
def login() -> t.Dict[int, t.Any]:
    from flask import request

    print(request.json)
    g.user = None
    g.token = None

    # Assuming that request.json is a dictionary
    data: t.Dict[str] = json.loads(request.json)
    username_or_email: str = data['email']
    password: str = data['password']

    print('username_or_email', username_or_email)
    print('password', password)

    # Uncomment this when you are ready to implement
    # found_user = models.user.User.query.filter(
    #     ((models.user.User.username == username_or_email) | (models.user.User.email == username_or_email))).first()

    # if found_user and bcrypt.checkpw(password.encode('utf-8'), found_user.password.encode('utf-8')):
    #     token = create_api_token(found_user.user_id)
    #     g.user = found_user
    #     g.token = token
    #     return jsonify(status=200, token=token, message=f'Welcome {found_user.username}')

    return jsonify(status=401, message='Invalid credentials')
