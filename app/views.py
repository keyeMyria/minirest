import os
from flask import render_template, request, jsonify, Response, send_from_directory
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from app import app

template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

# ==== entry points for one-page web application - no auth ====
@app.route('/')
def index():
  return render_template("indexpy.html")

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'cisco', 'cisco'),
    User(2, 'cisco1', 'cisco'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    print(username, password)
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

# ==== JWT ===
jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

# = end of JWT =

# ==== here is REST API calls ===
# if we don't need authenticate

# get
@app.route('/api/noauth/v1/get/<v1>/<v2>/<v3>/<v4>', methods = ['GET'])
def call1(v1,v2,v3,v4):
  if True:  # you can call any your function here with v1,...,v4
    # your code may be here as well
    return jsonify( { 'message': 'ok' } ), 200
    # or return jsonify( { 'message': your_variable } ), 200
  else:
    return jsonify( { 'message': 'your_error_message'} ), 401

# put
@app.route('/api/noauth/v1/put/<v1>/<v2>/<v3>/<v4>/<v5>', methods = ['PUT'])
def call2(v1,v2,v3,v4,v5):
    if True:  # you can call any your function here with v1,...,v4
      # your code may be here as well
      return jsonify( { 'message': 'ok' } ), 200
      # or return jsonify( { 'message': your_variable } ), 200
    else:
      return jsonify( { 'message': 'your_error_message'} ), 401

# and if we will need in web token authentication

# get for tests
@app.route('/api/auth/test', methods=['GET'])
@jwt_required()
def call_auth_test():
    return jsonify({'message': 'ok'}), 200

# get
@app.route('/api/auth/v1/get', methods=['GET'])
@jwt_required()
def call_a1():
    items = [{'i1':1},{'i2':2}];
    return jsonify({'message': items}), 200

# get2
@app.route('/api/auth/v1/get2/<v1>/<v2>', methods=['GET'])
@jwt_required()
def call_a2(v1,v2):
    if True:  # you can call any your function here with v1,...,v4
      # your code may be here as well
      return jsonify( { 'message': 'ok' } ), 200
      # or return jsonify( { 'message': your_variable } ), 200
    else:
      return jsonify( { 'message': 'your_error_message'} ), 401

# put
@app.route('/api/auth/v1/put/<v1>/<v2>', methods=['PUT'])
@jwt_required()
def call_a3(v1, v2):
    if True:  # you can call any your function here with v1,...,v4
      # your code may be here as well
      return jsonify( { 'message': 'ok' } ), 200
      # or return jsonify( { 'message': your_variable } ), 200
    else:
      return jsonify( { 'message': 'your_error_message'} ), 401

# ==== end of API calls from one-page web application ====

if __name__ == '__main__':
  app.run()
