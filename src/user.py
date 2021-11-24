from flask import Blueprint
from flask import jsonify # for return
from flask import request # for url parameter and password
import hashlib
#import db

user_bp = Blueprint('user', __name__)

'''
    request body: {"username": ..., "password": ...}

    return: {"valid": true/false}
'''
@user_bp.route('/login/', methods=['GET', 'POST'])
def login():
    username = request.form['username']
    password = hashlib.md5(request.form['password'].encode())

    '''
    user = db.query(
        'SELECT COUNT(*) FROM users WHERE username = %s AND password = %s',
        (username, password)
    )

    if user == 0:
        return jsonify({"valid":False})
    
    return jsonify({"valid":True})
    '''

    return jsonify({'username':username, 'password':password.hexdigest()})

'''
    request body: {"username": ..., "password": ...}

    return: {"valid": true/false}
'''
@user_bp.route('/signup/', methods=['POST'])
def signup():
    username = request.form['username']
    password = hashlib.md5(request.form['password'].encode())

    '''
    # see if it exists
    user = db.query(
        'SELECT COUNT(*) FROM users WHERE username = %s AND password = %s',
        (username, password)
    )

    if user == 0:
        # if not, create it (signup)
        db.query(
            'INSERT INTO users (username, password) VALUES(%s, %s)',
            (username, password)
        )

        # return false, showing it didnt exist and was created
        return jsonify({"valid":False})
    
    # return true, showing it existed already
    return jsonify({"valid":True})
    '''

    return jsonify({'username':username, 'password':password.hexdigest()})