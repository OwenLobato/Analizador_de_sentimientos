""" RESTAURANT model module """

from db import db
from datetime import datetime
class Restaurant(db.Model):
    """ Restaurant model class """
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    region = db.Column(db.String(45), nullable=False)
    kind = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    deleted_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    fields = [
        "id",
        "name",
        "address",
        "region",
        "kind",
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
                print("**************** ERROR RESTAURANT PARAMS **************")

    def get_all(self, params=None):
        """ Get all restaurants """
        self.__validate_params(params)
        return self.query.filter_by(deleted_at=None, **params).all()

    def create(self):
        """ Create a restaurant using an instance of class """
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first restaurant coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a restaurant """
        restaurant = self.find_by_params({'id': id, 'deleted_at': None})
        if restaurant:
            for key, value in params.items():
                setattr(restaurant, key, value)
            db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def deactive(self, restaurant_id, g_user_id):
        """ Logic deleted a restaurant """
        params = {
            'deleted_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'deleted_by': g_user_id
        }
        restaurant = self.find_by_params({'id': restaurant_id})
        if restaurant:
            for key, value in params.items():
                setattr(restaurant, key, value)
            db.session.commit()
            return self.find_by_params({'id': restaurant_id})
        return None

    def destroy(self, restaurant_id):
        """ Destroy an restaurant """
        restaurant = self.find_by_params({"id": restaurant_id})
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return True
        return False
