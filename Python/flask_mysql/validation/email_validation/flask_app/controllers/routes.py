from flask_app import app 
from flask_app.models.emails import Email
from flask import render_template, redirect, request

@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/list')
def list_emails():
    return render_template('list.html', emails = Email.list())

@app.route('/add_email', methods = ['POST'])
def add_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.new_email(request.form)
    return redirect('/list')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect ('/')