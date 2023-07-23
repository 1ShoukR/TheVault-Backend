from . import db



class StoredPasswordsAndEmails(db.Model): 
    __tablename__ = 'stored_passwords_and_emails'
    password_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    email_for_password = db.Column(db.String(200), nullable=True)
    username_for_password = db.Column(db.String(200), nullable=True)
    password_for_email = db.Column(db.String(120), nullable=False)
