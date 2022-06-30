from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key="oy you gits"

@app.route('/')
def landing():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)