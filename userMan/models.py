from userMan import db
import datetime
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
"""


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    firstName = db.Column(db.String(length=20), nullable=False, unique=False)
    lastName = db.Column(db.String(length=20), nullable=False, unique=False)
    email = db.Column(db.String(length=40), nullable=False, unique=False)
    password = db.Column(db.String(length=60), nullable=False, unique=False)
    created_at= db.Column(db.DateTime, default=datetime.datetime.utcnow) #default tells the constructor to generate timestamp at the time of insertion
    updated_at=db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    
    #method to give the model a readable string representation (used for debugging and testing)
    def __repr__(self):
        return '<User %r>' % self.username
    
#from userMan.models import db
#db.drop_all() - drops everything
#db.create_all()
#from userMan.models import User
#u1 = User(username='', ...)
#db.session.add(u1)
#db.session.commit()