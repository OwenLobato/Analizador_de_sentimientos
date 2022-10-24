""" PROFILE model module """

from db import db

class Profile(db.Model):
    """ Profile model class """
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    fields = [
        "id",
        "name",
        "gender"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR PROFILE PARAMS **************")

    def get_all(self, params=None):
        """ Get all profiles """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a profile using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a profile"""
        profile = self.find_by_params({'id': id})
        if profile:
            for key, value in params.items():
                setattr(profile, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, profile_id):
        """Destroy an profile in  DB"""
        profile = self.find_by_params({"id": profile_id})
        if profile:
            db.session.delete(profile)
            db.session.commit()
            return True
        return False
