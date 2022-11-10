""" FEELING Module """
import os
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required
from models.page_model import Page
from models.restaurant_model import Restaurant
from models.post_model import Post
from models.reaction_model import Reaction
from models.comment_model import Comment

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
    """ Post comments sentiment analysis """
    posts_fetch = Post().get_all({'page_id': page_id}, True)

    all_reactions = []
    all_total = []
    all_comments = {}
    all_post_react = []


    for post in posts_fetch:
        reactions_fetch = Reaction().find_by_params({'post_id': post.id})
        all_reactions.append(reactions_fetch)

        total_reactions = Reaction().get_total_reactions(post.id)
        all_total.append(total_reactions)

        post_sent = ''
        if total_reactions != 0:
            reactions = {
                "angry": reactions_fetch.angry,
                "haha": reactions_fetch.haha,
                "like": reactions_fetch.like,
                "love": reactions_fetch.love,
                "sad": reactions_fetch.sad,
                "wow": reactions_fetch.wow,
                "care": reactions_fetch.care
            }
            val_max = max(reactions, key = reactions.get)

            if val_max == 'angry':
                post_sent = 'Esta publicacion es disgustante'
            if val_max == 'haha':
                post_sent = 'Esta publicacion es divertida'
            if val_max == 'like':
                post_sent = 'Esta publicacion es llamativa'
            if val_max == 'love':
                post_sent = 'Esta publicacion es encantadora'
            if val_max == 'sad':
                post_sent = 'Esta publicacion es triste'
            if val_max == 'wow':
                post_sent = 'Esta publicacion es impresionante'
            if val_max == 'care':
                post_sent = 'Esta publicacion es relevante'
        else:
            post_sent = 'Publicacion sin reacciones'
        all_post_react.append(post_sent)
        print(post_sent)


        comments_fetch = Comment().get_all({'post_id': post.id})
        all_comments[post.id] = comments_fetch


    return render_template(
        'feeling/comments.html',
        page_id = page_id,
        posts_fetch = posts_fetch,
        all_reactions = all_reactions,
        all_post_react = all_post_react,
        all_total = all_total,
        all_comments = all_comments,
    )
