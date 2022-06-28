from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "oy you gits!"

@app.route('/')
def landing():
    if 'x' in session:
        session['x'] +=1
    else:
        session['x'] = 0
    return render_template('index.html', x=session['x'])


@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    if 'x' in session:
        session['x']+=1
    else:
        session['x'] =1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)