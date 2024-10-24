#!/usr/bin/env python3
import flask
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}
@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    arr = []
    for username in users:
        arr.append(username)
    return jsonify(arr)

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):
    if users[username]:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user", methods=["POST"])
def add_user():
    new_user = request.get_json()
    user = new_user.get("username")
    if not user:
        return jsonify({"error": "Username is required"}), 400
    users[user] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201

if __name__ == "__main__":
    app.run()
