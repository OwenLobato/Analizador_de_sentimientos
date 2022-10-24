""" Main flask module"""

import json
from flask import Flask
from db import db
from config import Config
from blueprints.auth import auth_bp
from blueprints.restaurant import restaurant_bp

app = Flask(__name__)
app.config.from_object(Config())

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(restaurant_bp)

db.init_app(app)

@app.route('/')
def index():
    """ App routes """
    routes = {
        "/auth": [
            "/register - [GET, POST] - register()",
            "/login - [GET, POST] - login()",
            "/logout - [GET, POST] - logout()"
        ],
        "/restaurants": [
            "/ - [GET] - index()",
            "/create - [GET, POST] - create()"
        ]
    }
    routes = json.dumps(routes, indent=2)
    return routes

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
