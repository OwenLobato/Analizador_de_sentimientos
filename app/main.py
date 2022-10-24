""" Main flask module"""

from flask import Flask
from db import db
from config import Config
from blueprints.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config())

# Blueprints
app.register_blueprint(auth_bp)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Created by: Owen Lobato!</h1>'

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
