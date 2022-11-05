""" Main flask module"""

from flask import Flask, url_for, redirect
from db import db
from config import Config
from blueprints.auth import auth_bp
from blueprints.restaurant import restaurant_bp
from blueprints.user import user_bp
from blueprints.feeling import feeling_bp
from blueprints.statistic import statistic_bp
from blueprints.kpi import kpi_bp

app = Flask(__name__)
app.config.from_object(Config())

# Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(restaurant_bp)
app.register_blueprint(user_bp)
app.register_blueprint(feeling_bp)
app.register_blueprint(statistic_bp)
app.register_blueprint(kpi_bp)

db.init_app(app)

@app.route('/')
def index():
    """ Main to login """
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.run(debug=True)
