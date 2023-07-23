from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import your models here to control the creation order
from . import (
    user,
    stored_passwords
)
