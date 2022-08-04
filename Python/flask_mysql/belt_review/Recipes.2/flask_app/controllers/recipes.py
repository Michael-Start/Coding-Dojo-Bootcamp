from flask_app import app
from flask_app.models.recipes import Recipe
from flask_app.models.users import User
#from flask_app.controllers import users
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
    #if not Recipe.validate_recipe(request.form):
        #return redirect ('/add_recipe')
    data = {
        'name' : request.form['name'],
        'description': request.form['description'],
        'date_made' : request.form['date'],
        'instructions': request.form['instructions'],
        'time' : request.form['time'],
        'user_id' : session['user_id']
    }
    Recipe.add_recipe(data)
    return redirect('/dashboard')

@app.route('/view_recipe/<int:id>')
def view_one(id):
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id']
    }
    data = {
        'id' : id
    }
    return render_template('recipe_display.html', recipe = Recipe.view_one(data), user=User.get_by_id(user_data))
    
@app.route('/delete/<int:id>')
def delete(id):
    data={
        'id' : id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/edit_recipe/<int:id>')
def edit(id):
    data={
        'id' : id
    }
    return render_template('edit_recipe.html', recipe=Recipe.view_one(data))

@app.route('/update_recipe/<int:id>', methods=['POST'])
def update(id):

    data ={
    'name': request.form['name'],
    'description': request.form['description'],
    'instructions': request.form['instructions'],
    'time' : request.form['time'],
    'date' : request.form['date'],
    'id' : id
        }
    Recipe.edit(data)
    return redirect('/dashboard')
