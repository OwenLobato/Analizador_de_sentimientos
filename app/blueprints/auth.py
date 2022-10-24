""" AUTH Module """
import functools
from flask import render_template, Blueprint, flash, g, redirect, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from models.user_model import User
from models.restaurant_model import Restaurant

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """ Registar usuario """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        role = request.form.get('role')
        restaurant_id = request.form.get('restaurant_id')
        # Check restaurant_id null
        if restaurant_id is '':
            restaurant_id = None
        else:
            restaurant_id = int(restaurant_id)
        # Assign values to params
        params = {
            "email": email,
            "password": generate_password_hash(password),
            "name": name,
            "role": role,
            "restaurant_id": restaurant_id
        }
        # Flash errors
        error = None
        if not email:
            error = 'Se requiere su correo electronico'
        elif not password:
            error = 'Se requiere su contraseña'
        elif not name:
            error = 'Se requiere su nombre'
        elif not role:
            error = 'Se requiere su rol'
        # Logic
        user_fetch = User().find_by_params({'email': email})
        restaurant_fetch = Restaurant().find_by_params({'id': restaurant_id})
        if user_fetch is None:
            if restaurant_fetch or restaurant_id is None:
                user = User(**params)
                user.create()
                return redirect(url_for('auth.login'))
            else:
                error = "Restaurante no existente"
        else:
            error = f"El correo '{user_fetch.email}' ya existe"
        flash(error)
    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Iniciar sesion """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        error = None
        user = User().find_by_params({'email': email})
        # Check user credentials
        if user is None:
            error = 'Correo inexistente'
        elif not check_password_hash(user.password, password):
            error = 'Contraseña incorrecta'
        # Login
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')

@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    """ Cerrar sesion """
    session.clear()
    return redirect(url_for('index'))

@auth_bp.before_app_request
def load_logged_user():
    """ Check if user is logged and load it """
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)

def login_required(bp):
    """ Decorator to require user login """
    @functools.wraps(bp)
    def wrapped_bp(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return bp(**kwargs)
    return wrapped_bp
