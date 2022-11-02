""" RESTAURANT Module """
from werkzeug.utils import secure_filename
import os 
from datetime import datetime
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.restaurant_model import Restaurant
from models.page_model import Page

restaurant_bp = Blueprint('restaurant', __name__, url_prefix='/restaurants')

@restaurant_bp.route('/')
@login_required
def index():
    """ Get all restaurants """
    params = request.args
    restaurants = Restaurant().get_all(params)
    return render_template('restaurant/index.html', restaurants = restaurants)

@restaurant_bp.route('/<int:restaurant_id>/page', methods=['GET', 'POST'])
@login_required
def page(restaurant_id):
    """ Create or update a restaurant page """
    restaurant = Restaurant().find_by_params({'id': restaurant_id})
    page_fetch = Page().find_by_params({'restaurant_id': restaurant.id})
    if request.method == 'POST':
        if page_fetch is None:
            # Crear
            name = request.form.get('name')
            followers = request.form.get('followers')
            params = {
                "restaurant_id": restaurant_id,
                "name": name,
                "followers": followers
            }
            error = None
            if not name:
                error = "Se requiere nombre de la página"
            elif not followers:
                error = "Se requiere la cantidad de seguidores"

            if error is not None:
                flash(error)
            else:
                page = Page(**params)
                page.create()
                return redirect(url_for('restaurant.index'))
            flash(error)
        else:
            #Actualizar
            page_fetch.name = request.form.get('name')
            page_fetch.followers = request.form.get('followers')
            body = {
                "name": page_fetch.name,
                "followers": page_fetch.followers
            }
            error = None
            if not page_fetch.name:
                error = 'Se requiere el nombre de la página de facebook del restaurante'
            elif not page_fetch.followers:
                error = 'Se requiere la cantidad de seguidores de la página'
            if error is not None:
                flash(error)
            else:
                updated_page = Page().update(page_fetch.id, body)
                if updated_page:
                    return redirect(url_for('restaurant.index'))
                return error
            flash(error)




    return render_template('restaurant/page.html', page = page_fetch)

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

@restaurant_bp.route('/<int:restaurant_id>/upload', methods=['GET', 'POST'])
@login_required
def upload(restaurant_id):
    """ Upload data to a restaurant """
    restaurant = Restaurant().find_by_params({'id': restaurant_id})
    if request.method == 'POST':
        excel_data = request.files['data']
        now = datetime.now()
        name = f"{str(restaurant.id)}_{now.year}{now.month}{now.day}_{now.hour}{now.minute}{now.second}_{excel_data.filename.replace(' ','_')}"
        file_name = secure_filename(name)
        path = 'static/uploads'
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.abspath(f'{path}/{file_name}')
        excel_data.save(file_path)
    return render_template('restaurant/upload.html', restaurant = restaurant)

@restaurant_bp.route('/<int:restaurant_id>/destroy', methods=['GET', 'POST'])
@login_required
def destroy(restaurant_id):
    """ Destroy restaurant """
    Restaurant().destroy(restaurant_id)
    return redirect(url_for('restaurant.index'))
