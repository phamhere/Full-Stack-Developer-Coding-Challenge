from db import db

class ContactsModel(db.Model):
	__tablename__ = 'contacts'

	id = db.Column(db.Integer, primary_key=True)
	_id = db.Column(db.String(80))
	contactId = db.Column(db.String(80))
	contactStatus = db.Column(db.String(80))
	contactName = db.Column(db.Integer)
	contactGround = db.Column(db.String(80))
	contactSatellite = db.Column(db.String(80))
	contactEquipment = db.Column(db.String(80))
	contactState = db.Column(db.String(80))
	contactStep = db.Column(db.String(80))
	contactDetail = db.Column(db.String(400))
	contactBeingTimeStamp = db.Column(db.Integer)
	contactEndTimeStamp = db.Column(db.Integer)
	contactLatitude = db.Column(db.Float(12))
	contactLongitude = db.Column(db.Float(12))
	contactAzimuth = db.Column(db.Float(12))
	contactElevation = db.Column(db.Float(12))
	contactResolution = db.Column(db.String(80))
	contactResolutionStatus = db.Column(db.String(80))