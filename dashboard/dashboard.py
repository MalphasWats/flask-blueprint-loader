from flask import (Flask, request, session, g, redirect, url_for,
                   abort, render_template, flash, jsonify)

import os
import imp

from functools import wraps

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template('home.html',
                            cwd = os.getcwd())
                            
                            
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)
        return redirect(url_for('home'))
    return decorated_function
                            
                            
def load_blueprints():
    """
        This code looks for any modules or packages in the given directory, loads them
        and then registers a blueprint - blueprints must be created with the name 'module'
        Implemented directory scan
        
        Bulk of the code taken from:
            https://github.com/smartboyathome/Cheshire-Engine/blob/master/ScoringServer/utils.py
    """
    
    path = 'blueprints'
    dir_list = os.listdir(path)
    mods = {}
    
    for fname in dir_list:
        if os.path.isdir(os.path.join(path, fname)) and os.path.exists(os.path.join(path, fname, '__init__.py')):
            f, filename, descr = imp.find_module(fname, [path])
            mods[fname] = imp.load_module(fname, f, filename, descr)
            app.register_blueprint(getattr(mods[fname], 'module'))
        elif os.path.isfile(os.path.join(path, fname)):
            name, ext = os.path.splitext(fname)
            if ext == '.py' and not name == '__init__':
                f, filename, descr = imp.find_module(name, [path])
                mods[fname] = imp.load_module(name, f, filename, descr)
                app.register_blueprint(getattr(mods[fname], 'module'))
