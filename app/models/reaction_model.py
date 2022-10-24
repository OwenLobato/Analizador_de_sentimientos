""" REACTION model module """

from db import db

class Reaction(db.Model):
    """ Reaction model class """
    __tablename__ = 'reaction'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    angry = db.Column(db.Integer, nullable=False, default=0)
    haha = db.Column(db.Integer, nullable=False, default=0)
    like = db.Column(db.Integer, nullable=False, default=0)
    love = db.Column(db.Integer, nullable=False, default=0)
    sad = db.Column(db.Integer, nullable=False, default=0)
    wow = db.Column(db.Integer, nullable=False, default=0)
    care = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, post_id, angry, haha, like, love, sad, wow, care) -> None:
        self.post_id = post_id
        self.angry = angry
        self.haha = haha
        self.like = like
        self.love = love
        self.sad = sad
        self.wow = wow
        self.care = care

    def __repr__(self) -> str:
        return f"Reacciones del post_id: {self.post_id}"
