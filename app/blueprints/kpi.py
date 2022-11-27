""" KPI Module """

from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.file_model import File
from models.page_model import Page
from models.post_model import Post
from helpers.excel_helper import ExcelHelper

kpi_bp = Blueprint('kpi', __name__, url_prefix='/kpis/pages')

@kpi_bp.route('/<int:page_id>', methods=['GET', 'POST'])
@kpi_bp.route('/', methods=['GET', 'POST'])
@login_required
def index(page_id = None):
    """ Index of kpis """
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
            return render_template('kpi/index.html', pages = pages, excel_files = excel_files, page_id = page_id)
        return redirect(url_for('kpi.index', page_id = page_id))
    return render_template('kpi/index.html', pages = pages, excel_files = excel_files, page_fetch = page_fetch)

@kpi_bp.route('/<int:file_id>/analysis', methods=['GET', 'POST'])
@login_required
def analysis(file_id):
    """ Post comments kpis """
    (file_fetch, posts_fetch, comments_fetch) = ExcelHelper('').read_db_file(file_id)
    (growth_rate, post_reach, applause_rate, avg_engagement_rate, amplification_rate, virality_rate) = __get_kips()
    if request.method == 'POST':
        start_date = request.form.get('start_date')
        finish_date = request.form.get('finish_date')

    return render_template(
        'kpi/analysis.html',
        # Date
        oldest_date = Post().get_oldest_date(file_id),
        recent_date = Post().get_recent_date(file_id),
        # File
        file_id = file_id,
        file_fetch = file_fetch,
        posts_fetch = posts_fetch,
        comments_fetch = comments_fetch,
        # KPIs
        growth_rate = growth_rate,
        post_reach = post_reach,
        applause_rate = applause_rate,
        avg_engagement_rate = avg_engagement_rate,
        amplification_rate = amplification_rate,
        virality_rate = virality_rate
    )

# Get KPIs functions

def __get_kpi_growth_rate():
    growth_rate = 1
    return growth_rate

def __get_kpi_post_reach():
    post_reach = 2
    return post_reach

def __get_kpi_applause_rate():
    applause_rate = 3
    return applause_rate

def __get_kpi_avg_engagement_rate():
    avg_engagement_rate = 4
    return avg_engagement_rate

def __get_kpi_amplification_rate():
    amplification_rate = 5
    return amplification_rate

def __get_kpi_virality_rate():
    virality_rate = 6
    return virality_rate

def __get_kips():
    growth_rate = __get_kpi_growth_rate()
    post_reach = __get_kpi_post_reach()
    applause_rate = __get_kpi_applause_rate()
    avg_engagement_rate = __get_kpi_avg_engagement_rate()
    amplification_rate = __get_kpi_amplification_rate()
    virality_rate = __get_kpi_virality_rate()
    return (
        growth_rate,
        post_reach,
        applause_rate,
        avg_engagement_rate,
        amplification_rate,
        virality_rate
    )
