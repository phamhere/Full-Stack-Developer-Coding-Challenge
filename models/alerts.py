from db import db

class AlertsModel(db.Model):
	__tablename__ = 'alerts'

	id = db.Column(db.Integer, primary_key=True)
	errorId = db.Column(db.String(80))
	errorSeverity = db.Column(db.String(80))
	errorCategory = db.Column(db.String(80))
	errorMessage = db.Column(db.String(80))
	longMessage = db.Column(db.String(200))
	errorTime = db.Column(db.Integer)
	selected = db.Column(db.Boolean())
	new = db.Column(db.Boolean())
	expanded = db.Column(db.Boolean())