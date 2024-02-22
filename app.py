from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""Run the Flask application in debug mode.

This allows the Flask server to reload when code changes and 
show debugging output. It should only be used during 
development, not in production.
"""

@app.route('/')
def welcome_page():
    return "Welcome to the first page!"

@app.route('/design')
def design_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)