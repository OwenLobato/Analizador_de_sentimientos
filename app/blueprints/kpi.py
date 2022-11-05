""" KPI Module """
from flask import render_template, Blueprint, flash, g, redirect, request, url_for
from blueprints.auth import login_required

kpi_bp = Blueprint('kpi', __name__, url_prefix='/kpis')

@kpi_bp.route('/')
@login_required
def index():
    """ Index of kpis """
    return render_template('kpi/index.html')
