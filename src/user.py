import hashlib
from flask import Blueprint
from flask import jsonify  # for return
from flask import request  # for url parameter and password
import db

user_bp = Blueprint('user', __name__)

'''
    Logs users into their profile 
    request body: {"username": ..., "password": ...}

    return: {"valid": true/false}
'''
@user_bp.route('/login/', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data.get('username')
    password = hashlib.md5(data.get('password').encode()).hexdigest()

    user = db.query(
        'SELECT COUNT(*) FROM user_data WHERE username = %s AND password = %s',
        (username, password)
    )[0][0]

    if user == 0:
        return jsonify({"valid": False})

    return jsonify({"valid": True})


'''
    Creates a new user profile
    request body: {"username": ..., "password": ...}

    return: {"valid": true/false}
'''
@user_bp.route('/signup/', methods=['POST'])
def signup():
    data = request.get_json(force=True)
    username = data.get('username')
    password = hashlib.md5(data.get('password').encode()).hexdigest()

    # see if it exists
    user = db.query(
        'SELECT COUNT(*) FROM user_data WHERE username = %s AND password = %s',
        (username, password)
    )[0][0]

    if user == 0:
        # if not, create it (signup)
        db.query(
            'INSERT INTO user_data(username, password) VALUES(%s, %s)',
            (username, password)
        )

        # return true, showing it didnt exist and was created
        return jsonify({"valid": True})

    # return false, showing it existed already
    return jsonify({"valid": False})


'''
    request body: {"username": ..., "password": ...}

    return: {"valid": true/false}
'''
@user_bp.route('/deleteuser/', methods=['DELETE'])
def delete():
    data = request.get_json(force=True)
    username = data.get('username')
    password = hashlib.md5(data.get('password').encode()).hexdigest()

    # see if it exists
    user = db.query(
        'SELECT COUNT(*) FROM user_data WHERE username = %s AND password = %s',
        (username, password)
    )[0][0]

    if user == 0:
        # return false, showing it didnt exist and was created
        return jsonify({"valid": False})

    # valid, then delete
    db.query(
        f'DELETE FROM user_data WHERE username = \'{username}\''
    )

    # return true, showing it existed already
    return jsonify({"valid": True})
