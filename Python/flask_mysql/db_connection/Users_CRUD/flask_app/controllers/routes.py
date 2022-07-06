from flask_app.models.users import User
from flask_app import app
from flask import render_template, redirect, request

@app.route('/')
def landing():
    return render_template('/users.html', users=User.get_all())

@app.route('/new')
def newuser():
    return render_template('/new_user.html')

@app.route('/create_user', methods = ['POST'])
def create():
    data ={
    'fname': request.form['fname'],
    'lname': request.form['lname'],
    'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/show/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    print(data)
    return render_template('/show.html', user =User.one_user(data))

@app.route('/update/<int:id>')
def update(id):
    data = {
        'id':id
    }
    return render_template('/edit.html', user = User.one_user(data))

@app.route('/edit/<int:id>', methods =['POST'])
def edit(id):
    data ={
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'id' : id
        }
    User.update(data)
    return redirect('/')

@app.route('/delete<int:id>')
def delete(id):
    data={
        'id' : id
    }
    User.delete(data)
    return redirect('/')