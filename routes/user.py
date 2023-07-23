from flask import Blueprint, request, jsonify, g
from models import db
from utils.errorhandling import UserAlreadyExistsError, UserCreationError
from auth import create_api_token, check_jwt_token
import models
import bcrypt



bp = Blueprint('user', __name__)

@bp.route('/get-user')
def get_user():
    return 'get user'


@bp.route('/create', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    password_encoded = password.encode('utf-8')
    
    found_user = models.user.User.query.filter(
        (models.user.User.username == username) | (models.user.User.email == email)
    ).first()
    
    if found_user:
        if found_user.username == username:
            raise UserAlreadyExistsError('username', username)
        elif found_user.email == email:
            raise UserAlreadyExistsError('email', email)
        
    try:
        hashed_pass = bcrypt.hashpw(password_encoded, bcrypt.gensalt())
        print('hashed_pass', hashed_pass)
        create_user = models.user.User(
            username=username,
            password=password_encoded,
            email=email
        )
        db.session.add(create_user)
        db.session.commit()
        return jsonify(status=200, message='User created successfully')
    except Exception as e:\
        raise UserCreationError(str(e))


@bp.route('/login', methods=["POST"])
def login():
    g.user = None
    g.token = None
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    found_user = models.user.User.query.filter(
        ((models.user.User.username == username) | (models.user.User.email == email)) &
        (models.user.User.password == password)
    ).first()
    token = create_api_token(found_user.user_id)
    g.user = found_user
    g.token = token
    return jsonify(status=200, token=token, message=f'Welcome {found_user.username}')


@bp.route('/test-decorator')
@check_jwt_token
def test():
    return 'work'