import re
from flask import Flask, request, jsonify
from flask_jwt_extended import (JWTManager, jwt_required,
                                create_access_token, get_raw_jwt)
from . import model
# setting up flask
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my-key'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
app.config["TESTING"] = True
app.url_map.strict_slashes = False
jwt = JWTManager(app)

# creating user object
A_USER = model.Users()

# creating the signup api endpoint which is a post request


@app.route('/auth/signup', methods=['POST'])
def register():
    '''endpoint to register a user'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Fields cannot be empty"})
    username = data.get('username')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    if username is None or not username:
        return jsonify({"message": "Enter username"})
    if name is None or not name:
        return jsonify({"message": "Enter name"}), 206

    if len(password) < 4:
        return jsonify({"message": "password is too short"})
    if confirm_password != password:
        return jsonify({"message": "Passwords don't match"})
    b = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    match = re.match(b, email)
    if match is None:
        return jsonify({"message": "Enter a valid email address"})
    result = A_USER.put(name, username, email, password)
    access_token = create_access_token(username)

    result["access_token"] = access_token

    return jsonify(result), 201
