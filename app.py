import os
from flask import Flask
from flaskext.mysql import MySQL      # For newer versions of flask-mysql 
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome Tim!"

@app.route('/how are you')
def hello():
    return "I am good, thank you"

if __name__ == "__main__":
    app.run()
