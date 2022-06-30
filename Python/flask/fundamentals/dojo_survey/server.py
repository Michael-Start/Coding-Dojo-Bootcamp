<<<<<<< HEAD

from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="oy you gits"

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/create', methods = ['POST'])
def survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
