from flask import Blueprint

module = Blueprint('very_simple_page', __name__,
                        template_folder='templates')


@module.route('/very_simple_page')
def show():
    return """<html>
    <head>
    <title>Very Simple Page</title>
    </head>
    <body>
    <h1>Very Simple Page</h1>
    <p>This is a very simple Page</p>
    </body>
    </html>"""