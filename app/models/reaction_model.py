""" REACTION model module """

from db import db

class Reaction(db.Model):
    """ Reaction model class """
    __tablename__ = 'reaction'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    angry = db.Column(db.Integer, nullable=False, default=0)
    haha = db.Column(db.Integer, nullable=False, default=0)
    like = db.Column(db.Integer, nullable=False, default=0)
    love = db.Column(db.Integer, nullable=False, default=0)
    sad = db.Column(db.Integer, nullable=False, default=0)
    wow = db.Column(db.Integer, nullable=False, default=0)
    care = db.Column(db.Integer, nullable=False, default=0)

    fields = [
        "id",
        "post_id",
        "angry",
        "haha",
        "like",
        "love",
        "sad",
        "wow",
        "care"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR REACTION PARAMS **************")

    def get_all(self, params=None):
        """ Get all reactions """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a reaction using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a reaction"""
        reaction = self.find_by_params({'id': id})
        if reaction:
            for key, value in params.items():
                setattr(reaction, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, reaction_id):
        """Destroy an reaction in  DB"""
        reaction = self.find_by_params({"id": reaction_id})
        if reaction:
            db.session.delete(reaction)
            db.session.commit()
            return True
        return False