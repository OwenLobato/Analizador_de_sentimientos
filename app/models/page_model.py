""" PAGE model module """

from db import db
from datetime import datetime

class Page(db.Model):
    """ Page model class """
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    all_followers = db.Column(db.Integer, nullable=False, default=0)
    new_followers = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    deleted_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    fields = [
        "id",
        "restaurant_id",
        "name",
        "all_followers",
        "new_followers",
        "created_at",
        "updated_at",
        "deleted_at",
        "created_by",
        "updated_by",
        "deleted_by"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR PAGE PARAMS **************")

    def get_all(self, params=None):
        """ Get all pages """
        self.__validate_params(params)
        return self.query.filter_by(deleted_at=None, **params).all()

    def create(self):
        """ Create a page using an instance of class """
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first page coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a page """
        page = self.find_by_params({'id': id, 'deleted_at': None})
        if page:
            for key, value in params.items():
                setattr(page, key, value)
            db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def deactive(self, id, params):
        """ Logic deleted a page """
        page = self.find_by_params({'id': id, 'deleted_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        if page:
            for key, value in params.items():
                setattr(page, key, value)
            db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, page_id):
        """ Destroy an page """
        page = self.find_by_params({"id": page_id})
        if page:
            db.session.delete(page)
            db.session.commit()
            return True
        return False
