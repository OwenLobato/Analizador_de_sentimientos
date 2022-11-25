""" COMMENT model module """

from db import db

class Comment(db.Model):
    """ Comment model class """
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_id = db.Column(db.String(16), db.ForeignKey("post.id"), nullable=False)
    from_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    created_time = db.Column(db.Time, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    message = db.Column(db.Text, nullable=False)
    feeling = db.Column(db.String(15), nullable=False)
    reactions = db.Column(db.Integer, nullable=False, default=0)

    fields = [
        "id",
        "post_id",
        "from_name",
        "gender",
        "created_time",
        "created_date",
        "message",
        "feeling",
        "reactions"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR COMMENT PARAMS **************")

    def get_all(self, params=None):
        """ Get all comments """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a comment using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a comment"""
        comment = self.find_by_params({'id': id})
        if comment:
            for key, value in params.items():
                setattr(comment, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, post_id):
        """Destroy a comment in DB"""
        comments = self.get_all({"post_id": post_id})
        if comments:
            for comment in comments:
                db.session.delete(comment)
                db.session.commit()
            return True
        return False
