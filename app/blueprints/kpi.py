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
    (growth_rate, post_reach, applause_rate, avg_engagement_rate, amplification_rate, comment_conversation_rate) = __get_kips(file_id)
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
        comment_conversation_rate = comment_conversation_rate
    )

# Get KPIs functions

def __get_kpi_growth_rate(page):
    new_followers = page.new_followers
    all_followers = page.all_followers
    growth_rate = (new_followers/all_followers) * 100
    return growth_rate

def __get_kpi_post_reach(page, posts):
    # all_followers = page.all_followers
    # posts = len(posts)
    post_reach = 20
    return post_reach

def __get_kpi_applause_rate(page, posts):
    all_followers = page.all_followers
    posts_likes = []
    for post in posts:
        posts_likes.append(post.like)
    likes = max(posts_likes)
    applause_rate = (likes / all_followers) * 100
    return applause_rate

def __get_kpi_avg_engagement_rate():
    avg_engagement_rate = 40
    return avg_engagement_rate

def __get_kpi_amplification_rate():
    amplification_rate = 50
    return amplification_rate

def __get_kpi_comment_conversation_rate():
    comment_conversation_rate = 60
    return comment_conversation_rate

def __get_kips(file_id):
    file = File().find_by_params({'id': file_id})
    page = Page().find_by_params({'id': file.page_id})
    posts = Post().get_all({'file_id': file_id})
    growth_rate = __get_kpi_growth_rate(page)
    post_reach = __get_kpi_post_reach(page, posts)
    applause_rate = __get_kpi_applause_rate(page, posts)
    avg_engagement_rate = __get_kpi_avg_engagement_rate()
    amplification_rate = __get_kpi_amplification_rate()
    comment_conversation_rate = __get_kpi_comment_conversation_rate()
    return (
        growth_rate,
        post_reach,
        applause_rate,
        avg_engagement_rate,
        amplification_rate,
        comment_conversation_rate
    )
