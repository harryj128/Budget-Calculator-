from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bud-cal-db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'eiwnonwvoiwnvworbn'

db = SQLAlchemy(app)

import application.routes


#getenv('DATABASE_URI')