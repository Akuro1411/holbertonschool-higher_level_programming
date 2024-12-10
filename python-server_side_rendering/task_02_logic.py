#!/usr/bin/python3
"""Flask is imported for app"""
import json

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

@app.route('/items')
def items_func():
    try:
        with open("item.json") as file:
            items = json.load(file)
            item = items["items"]
    except Exception:
        item = []
    return render_template('items.html', item=item), 200


if __name__ == "__main__":
    app.run()

