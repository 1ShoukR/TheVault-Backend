from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from . import routes
from .models import db

app = Flask(__name__)
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rahmin12@localhost:3306/the_vault'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db(app)
db.init_app(app)

app.add_url_rule('/api', 'index', lambda: 'API for TheVault', strict_slashes=False)
app.register_blueprint(routes.user.bp, url_prefix='/api/users')
app.register_blueprint(routes.create_db.bp, url_prefix='/api/db')



