""" Config Module """

class Config:
    def __init__(self):
        self.__user = "root"
        self.__pass = "12345"
        self.__host = "localhost"
        self.__port = "3306"
        self.__db = "analizador"
        self.SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{self.__user}:{self.__pass}@{self.__host}:{self.__port}/{self.__db}"
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
