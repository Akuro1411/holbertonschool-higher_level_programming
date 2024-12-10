#!/usr/bin/python3
"""Flask is imported for app"""
from flask import render_template, Flask

app = Flask(__name__)


@app.route("/")
def run_app():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
