from . import db

class Person(db.Model):
    __tablename__ = 'person'
    person_id:int = db.Column(db.Integer, primary_key=True)
    first_name:str = db.Column(db.String(120), unique=False, nullable=False)
    last_name:str = db.Column(db.String(120), unique=False, nullable=False)
    address:str = db.Column(db.String(120), unique=False, nullable=True)
    # Define the one-to-one relationship with User
    user_id:int = db.Column(db.Integer, db.ForeignKey('user.user_id'), unique=True, nullable=True)
    user = db.relationship('User', backref='person', uselist=False)



class User(db.Model):
    __tablename__ = 'user'
    user_id:int = db.Column(db.Integer, primary_key=True)
    username:str = db.Column(db.String(80), unique=True, nullable=False)
    password:str = db.Column(db.String(120), nullable=False)
    email:str = db.Column(db.String(200), unique=True, nullable=False)
    stored_passwords = db.relationship('StoredPasswordsAndEmails', backref='user', lazy=True)
