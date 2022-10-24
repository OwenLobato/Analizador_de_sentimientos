from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from werkzeug.exceptions import abort
from models.user_model import User
from models.restaurant_model import Restaurant
from blueprints.auth import login_required

restaurant_bp = Blueprint('restaurant', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/')
def index():
    """ Get all restaurants """
    params = request.args
    restaurants = Restaurant().get_all(params)
    return render_template('restaurant/index.html', restaurants = restaurants)

@restaurant_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """ Register restaurant """
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        region = request.form.get('region')
        kind = request.form.get('kind')
        # Assign values to params
        params = {
            "name": name,
            "address": address,
            "region": region,
            "kind": kind
        }
        # Flash errors
        error = None
        if not name:
            error = 'Se requiere el nombre del restaurante'
        elif not address:
            error = 'Se requiere la direccion del restaurante'
        elif not region:
            error = 'Se requiere la region del restaurante'
        elif not kind:
            error = 'Se requiere el tipo de restaurante'

        if error is not None:
            flash(error)
        else:
            restaurant_fetch = Restaurant().find_by_params({'name': name})
            if restaurant_fetch is None:
                restaurant = Restaurant(**params)
                restaurant.create()
                return redirect(url_for('restaurant.index'))
            else:
                error = f"El restaurante '{restaurant_fetch.name}' ya existe"
        flash(error)
    return render_template('restaurant/create.html')
