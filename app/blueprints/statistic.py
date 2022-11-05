""" STATISTIC Module """
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required

statistic_bp = Blueprint('statistic', __name__, url_prefix='/statistics')

@statistic_bp.route('/')
@login_required
def index():
    """ Index of statistics """
    return render_template('statistic/index.html')
