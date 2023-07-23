from flask import Blueprint, request
from models import db
from models.user import User


bp = Blueprint('user', __name__)

@bp.route('/get-user')
def get_user():
    return 'get user'



@bp.route('/create', methods=['POST'])
def create():
    print('hello')
    create_user = User(
        username=request.form.get('username'),
        password = request.form.get('password'),
        email = request.form.get('email')
    )
    print('this is user', create_user)
    return 'done'

