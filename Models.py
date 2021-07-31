import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)


class Puppy(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.INTEGER)
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        if self.owner:
            return f"The name of the puppy is {self.name}. His age is {self.age}. The owner name is {self.owner.name}"
        else:
            return f"The name of the puppy is {self.name}. His age is {self.age}. He has no owner :)"

    def send_toys(self):
        for toy in self.toys:
            return f"The puppy {self.name} has a toy name {toy.item_name}"


class Owner(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.INTEGER, db.ForeignKey('puppy.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id


class Toy(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.INTEGER, db.ForeignKey('puppy.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id
