from . import db

class TestRent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    apr = db.Column(db.Integer, nullable=False)

class UserInp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    period = db.Column(db.String(80), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)