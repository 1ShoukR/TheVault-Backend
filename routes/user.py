from flask import Blueprint, request
from models import db
import models
from utils.errorhandling import UserAlreadyExistsError, UserCreationError



bp = Blueprint('user', __name__)

@bp.route('/get-user')
def get_user():
    return 'get user'


@bp.route('/create', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    
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
            password=request.form.get('password'),
            email=email
        )
        db.session.add(create_user)
        db.session.commit()
        return 'done'
    except Exception as e:\
        raise UserCreationError(str(e))