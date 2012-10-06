from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

module = Blueprint('simple_page', __name__,
                        template_folder='templates')


@module.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)