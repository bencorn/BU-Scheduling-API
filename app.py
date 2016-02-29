# File name: app.py
# Author: Benjamin Corn
# Date created: 2/20/2016
# Date last modified: 2/25/2016
# Python Version: 3.0

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

# Starting new Flask app
app = Flask(__name__)

# Starting new sqlite database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///classdata.db'
db = SQLAlchemy(app)


# RESTful API database model class
class Class(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	classnum = db.Column(db.Text)
	classname = db.Column(db.Text)
	professor = db.Column(db.Text)
	classtype = db.Column(db.Text)
	seats = db.Column(db.INT)
	bldgcode = db.Column(db.Text)
	roomcode = db.Column(db.Text)
	classdays = db.Column(db.Text)
	starttime = db.Column(db.Text)
	endtime = db.Column(db.Text)

# Push all structures to database
db.create_all()

# Creating APIManager from restless extension
manager = APIManager(app, flask_sqlalchemy_db=db)

# Defining valid HTML requests
class_blueprint = manager.create_api(Class, methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])

# Running Flask loop sequence
if __name__ == "__main__":
	app.run()
