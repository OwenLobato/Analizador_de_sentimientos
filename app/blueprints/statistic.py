""" STATISTIC Module """

import os
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.page_model import Page
from models.restaurant_model import Restaurant
from helpers.excel_helper import ExcelHelper

statistic_bp = Blueprint('statistic', __name__, url_prefix='/statistics')

@statistic_bp.route('/<int:page_id>', methods=['GET', 'POST'])
@statistic_bp.route('/', methods=['GET', 'POST'])
@login_required
def index(page_id = None):
    """ Index of statics """
    params = request.args
    pages = Page().get_all(params)
    if page_id:
        excel_files = __get_excel_files(page_id)
    else:
        excel_files = []
    if request.method == 'POST':
        params = request.args
        pages = Page().get_all(params)
        page_id = request.form.get('page_id')
        if page_id is '0':
            flash('Seleccione una pagina', 'error')
            return render_template('statistic/index.html', pages = pages, excel_files = [])
        excel_files = __get_excel_files(page_id)
        return redirect(url_for('statistic.index', page_id = page_id))
    return render_template('statistic/index.html', pages = pages, excel_files = excel_files)

def __get_excel_files(page_id):
    """ Get all the excel files by page_id """
    page_fetch = Page().find_by_params({'id': page_id})
    restaurant_fetch = Restaurant().find_by_params({'id': page_fetch.restaurant_id})
    uploads = [f for f in os.listdir('static/uploads') if os.path.isfile(os.path.join('static/uploads', f))]
    excel_files = [excel_name for excel_name in uploads if int(excel_name[0]) == restaurant_fetch.id]
    return excel_files

@statistic_bp.route('/<int:page_id>/graphics/<string:file>', methods=['GET', 'POST'])
@login_required
def graphic(page_id, file):
    """ Graphics the excel data """
    file_path = 'static/uploads/' + file
    page_fetch = Page().find_by_params({'id': page_id})
    posts = ExcelHelper(file_path).read_posts()
    reactions = ExcelHelper(file_path).read_reactions()
    comments = ExcelHelper(file_path).read_reactions()

    return render_template(
        'statistic/graphic.html',
        page_fetch = page_fetch,
        posts = posts,
        reactions = reactions,
        comments = comments,
        file_name =  file.split('___')[1]
    )


# Gráfica 1: Por mes cantidad de H y M de comentarios totales
# Gráfica 2: Mes y hora del post y reacciónes totales
# Gráfica 3: Cantidad de comentarios por mes (H y M)
# Gráfica 4: Número de compartidas de post por mes

# Pasar de lectura de excel a lectura de mysql