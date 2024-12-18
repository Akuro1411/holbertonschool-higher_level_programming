#!/usr/bin/python3
"""Flask is imported for app"""
import json
import csv
from flask import render_template, Flask, request, jsonify

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
    return render_template('items.html', item=item)


@app.route('/products')
def products_finder():
    id = request.args.get("id")
    if id:
        with open("products.json") as file:
            data = json.load(file)
            for row in data:
                if row["id"] == int(id):
                    return jsonify(row)
            error_id = "Product not found"
            return render_template("product_display.html", error_id=error_id)
    source = request.args.get("source")
    if source == "csv":
        with open("products.csv") as file:
            row_data = csv.DictReader(file)
            data = []
            for row in row_data:
                id, price = int(row["id"]), float(row["price"])
                row["id"], row["price"] = id, price
                data.append(row)
    elif source == "json":
        with open("products.json") as file:
            json_data = json.load(file)
            data = json_data
    else:
        return render_template("product_display.html", error_source="Wrong source")
    return render_template("product_display.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)

