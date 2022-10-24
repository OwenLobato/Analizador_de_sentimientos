""" RESTAURANT model module """

from db import db

class Restaurant(db.Model):
    """ Restaurant model class """
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    region = db.Column(db.String(45), nullable=False)
    kind = db.Column(db.String(45), nullable=False)

    fields = [
        "id",
        "name",
        "address",
        "region",
        "kind"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR RESTAURANT PARAMS **************")

    def get_all(self, params=None):
        """ Get all restaurants """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a restaurant using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a restaurant"""
        restaurant = self.find_by_params({'id': id})
        if restaurant:
            for key, value in params.items():
                setattr(restaurant, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, restaurant_id):
        """Destroy an restaurant in  DB"""
        restaurant = self.find_by_params({"id": restaurant_id})
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return True
        return False
