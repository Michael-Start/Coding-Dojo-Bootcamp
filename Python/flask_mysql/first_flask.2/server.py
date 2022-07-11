<<<<<<< HEAD
from flask import Flask, render_template, redirect, request
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=['POST'])
def create_friend():
    #First we make a data dictionary from the request.form coming from the template page.
    #The keys in data need to line up exactly with the variables in our query string
    data ={
        'fname': request.form['fname'],
        'lname' : request.form['lname'],
        'occ' : request.form['occ']
    }
#we pass the data dictionary into the save method from Friend class
    Friend.save(data)
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)

=======
from flask import Flask, render_template
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
            
if __name__ == "__main__":
    app.run(debug=True)

>>>>>>> e7d0478fbf1ab043623e4921430e41c0d5112a08
