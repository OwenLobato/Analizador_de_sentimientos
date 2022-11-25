""" USER model module """

from db import db
from datetime import datetime


class User(db.Model):
    """ User model class """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    updated_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    deleted_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    fields = [
        "id",
        "email",
        "password",
        "name",
        "role",
        "restaurant_id",
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
                print("**************** ERROR USER PARAMS **************")

    def get_all(self, params=None):
        """ Get all users """
        self.__validate_params(params)
        return self.query.filter_by(deleted_at=None, **params).all()

    def create(self):
        """ Create an user using an instance of class """
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first user coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a user """
        user = self.find_by_params({'id': id, 'deleted_at': None})
        if user:
            for key, value in params.items():
                setattr(user, key, value)
            db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def deactive(self, user_id, g_user_id):
        """ Logic deleted a user """
        params = {
            'deleted_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'deleted_by': g_user_id
        }
        user = self.find_by_params({'id': user_id})
        if user:
            for key, value in params.items():
                setattr(user, key, value)
            db.session.commit()
            return self.find_by_params({'id': user_id})
        return None

    def destroy(self, object_id):
        """ Destroy a user """
        user = self.find_by_params({"id": object_id})
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
