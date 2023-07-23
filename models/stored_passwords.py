from . import db



class StoredPasswords(db.Model): 
    __tablename__ = 'stored_passwords'
    password_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    website_for_password = db.Column(db.String(200), nullable=False)
    email_for_password = db.Column(db.String(200), nullable=True)
    username_for_password = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(120), nullable=False)
