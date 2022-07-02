from flask_app import app   #define the app
from flask_app.controllers import attractions #define our routes
app.secret_key="oy you gits"

if __name__ == "__main__":
    app.run(debug=True)