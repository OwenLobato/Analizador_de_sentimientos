""" SCHEDULE model module """

from db import db

class Schedule(db.Model):
    """ Schedule model class """
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    week_day = db.Column(db.String(9), nullable=False)
    start_hour = db.Column(db.Time, nullable=False)
    finish_hour = db.Column(db.Time, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"), nullable=False)

    def __init__(self, week_day, start_hour, finish_hour, restaurant_id) -> None:
        self.week_day = week_day
        self.start_hour = start_hour
        self.finish_hour = finish_hour
        self.restaurant_id = restaurant_id

    def __repr__(self) -> str:
        return f"Horario -> Dia:{self.week_day} Abre:{self.start_hour} Cierra:{self.finish_hour}"
