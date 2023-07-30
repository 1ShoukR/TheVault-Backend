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
    print('request',request.json)
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

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
            first_name=request.json['firstname'],
            last_name=request.json['lastname'],
            user=create_user 
        )
        token = create_api_token(user_id=create_user.user_id)
        print(token)

        # db.session.add(create_user)
        # db.session.add(create_person)
        # db.session.commit()
        return jsonify(status=200, message='User created successfully', token=token, first_name=create_person.first_name, last_name=create_person.last_name)
    except Exception as e:
        raise UserCreationError(str(e))



@bp.route('/test-decorator')
@check_jwt_token
def test():
    return 'work'