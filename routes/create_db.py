from flask import Blueprint
from ..models import db



bp = Blueprint('create_db', __name__)


@bp.route('/create')
def get_user():
    db.create_all()
    return 'db created'