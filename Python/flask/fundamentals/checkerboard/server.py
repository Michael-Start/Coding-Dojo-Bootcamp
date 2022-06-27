from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', x = 4)

@app.route('/<int:x>')
def vartable(x):

    return render_template('index.html', x=x)

if __name__ == "__main__":
    app.run(debug=True)