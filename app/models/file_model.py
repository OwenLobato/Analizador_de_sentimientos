""" FILE model module """

from db import db
from datetime import datetime

class File(db.Model):
    """ File model class """
    __tablename__ = "file"
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    page_id = db.Column(db.Integer, db.ForeignKey("page.id"), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    path = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=True)
    deleted_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    deleted_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    fields = [
        "id",
        "page_id",
        "name",
        "path",
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
                print("**************** ERROR FILE PARAMS **************")

    def get_all(self, params=None):
        """ Get all files """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a file using an instance of class """
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first file coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a file """
        file = self.find_by_params({'id': id, 'deleted_at': None})
        if file:
            for key, value in params.items():
                setattr(file, key, value)
            db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def deactive(self, file_id, g_user_id):
        """ Logic deleted a file """
        params = {
            'deleted_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'deleted_by': g_user_id
        }
        file = self.find_by_params({'id': file_id})
        if file:
            for key, value in params.items():
                setattr(file, key, value)
            db.session.commit()
            return self.find_by_params({'id': file_id})
        return None
        return None

    def destroy(self, file_id):
        """ Destroy an file """
        file = self.find_by_params({"id": file_id})
        if file:
            db.session.delete(file)
            db.session.commit()
            return True
        return False
