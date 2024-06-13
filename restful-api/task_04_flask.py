#!/usr/bin/env python3
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    arr = []
    for i in users:
        arr.append(i)
    return jsonify(arr)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def profile(username):
    if username in users:
        return users[username]
    else:
        return {"error": "User not found"}

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run()
