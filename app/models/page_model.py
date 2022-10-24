""" PAGE model module """

from db import db

class Page(db.Model):
    """ Page model class """
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    followers = db.Column(db.Integer, nullable=False, default=0)
    posts = db.relationship('Post', backref='page')

    def __init__(self, restaurant_id, name, followers) -> None:
        self.restaurant_id = restaurant_id
        self.name = name
        self.followers = followers

    def __repr__(self) -> str:
        return f"Pagina: {self.name}"
