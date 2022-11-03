""" SCHEDULE model module """

from db import db

class Schedule(db.Model):
    """ Schedule model class """
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    week_day = db.Column(db.String(9), nullable=False)
    start_hour = db.Column(db.Time, nullable=False)
    finish_hour = db.Column(db.Time, nullable=False)
    schedule_name = db.Column(db.String(12), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)

    fields = [
        "id",
        "week_day",
        "start_hour",
        "finish_hour",
        "schedule_name",
        "restaurant_id"
    ]

    def __validate_params(self, params):
        """ Validate if sent params are valid """
        for param in params:
            if param not in self.fields:
                print("**************** ERROR SCHEDULE PARAMS **************")

    def get_all(self, params=None):
        """ Get all schedules """
        self.__validate_params(params)
        return self.query.filter_by(**params).all()

    def create(self):
        """ Create a schedule using an instance of class """
        db.session.add(self)
        db.session.commit()

    def find_by_params(self, params):
        """ Get the first coincidence to the given params """
        self.__validate_params(params)
        return self.query.filter_by(**params).first()

    def update(self, id, params):
        """ Update a schedule"""
        schedule = self.find_by_params({'id': id})
        if schedule:
            for key, value in params.items():
                setattr(schedule, key, value)
                db.session.commit()
            return self.find_by_params({'id': id})
        return None

    def destroy(self, schedule_id):
        """Destroy an schedule in  DB"""
        schedule = self.find_by_params({"id": schedule_id})
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
            return True
        return False
