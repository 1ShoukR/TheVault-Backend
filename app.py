import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
import routes
import os
import configparser
from models.stored_passwords import StoredPasswords

config = configparser.ConfigParser()
config.read('config/config.cfg')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('DEFAULT', 'SQLALCHEMY_DATABASE_URI')
app.config['DEBUG'] = config.getboolean('DEFAULT', 'DEBUG')

# Initialize the database for the User and StoredPasswords models
db.init_app(app)

print(db)

# Register your blueprints
app.register_blueprint(routes.user.bp, url_prefix='/api/users')
app.register_blueprint(routes.create_db.bp, url_prefix='/api/db')

# Ensure the table is created before serving the app
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'api index'

if __name__ == "__main__":
    app.run(port=os.environ.get('FLASK_RUN_PORT'), debug=True)
