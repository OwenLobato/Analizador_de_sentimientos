""" STATISTIC Module """

from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.file_model import File
from models.page_model import Page
from helpers.excel_helper import ExcelHelper

statistic_bp = Blueprint('statistic', __name__, url_prefix='/statistics/pages')

@statistic_bp.route('/<int:page_id>', methods=['GET', 'POST'])
@statistic_bp.route('/', methods=['GET', 'POST'])
@login_required
def index(page_id = None):
    """ Index of statics """
    params = request.args
    pages = Page().get_all(params)
    page_fetch = Page().find_by_params({'id': page_id})
    excel_files = File().get_all({'page_id': page_id})
    if request.method == 'POST':
        params = request.args
        pages = Page().get_all(params)
        page_id = request.form.get('page_id')
        if page_id is '0':
            flash('Seleccione una pagina', 'error')
            return render_template('statistic/index.html', pages = pages, excel_files = excel_files, page_id = page_id)
        return redirect(url_for('statistic.index', page_id = page_id))
    return render_template('statistic/index.html', pages = pages, excel_files = excel_files, page_fetch = page_fetch)

@statistic_bp.route('/<int:file_id>/graphics', methods=['GET', 'POST'])
@login_required
def graphic(file_id):
    """ Graphics the excel data """
    (file_fetch, posts_fetch, comments_fetch) = ExcelHelper('').read_db_file(file_id)

    return render_template(
        'statistic/graphic.html',
        file_id = file_id,
        file_fetch = file_fetch,
        posts_fetch = posts_fetch,
        comments_fetch = comments_fetch
    )
