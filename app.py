from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/postgres'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://jdlgiettktpknc:f7a0ebfa34ce869bdb6ac7588ebd2e72a1cb48110132cbca914c4cf04996aa8c@ec2-54-235-103-219.compute-1.amazonaws.com:5432/d2dcs919qvqv22'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, host='0.0.0.0', debug=True)