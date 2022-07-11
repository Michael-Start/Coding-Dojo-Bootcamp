from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja
from flask_app import app
from flask import render_template, redirect, request

@app.route('/')
def landing():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos= Dojo.get_all())

@app.route('/location/<int:id>')
def location(id):
    data ={
        'id' : id
    }
    return render_template('location.html', dojo = Dojo.dojo_ninjas(data)) 

@app.route('/new_ninja')
def new_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/create_ninja', methods=['POST'])
def add_ninja():
    Ninja.new_ninja(request.form)
    return redirect('/')

@app.route('/new_dojo', methods =['POST'])
def add_dojo():
    Dojo.new_dojo(request.form)
    return redirect('/')