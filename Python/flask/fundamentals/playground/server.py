
from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome! Please type /play/number/color!'

@app.route('/play')
def play():
    color = 'blue' 
    num =3
    return render_template('index.html', color = color, num =num)

@app.route('/play/<int:num>')
def blue_boxes(num):
    color = 'blue'
    return render_template('index.html', num = num, color = color)

@app.route('/play/<int:num>/<string:color>')
def boxes(num, color):
    return render_template('index.html', color = color, num = num)

if __name__ == "__main__":
    app.run(debug=True)