from sqlalchemy import and_, cast, or_, orm
from flask import Flask
import sqlalchemy as sa
import typing as t
from models import db
from flask_sqlalchemy import SQLAlchemy







class User(db.Model):
    __tablename__ = 'user'
    user_id:int = sa.Column(sa.Integer, primary_key=True)
    username:str = sa.Column(sa.String, unique=True)
    password:str = sa.Column(sa.String)
    email:str = sa.Column(sa.String, unique=True)
