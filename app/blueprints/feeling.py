""" FEELING Module """
import os
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.page_model import Page
from models.restaurant_model import Restaurant

feeling_bp = Blueprint('feeling', __name__, url_prefix='/feelings/pages')

@feeling_bp.route('/<int:page_id>', methods=['GET', 'POST'])
@feeling_bp.route('/', methods=['GET', 'POST'])
@login_required
def index(page_id = None):
    """ Index of sentiment analysis """
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
            return render_template('feeling/index.html', pages = pages, excel_files = [])
        excel_files = __get_excel_files(page_id)
        return redirect(url_for('feeling.index', page_id = page_id))
    return render_template('feeling/index.html', pages = pages, excel_files = excel_files)

def __get_excel_files(page_id):
    """ Get all the excel files by page_id """
    page_fetch = Page().find_by_params({'id': page_id})
    restaurant_fetch = Restaurant().find_by_params({'id': page_fetch.restaurant_id})
    uploads = [f for f in os.listdir('static/uploads') if os.path.isfile(os.path.join('static/uploads', f))]
    excel_files = [excel_name for excel_name in uploads if int(excel_name[0]) == restaurant_fetch.id]
    return excel_files

@feeling_bp.route('/<int:page_id>/comments', methods=['GET', 'POST'])
@login_required
def comments(page_id):
    """ Page comments sentiment analysis """
    return render_template('feeling/comments.html', page_id = page_id)
