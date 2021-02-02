from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jdlgiettktpknc:f7a0ebfa34ce869bdb6ac7588ebd2e72a1cb48110132cbca914c4cf04996aa8c@ec2-54-235-103-219.compute-1.amazonaws.com:5432/d2dcs919qvqv22'

db = SQLAlchemy(app)