from flask import Flask
import json
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/flask'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/')
def home():
	return "Hello World!"

def seed_db():
	with open('alerts.json') as f:
		alerts = json.load(f)

	with open('alerts.json') as f:
		alerts = json.load(f)

	pass

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, host='0.0.0.0', debug=True)