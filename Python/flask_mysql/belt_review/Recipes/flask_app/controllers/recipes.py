from flask_app import app
from flask_app.models.recipes import Recipe
from flask_app.models.users import User
from flask_app.controllers import users
from flask import render_template, redirect, session, request
from flask import flash
from flask_bcrypt  import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/add_recipe')
def create():
    if 'user_id' not in session:
        flash('You must be logged in to view this page')
        return redirect('/')
    return render_template('add_new_recipe.html')
    
@app.route('/create_recipe', methods=['POST'])
def add_recipe():
    data = {
        'name' : request.form['name'],
        'description': request.form['description'],
        'date_made' : request.form['date'],
        'instructions': request.form['instructions'],
        'time' : request.form['time'],
        'user_id' : session['user_id']
    }
    #if not Recipe.validate_recipe(data):
        #return redirect ('/add_recipe')
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/view_recipe/<int:id>')
def view_one(id):
    data = {
        'id' : id
    }
    return render_template('recipe_display.html', recipe = Recipe.view_one(data))

