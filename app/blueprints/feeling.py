""" FEELING Module """
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required

feeling_bp = Blueprint('feeling', __name__, url_prefix='/feelings')

@feeling_bp.route('/')
@login_required
def index():
    """ Index of sentiment analysis """
    return render_template('feeling/index.html')
