from flask import Flask
# Basic authentication modules
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user_password = users.get(username)['password']
    if username in users and check_password_hash(user_password, password):
        return users[username]
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
