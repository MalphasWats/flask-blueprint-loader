from flask import (Flask, request, session, g, redirect, url_for,
                   abort, render_template, flash, jsonify)

import os,sys
import imp

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('home.html',
                            cwd = os.getcwd())
                            
                            
def load_blueprints():
    fp, pathname, description = imp.find_module('very_simple_page', 'blueprints')
    print fp, pathname, description
    mod = imp.load_module('very_simple_page', fp, pathname, description)
        
    app.register_blueprint(getattr(mod, 'module'))