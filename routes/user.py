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

    # Generate a random salt
    salt = bcrypt.gensalt()

    # Hash the password using the generated salt
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)

    found_user = models.user.User.query.filter(
        (models.user.User.username == username) | (models.user.User.email == email)
    ).first()

    if found_user:
        if found_user.username == username:
            raise UserAlreadyExistsError('username', username)
        elif found_user.email == email:
            raise UserAlreadyExistsError('email', email)

    try:
        create_user = models.user.User(
            username=username,
            password=hashed_pass,
            email=email,
        )

        create_person = models.user.Person(
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            address=request.form.get('address'),
            user=create_user 
        )

        db.session.add(create_user)
        db.session.add(create_person)
        db.session.commit()
        return jsonify(status=200, message='User created successfully')
    except Exception as e:
        raise UserCreationError(str(e))

@bp.route('/login', methods=["POST"])
def login():
    g.user = None
    g.token = None
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Find the user by username or email
    found_user = models.user.User.query.filter(
        ((models.user.User.username == username) | (models.user.User.email == email))
    ).first()

    if found_user and bcrypt.checkpw(password.encode('utf-8'), found_user.password.encode('utf-8')):
        # Passwords match, generate and store the token in g.token
        token = create_api_token(found_user.user_id)
        g.user = found_user
        g.token = token
        return jsonify(status=200, token=token, message=f'Welcome {found_user.username}')
    else:
        # User not found or password does not match
        return jsonify(status=401, message='Invalid credentials')


@bp.route('/test-decorator')
@check_jwt_token
def test():
    return 'work'