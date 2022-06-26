from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'   #display Hello World!

@app.route('/dojo')
def dojo():
    return 'Dojo'         #display Dojo

@app.route('/say/<name>')
def sayhi(name):
    print(name)
    return 'Hi ' + str(name)       #display Hi and a name

@app.route('/say/<num>/<word>')
def repeat(num, word):
    print(word)
    return str(word + ' ') * int(num)      #display a word a bunch of times

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.