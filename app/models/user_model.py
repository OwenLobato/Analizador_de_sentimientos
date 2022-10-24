""" USER model module """

from db import db

class User(db.Model):
    """ User model class """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=True)

    def __init__(self, email, password, name, role, restaurant_id) -> None:
        self.email = email
        self.password = password
        self.name = name
        self.role = role
        self.restaurant_id = restaurant_id

    def __repr__(self) -> str:
        return f"Correo usuario: {self.email}"
