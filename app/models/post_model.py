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

    fields = [
        "id",
        "page_id",
        "created_time",
        "created_date",
        "message",
        "clasification",
        "xformat",
        "share"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR POST PARAMS **************")

    def get_all(self, params=None):
        """ Get all posts """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a post using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a post"""
        post = self.find_by_params({'id': id})
        if post:
            for key, value in params.items():
                setattr(post, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, post_id):
        """Destroy an post in  DB"""
        post = self.find_by_params({"id": post_id})
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return False
