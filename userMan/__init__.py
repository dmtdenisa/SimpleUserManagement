from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
import datetime



app=Flask(__name__)
#URI - unity resource identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userData.db'
db= SQLAlchemy(app)
app.config['SECRET_KEY']='02161e53583a86c2649e93b4'
from userMan import routes