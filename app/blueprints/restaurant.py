""" RESTAURANT Module """
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.restaurant_model import Restaurant
from models.page_model import Page
from models.schedule_model import Schedule
from models.file_model import File
from helpers.schedule import week_days, hours
from helpers.excel_helper import ExcelHelper

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
    page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
    if request.method == 'POST':
        if page_fetch is None:
            # CREATE
            name = request.form.get('name')
            new_followers = request.form.get('followers')
            all_followers = new_followers
            params = {
                "restaurant_id": restaurant_id,
                "name": name,
                "new_followers": new_followers,
                "all_followers": all_followers,
                "created_by": g.user.id
            }
            error = None
            if not name:
                error = "Se requiere nombre de la página"
            elif not all_followers:
                error = "Se requiere la cantidad de seguidores"

            if error is not None:
                flash(error, 'error')
            else:
                page = Page(**params)
                page.create()
                flash('Datos de la página creados correctamente', 'success')
                return redirect(url_for('restaurant.index'))
            flash(error, 'error')
        else:
            # UPDATE
            page_fetch.name = request.form.get('name')
            followers = int(request.form.get('followers'))
            page_fetch.new_followers = followers - page_fetch.all_followers
            page_fetch.all_followers = followers
            body = {
                "name": page_fetch.name,
                "new_followers": page_fetch.new_followers,
                "all_followers": page_fetch.all_followers,
                "updated_by": g.user.id
            }
            error = None
            if not page_fetch.name:
                error = 'Se requiere el nombre de la página de facebook del restaurante'
            elif not page_fetch.all_followers:
                error = 'Se requiere la cantidad de seguidores de la página'
            if error is not None:
                flash(error, 'error')
            else:
                updated_page = Page().update(page_fetch.id, body)
                if updated_page:
                    flash('Datos de la página actualizados correctamente', 'success')
                    return redirect(url_for('restaurant.index'))
                return error
            flash(error, 'error')
    return render_template('restaurant/page.html', page = page_fetch)

@restaurant_bp.route('/<int:restaurant_id>/schedule', methods=['GET', 'POST'])
@login_required
def schedule(restaurant_id):
    """ Create or update a restaurant schedule """
    schedule_fetch = Schedule().get_all({'restaurant_id': restaurant_id})
    schedule = []
    if schedule_fetch:
        for sche in schedule_fetch:
            schedule.append(int(sche.schedule_name.split("_")[1]))
        if request.method == 'POST':
            # UPDATE (delete and create)
            for sche in schedule_fetch:
                Schedule().destroy(sche.id)
            options = request.form.getlist('schedule')
            for day in week_days:
                for s in week_days[day]:
                    for op in options:
                        if s == op:
                            params = {
                                "week_day": day,
                                "start_hour": week_days[day][s][0],
                                "finish_hour": week_days[day][s][1],
                                "schedule_name": s,
                                "restaurant_id": restaurant_id
                            }
                            schedule = Schedule(**params)
                            schedule.create()
            flash('Horario actualizado exitosamente','success')
            return redirect(url_for('restaurant.index'))
    else:
        if request.method == 'POST':
            # CREATE
            options = request.form.getlist('schedule')
            for day in week_days:
                for s in week_days[day]:
                    for op in options:
                        if s == op:
                            params = {
                                "week_day": day,
                                "start_hour": week_days[day][s][0],
                                "finish_hour": week_days[day][s][1],
                                "schedule_name": s,
                                "restaurant_id": restaurant_id
                            }
                            schedule = Schedule(**params)
                            schedule.create()
            flash('Horario creado exitosamente','success')
            return redirect(url_for('restaurant.index'))
    return render_template('restaurant/schedule.html', schedule = schedule, hours = hours)

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
            "kind": kind,
            "created_by": g.user.id
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
            flash(error, 'error')
        else:
            restaurant_fetch = Restaurant().find_by_params({'name': name})
            if restaurant_fetch is None:
                restaurant = Restaurant(**params)
                restaurant.create()
                flash('Restaurante creado correctamente', 'success')
                return redirect(url_for('restaurant.index'))
            else:
                error = f"El restaurante '{restaurant_fetch.name}' ya existe"
        flash(error, 'error')
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
                "kind": restaurant.kind,
                "updated_by": g.user.id
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
                flash(error, 'error')
            else:
                updated_rest = Restaurant().update(restaurant_id, body)
                if updated_rest:
                    flash('Restaurante actualizado correctamente', 'success')
                    return redirect(url_for('restaurant.index'))
                return error
            flash(error, 'error')
        else:
            error = 'El restaurante con ese id no existe'
        flash(error, 'error')
    return render_template('restaurant/update.html', restaurant = restaurant)

