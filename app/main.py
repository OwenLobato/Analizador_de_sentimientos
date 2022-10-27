""" Main flask module"""

from flask import Flask
from db import db
from config import Config
from blueprints.auth import auth_bp
from blueprints.restaurant import restaurant_bp
from blueprints.user import user_bp

app = Flask(__name__)
app.config.from_object(Config())

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(user_bp)

db.init_app(app)

@app.route('/routes')
def index():
    """ App routes """
    routes = {
        "/auth": [
            "/register - [GET, POST] - register()",
            "/login - [GET, POST] - login()",
            "/logout - [GET, POST] - logout()"
            "/users/<int:user_id>/update - [GET, POST] - update()",
            "/users/<int:user_id>/destroy - [GET, POST] - destroy()",
        ],
        "/restaurants": [
            "/ - [GET] - index()",
            "/create - [GET, POST] - create()",
            "/<int:restaurant_id>/update - [GET, POST] - update()"
            "/<int:restaurant_id>/destroy - [GET, POST] - destroy()"
        ]
    }
    return routes

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
