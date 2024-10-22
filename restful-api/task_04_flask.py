import flask
from flask import jsonify
from flask import request
app = flask.Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
         "arnold": {"name": "Arnold", "age": 30, "city": "Los Angeles"}
         }


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def user_list():
    return jsonify(users)


@app.route('/status')
def status():
    return "OK"


@app.route('/user/<username>')
def get_user_info(username):
    if username not in users:
        return {"error": "User not found"}
    return jsonify(users[username])


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

