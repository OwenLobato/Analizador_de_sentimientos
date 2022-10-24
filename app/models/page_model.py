""" PAGE model module """

from db import db

class Page(db.Model):
    """ Page model class """
    __tablename__ = 'page'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    followers = db.Column(db.Integer, nullable=False, default=0)

    fields = [
        "id",
        "restaurant_id",
        "name",
        "followers"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR PAGE PARAMS **************")

    def get_all(self, params=None):
        """ Get all pages """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a page using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a page"""
        page = self.find_by_params({'id': id})
        if page:
            for key, value in params.items():
                setattr(page, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, page_id):
        """Destroy an page in  DB"""
        page = self.find_by_params({"id": page_id})
        if page:
            db.session.delete(page)
            db.session.commit()
            return True
        return False
