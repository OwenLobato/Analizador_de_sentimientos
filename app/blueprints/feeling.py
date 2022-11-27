""" FEELING Module """

from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.file_model import File
from models.page_model import Page
from helpers.excel_helper import ExcelHelper

feeling_bp = Blueprint('feeling', __name__, url_prefix='/feelings/pages')

@feeling_bp.route('/<int:page_id>', methods=['GET', 'POST'])
@feeling_bp.route('/', methods=['GET', 'POST'])
@login_required
def index(page_id = None):
    """ Index of sentiment analysis """
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
            return render_template('feeling/index.html', pages = pages, excel_files = excel_files, page_id = page_id)
        return redirect(url_for('feeling.index', page_id = page_id))
    return render_template('feeling/index.html', pages = pages, excel_files = excel_files, page_fetch = page_fetch)

@feeling_bp.route('/<int:file_id>/comments', methods=['GET', 'POST'])
@login_required
def comments(file_id):
    """ Post comments sentiment analysis """
    (file_fetch, posts_fetch, comments_fetch) = ExcelHelper('').read_db_file(file_id)

    return render_template(
        'feeling/comments.html',
        file_id = file_id,
        file_fetch = file_fetch,
        posts_fetch = posts_fetch,
        comments_fetch = comments_fetch
    )
