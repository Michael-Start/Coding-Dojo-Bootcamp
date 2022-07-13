
from flask_app import app
from flask_app.models.users import User
from flask import render_template, redirect, session, request
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def landing():
    return render_template('login.html')

@app.route('/register_user', methods =['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect ('/')
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form ['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    print(data)
    id = User.new_user(data)
    session['user_id'] = id
    print(session)
    print(session['user_id'])
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : session['user_id']
    }
    return render_template('dashboard.html', user = User.get_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash('Email not fond')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password not found')
        return redirect ('/')
    session['user_id']= user.id
    print(session)
    print(session['user_id'])
    print(user)
    return redirect('/dashboard')


