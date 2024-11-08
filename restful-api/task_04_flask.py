#!/usr/bin/env python3
from flask import Flask, jsonify, request
app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data', methods=['GET'])
def user_list():
    arr = [i for i in users.keys()]
    return jsonify(arr)


@app.route('/status', methods=['GET'])
def return_ok():
    return 'OK', 200


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data.get('username')
    users[username] = data
    response_dict = {
        "message": "User added",
        "user": users[username]
    }
    return jsonify(response_dict), 201


if __name__ == '__main__':
    app.run(port=5000)
