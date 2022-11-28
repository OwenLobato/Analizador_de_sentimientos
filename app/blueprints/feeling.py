""" FEELING Module """

import nltk
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
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
    # File data
    (file_fetch, posts_fetch, comments_fetch) = ExcelHelper('').read_db_file(file_id)
    # Word cloud
    file = File().find_by_params({'id': file_id})
    file_path = file.path + file.name
    wordcloud_path = __get_word_cloud(file_path, file.name)

    return render_template(
        'feeling/comments.html',
        file_id = file_id,
        file_fetch = file_fetch,
        posts_fetch = posts_fetch,
        comments_fetch = comments_fetch,
        wordcloud_path = wordcloud_path
    )

def __get_word_cloud(file_path, file_name):
    # Download and set spanish stopwords
    nltk.download('stopwords')
    stop_words = set(stopwords.words('spanish'))
    # Read and join all comments
    comments = ExcelHelper(file_path).read_comments()
    words = comments.message.tolist()
    words = map(str, words)
    words = ' '.join(words).lower()
    # Generate wordcloud
    word_cloud = WordCloud(
        collocations = True,
        background_color = '#FFFCF0',
        colormap = ListedColormap(["#1F5C82", "#278ECF", "#CF3C3C", "#D5AC2E"]),
        stopwords = stop_words,
        width = 1500,
        height = 400,
        min_word_length = 5,
        max_words = 100
    ).generate(words)
    # Save wordcloud to PNG image
    file_name = file_name.split('.')[0]
    wordcloud_path = f"uploads/{file_name}.png"
    word_cloud.to_file(f"static/{wordcloud_path}")
    return wordcloud_path