@restaurant_bp.route('/<int:restaurant_id>/upload', methods=['GET', 'POST'])
@login_required
def upload(restaurant_id):
    """ Upload data to a restaurant """
    restaurant_fetch = Restaurant().find_by_params({'id': restaurant_id})
    page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
    excel_files = None
    if page_fetch:
        excel_files = File().get_all({'page_id': page_fetch.id})

    if request.method == 'POST':
        page_fetch = Page().find_by_params({'restaurant_id': restaurant_id})
        if not page_fetch:
            flash('Favor de previamente registrar una pagina','error')
            return redirect(url_for('restaurant.upload', restaurant_id = restaurant_id))
        # File naming
        excel_data = request.files['data']
        name = __name_excel_file(excel_data, restaurant_fetch.id)
        # Folder creation
        path = 'static/uploads/'
        if not os.path.exists(path):
            os.makedirs(path)
        # File creation
        file_name = secure_filename(name)
        file_path = os.path.abspath(f'{path}/{file_name}')
        excel_data.save(file_path)
        # Save file in the DB
        params = {
            "page_id": page_fetch.id,
            "name": name,
            "path": path,
            "created_by": g.user.id
        }
        file = File(**params)
        file.create()
        # Save file info in the DB
        excel_db = ExcelHelper(file.path + file.name).save_excel_data(restaurant_id, file.id)
        if excel_db:
            flash('Archivo subido correctamente', 'success')
        else:
            # ExcelHelper(file.path + file.name).delete_excel_data(restaurant_id, file.id)  # Rollback in case erro file
            flash('Elimine el archivo, corríjalo y vuelva a intentarlo', 'error')
        return redirect(url_for('restaurant.upload', restaurant_id = restaurant_id))
    return render_template('restaurant/upload.html', restaurant=restaurant_fetch, excel_files=excel_files, page_fetch=page_fetch)

def __name_excel_file(excel_data, restaurant_id):
    """Generate excel file name

    Args:
        excel_data (file): Excel file
        restaurant_id (int): Restaurant id

    Returns:
        String: New excel file name (id_date_hour___Excel_file_name.xslx)
    """
    now = datetime.now()
    n_date = f"{now.year}{now.month}{now.day}"
    n_hour = f"{now.hour}{now.minute}{now.second}"
    name = f"{str(restaurant_id)}_{n_date}_{n_hour}___{excel_data.filename.replace(' ','_')}"
    return name

@restaurant_bp.route('/<int:restaurant_id>/upload/delete/<int:file_id>')
@login_required
def delete_excel(restaurant_id, file_id):
    """ Delete excel data and file """
    msj = 'Error en borrado de archivo'
    status = 'error'
    deactive_file = File().deactive(file_id, g.user.id)
    if deactive_file:
        file_fetch = File().find_by_params({'id': file_id})
        path = os.path.join(file_fetch.path, file_fetch.name)
        ExcelHelper(file_fetch.path + file_fetch.name).delete_excel_data(restaurant_id, file_id)
        os.remove(path)
        # Delete wordcloud image if exist
        wc_path = f"static/uploads/{file_fetch.name.split('.')[0]}.png"
        if os.path.exists(wc_path):
            os.remove(wc_path)
        msj = 'Archivo borrado correctamente'
        status = 'success'
    flash(msj, status)
    return redirect(url_for('restaurant.upload', restaurant_id = restaurant_id))

@restaurant_bp.route('/<int:restaurant_id>/destroy', methods=['GET', 'POST'])
@login_required
def destroy(restaurant_id):
    """ Destroy restaurant """
    Restaurant().destroy(restaurant_id)
    return redirect(url_for('restaurant.index'))

@restaurant_bp.route('/<int:restaurant_id>/deactive', methods=['GET', 'POST'])
@login_required
def deactive(restaurant_id):
    """ Deactive restaurant """
    deactive_rest = Restaurant().deactive(restaurant_id, g.user.id)
    if deactive_rest:
        flash('Restaurante desactivado correctamente', 'success')
    return redirect(url_for('restaurant.index'))
