from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

def get_memes():
    url = ""

@blueprint.route('/memes')
def memes():

    return render_template('sandbox/memes.html')

@blueprint.route('/recorder')
def recorder():

    return render_template('sandbox/recorder.html')