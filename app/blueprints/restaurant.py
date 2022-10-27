""" RESTAURANT Module """
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from models.restaurant_model import Restaurant
from blueprints.auth import login_required

restaurant_bp = Blueprint('restaurant', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/')
@login_required
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

@restaurant_bp.route('/<int:restaurant_id>/update', methods=['GET', 'POST'])
@login_required
def update(restaurant_id):
    """ Update restaurant """
    restaurant = Restaurant().find_by_params({'id': restaurant_id})
    if request.method == 'POST':
        error = None
        if restaurant:
            restaurant.name = request.form.get('name')
            restaurant.address = request.form.get('address')
            restaurant.region = request.form.get('region')
            restaurant.kind = request.form.get('kind')
            # Assign values to body
            body = {
                "name": restaurant.name,
                "address": restaurant.address,
                "region": restaurant.region,
                "kind": restaurant.kind
            }
            if not restaurant.name:
                error = 'Se requiere el nombre del restaurante'
            elif not restaurant.address:
                error = 'Se requiere la direccion del restaurante'
            elif not restaurant.region:
                error = 'Se requiere la region del restaurante'
            elif not restaurant.kind:
                error = 'Se requiere el tipo de restaurante'

            if error is not None:
                flash(error)
            else:
                updated_rest = Restaurant().update(restaurant_id, body)
                if updated_rest:
                    return redirect(url_for('restaurant.index'))
                return error
            flash(error)
        else:
            error = 'El restaurante con ese id no existe'
        flash(error)
    return render_template('restaurant/update.html', restaurant = restaurant)

@restaurant_bp.route('/<int:restaurant_id>/destroy', methods=['GET', 'POST'])
@login_required
def destroy(restaurant_id):
    """ Destroy restaurant """
    Restaurant().destroy(restaurant_id)
    return redirect(url_for('restaurant.index'))
