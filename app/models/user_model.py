""" USER model module """

from db import db


class User(db.Model):
    """ User model class """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    restaurant_id = db.Column(
        db.Integer, db.ForeignKey("restaurant.id"), nullable=True)

    fields = [
        "id",
        "email",
        "password",
        "name",
        "role",
        "restaurant_id"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR USER PARAMS **************")

    def get_all(self, params=None):
        """ Get all users """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a user using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a user"""
        user = self.find_by_params({'id': id})
        if user:
            for key, value in params.items():
                setattr(user, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, user_id):
        """Destroy an user in  DB"""
        user = self.find_by_params({"id": user_id})
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
