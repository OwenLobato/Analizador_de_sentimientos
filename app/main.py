""" Main flask module"""

from flask import Flask
from db import db
from config import Config
# from blueprints.user import user_bp

app = Flask(__name__)
app.config.from_object(Config())

""" Blueprints """
# app.register_blueprint(user_bp)

db.init_app(app)

@app.route('/')
def index():
    return 'Created by: Owen Lobato!'

if __name__ == '__main__':
    app.run(debug=True)
