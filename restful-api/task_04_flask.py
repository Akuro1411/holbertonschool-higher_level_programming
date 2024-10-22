import flask
from flask import jsonify
from flask import request
app = flask.Flask(__name__)

users = {}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def user_list():
    arr = []
    for username in users:
        arr.append(username)
    return jsonify(arr)


@app.route('/status')
def status():
    return "OK"


@app.route('/user/<username>')
def get_user_info(username):
    if users[username]:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})    if users[username]:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.get_json()
    user = data.get("username")
    if not user:
        return jsonify({"error": "Username is required"}), 404
    users[user] = data
    response_post = {"message": "User added", "user": data}
    return jsonify(response_post), 201

if __name__ == "__main__":
    app.run(port=5000)

