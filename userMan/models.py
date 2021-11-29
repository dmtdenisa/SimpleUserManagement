from userMan import db

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    firstName = db.Column(db.String(length=20), nullable=False, unique=False)
    lastName = db.Column(db.String(length=20), nullable=False, unique=False)
    email = db.Column(db.String(length=40), nullable=False, unique=False)
    password = db.Column(db.String(length=60), nullable=False, unique=False)
