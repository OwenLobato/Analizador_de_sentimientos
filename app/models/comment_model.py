""" COMMENT model module """

from db import db

class Comment(db.Model):
    """ Comment model class """
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    profile_id = db.Column(db.Integer, db.ForeignKey("profile.id"), nullable=False)
    created_time = db.Column(db.Time, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    message = db.Column(db.Text, nullable=False)
    reactions = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, post_id, profile_id, created_time, created_date, message, reactions) -> None:
        self.post_id = post_id
        self.profile_id = profile_id
        self.created_time = created_time
        self.created_date = created_date
        self.message = message
        self.reactions = reactions

    def __repr__(self) -> str:
        return f"Comentario: {self.message}"
