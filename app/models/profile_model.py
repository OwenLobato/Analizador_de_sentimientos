""" PROFILE model module """

from db import db

class Profile(db.Model):
    """ Profile model class """
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    comments = db.relationship('Comment', backref='profile')

    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender

    def __repr__(self) -> str:
        return f"Perfil: {self.name}"
