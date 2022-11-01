""" USER Module """
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.user_model import User
from models.restaurant_model import Restaurant

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/')
@login_required
def index():
    """ Get all users """
    params = request.args
    users = User().get_all(params)
    return render_template('user/index.html', users = users)


@user_bp.route('/<int:user_id>/update', methods=['GET', 'POST'])
@login_required
def update(user_id):
    """ Update user """
    restaurants = Restaurant().get_all(request.args)
    user = User().find_by_params({'id': user_id})
    if request.method == 'POST':
        error = None
        if user:
            user.name = request.form.get('name')
            user.role = request.form.get('role')
            user.restaurant_id = request.form.get('restaurant_id')

            # Check restaurant_id null
            if user.restaurant_id is '':
                user.restaurant_id = None
            else:
                user.restaurant_id = int(user.restaurant_id)

            # Assign values to body
            body = {
                "name": user.name,
                "role": user.role,
                "restaurant_id": user.restaurant_id
            }

            if not user.name:
                error = 'Se requiere el nombre del usuario'
            elif not user.role:
                error = 'Se requiere el rol del usuario'

            if error is not None:
                flash(error)
            else:
                restaurant_fetch = None
                try:
                    restaurant_fetch = Restaurant().find_by_params({'id': user.restaurant_id})
                except:
                    return "Restaurante no existente"
                if restaurant_fetch or user.restaurant_id is None:
                    updated_rest = User().update(user_id, body)
                    if updated_rest:
                        return redirect(url_for('user.index'))
                    return error                    
            flash(error)
        else:
            error = 'El user con ese id no existe'
        flash(error)
    return render_template('user/update.html', user = user, restaurants = restaurants)

@user_bp.route('/<int:user_id>/destroy', methods=['GET', 'POST'])
@login_required
def destroy(user_id):
    """ Destroy user """
    User().destroy(user_id)
    return redirect(url_for('user.index'))
