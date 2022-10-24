""" RESTAURANT model module """

from db import db

class Restaurant(db.Model):
    """ Restaurant model class """
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    region = db.Column(db.String(45), nullable=False)
    kind = db.Column(db.String(45), nullable=False)
    users = db.relationship('User', backref='restaurant')
    schedules = db.relationship('Schedule', backref='restaurant')
    pages = db.relationship('Page', backref='restaurant')

    def __init__(self, name, address, region, kind) -> None:
        self.name = name
        self.address = address
        self.region = region
        self.kind = kind

    def __repr__(self) -> str:
        return f"Restaurante: {self.name}"
