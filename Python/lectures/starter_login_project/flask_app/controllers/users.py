# Where we define our routes!
from flask_app import app # Needed for @app.route() among other things
#from flask_app.models import User # Import models
from flask import render_template, redirect, request, session # Import methods from Flask


@app.route('/')
def landing():
    return render_template('login_reg.html')

