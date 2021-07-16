import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.INTEGER)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy name is {self.name}. His age is around {self.age}"
