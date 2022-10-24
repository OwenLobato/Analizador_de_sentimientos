""" POST model module """

from db import db

class Post(db.Model):
    """ Post model class """
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey("page.id"), nullable=False)
    created_time = db.Column(db.Time, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    message = db.Column(db.Text, nullable=False)
    clasification = db.Column(db.String(30), nullable=False)
    xformat = db.Column(db.String(30), nullable=False)
    share = db.Column(db.Integer, nullable=False, default=0)
    comments = db.relationship('Comment', backref='post')
    reactions = db.relationship('Reaction', backref='post')

    def __init__(self, page_id, created_time, created_date, message, clasification, xformat, share) -> None:
        self.page_id = page_id
        self.created_time = created_time
        self.created_date = created_date
        self.message = message
        self.clasification = clasification
        self.xformat = xformat
        self.share = share

    def __repr__(self) -> str:
        return f"Publicación: {self.message}"
