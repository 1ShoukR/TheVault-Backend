from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db
import os
import routes
import configparser

config = configparser.ConfigParser()
config.read('config/config.cfg')


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DEFAULT', 'SQLALCHEMY_DATABASE_URI')
app.config['DEBUG'] = config.getboolean('DEFAULT', 'DEBUG')
app.config['SECRET_KEY'] = config.get('DEFAULT', 'SECRET_KEY')
app.config['API_JWT_SECRET'] = ''

# Initialize the database for the User and StoredPasswords models
db.init_app(app)


# Register your blueprints
app.register_blueprint(routes.user.bp, url_prefix='/api/users')
app.register_blueprint(routes.auth.bp, url_prefix='/api/auth')

# Ensure the table is created before serving the app
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'api index'

if __name__ == "__main__":
    app.run(port=os.environ.get('FLASK_RUN_PORT'), debug=True)
