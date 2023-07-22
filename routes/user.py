from flask import Blueprint


bp = Blueprint('user', __name__)

@bp.route('/get-user')
def get_user():
    return 'get user'