# Flask module
from flask import Flask, request, jsonify
# Basic authentication module
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
# JWT module
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
basic_auth = HTTPBasicAuth()
jwt_app = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'n1*s2>a3?d_4'

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Basic authentication part
@basic_auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username)['password'], password):
        return "Basic Auth: Access Granted"
    return "Unauthorized", 401


@app.route('/basic-protected', methods=['GET'])
@basic_auth.login_required
def basic():
    return "Basic Auth: Access Granted"

# JWT authentication part
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username in users and check_password_hash(users.get(username).get('password'), password):
        new_token = create_access_token(identity=username)
        return jsonify(jwt_token=new_token)
    return 'Credentials are not valid'


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protect():
    user = get_jwt_identity()
    if user not in users or user is None:
        return "Unauthorized", 401
    return "JWT Auth: Access Granted"


# @jwt_app.unauthorized_loader
# def handle_unauthorized_error(err):
#   return jsonify({"error": "Invalid token"}), 401
# # @app.route('/admin-only', methods=['GET'])
# # @basic_auth.login_required(role='admin1')
# # def only_admins(username):


if __name__ == '__main__':
    app.run(debug=True, port=5000)
