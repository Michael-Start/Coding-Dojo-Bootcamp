from flask_app import app
from flask import render_template, request, redirect, session


# visable pages
@app.route('/')
def home_page():
    return render_template('welcome.html')

@app.route('/attractions')
def tourist_page():
    if 'name' not in session:
        return redirect('/')
    if 'attractions' not in session:
        session['attractions'] = []
    return render_template('attractions.html')

# redirect pages

@app.route('/enter', methods=['POST'])
def enter():
    session['name'] = request.form['name']
    return redirect('/attractions')

@app.route('/exit')
def exit():
    session.clear()
    return redirect('/')

@app.route('/add_attraction', methods =['POST'])
def add_attraction_to_session():
    old_attractions= session['attractions']
    old_attractions.append(f"{request.form['attraction']} in {request.form['city']}")
    session['attraction'] = old_attractions
    return redirect('/attractions')

@app.route('/reset_attractions')
def reset():
    session.pop('attractions')
    return redirect('/attractions')
