from datetime import date
from logging import error, exception
from flask import Flask, request, jsonify, make_response
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import numpy as np 
from functools import wraps
from sqlalchemy_utils import database_exists

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'asdfdgd123'  #to use token encoding
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ezml.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  #database
model = None

TOKEN_EXP_MIN = 30

class User(db.Model):
    '''Class representing the users of the application'''
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(
        db.String(50), unique=True
    )  #preventing to reveal the true id if somebody decodes the token
    name = db.Column(db.String(80))
    password = db.Column(
        db.String(80))  #we will store only the hashed password
    admin = db.Column(db.Boolean)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

#TODO: optional refresh the token every x minutes 
def token_required(f):
    '''decorator for token authentication
    if used, the first argument of the decorated function should be current_user'''
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            
            return jsonify({'message': 'token is missing'}), status.HTTP_401_UNAUTHORIZED

        try: #if the token is't valid during decoding, it will raise an exception
            token_data =  jwt.decode(token.encode(), app.config['SECRET_KEY']) #it also checks the expiration of the token
            current_user = User.query.filter_by(public_id=token_data['public_id']).first()
        except:

            return jsonify({'message': 'token is invalid'}),status.HTTP_401_UNAUTHORIZED

        return f(current_user, *args, **kwargs)

    return decorated

@app.route('/register')
def register():
    '''registers a user to the database with the specified username and password,
     but only if the username is not already in use'''

    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        make_response('wrong content', status.HTTP_400_BAD_REQUEST)

    user = User.query.filter_by(name = auth.username).first()
    if user:
        return jsonify({'message' : 'Username already in use!'}),status.HTTP_401_UNAUTHORIZED
   
    try:
        hashed_pwd = generate_password_hash(auth.password, method = 'sha256') #generating salted and hashed password
        #uuid creates unique user id, version 4 creates a random one
        new_user = User(public_id = str(uuid.uuid4()), name = auth.username, password = hashed_pwd, admin = False)
        db.session.add(new_user)
        db.session.commit()
    except:
        
        return jsonify(succes = False), status.HTTP_400_BAD_REQUEST

    #generate token from public_id, and adding a expire time for the token
    token = jwt.encode({'public_id': new_user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = TOKEN_EXP_MIN)}, app.config['SECRET_KEY'])
    return jsonify({'token':token.decode('UTF-8')})
    

@app.route('/login')
def login():
    '''login with username and password'''
    
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        make_response('wrong content', status.HTTP_400_BAD_REQUEST)

    user = User.query.filter_by(name = auth.username).first()
    if not user:
        return jsonify({'message' : 'Cold not verify'}),status.HTTP_401_UNAUTHORIZED

    #user.password is hashed password
    if check_password_hash(user.password, auth.password):
        #generate token from public_id, and adding a expire time for the token
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = TOKEN_EXP_MIN)}, app.config['SECRET_KEY'])
        return jsonify({'token':token.decode('UTF-8')}),status.HTTP_200_OK
    
    return jsonify({'message' : 'Cold not verify'}),status.HTTP_401_UNAUTHORIZED



@app.route('/user', methods = ['GET'])
@token_required
def get_all_users(current_user):
    '''returns all users from the databse'''

    if not current_user.admin:
        return jsonify({'message': 'Not authorized to do that'}), status.HTTP_401_UNAUTHORIZED

    users = User.query.all()
    users = [user.as_dict() for user in users] 
    
    return jsonify({'users' : users})


@app.route('/user/<public_id>', methods = ['GET'])
@token_required
def get_user(current_user, public_id:str):
    '''return one user specified by the user id'''
    
    if not current_user.admin:
        return jsonify({'message': 'Not authorized to do that'}), status.HTTP_401_UNAUTHORIZED

    user = User.query.filter_by(public_id = public_id).first()
    if not user:
         
        return jsonify(succes = False), status.HTTP_400_BAD_REQUEST
    
    user = user.as_dict()

    return jsonify({'user' : user})


@app.route('/user', methods = ['POST'])
@token_required
def create_user(current_user):
    '''create a user from json containing the name and password'''

    if not current_user.admin:
        return jsonify({'message': 'Not authorized to do that'}), status.HTTP_401_UNAUTHORIZED

    try:
        data = request.get_json()
        hashed_pwd = generate_password_hash(data['password'], method = 'sha256') #generating salted and hashed password
        #uuid creates uniwue user id, version 4 creates a random one
        new_user = User(public_id = str(uuid.uuid4()), name = data['name'], password = hashed_pwd, admin = False)
        db.session.add(new_user)
        db.session.commit()
    except:
        
        return jsonify(succes = False), status.HTTP_400_BAD_REQUEST

    return jsonify({'message' : 'Successfully created.'}), status.HTTP_200_OK


@app.route('/user/<public_id>', methods = ['PUT'])
@token_required
def promote_user(current_user, public_id:str):
    '''promotes any user to admin'''
    
    if not current_user.admin:
        return jsonify({'message': 'Not authorized to do that'}), status.HTTP_401_UNAUTHORIZED

    user = User.query.filter_by(public_id = public_id).first()
    if not user:
         
        return jsonify(succes = False), status.HTTP_400_BAD_REQUEST

    user.admin = True
    db.session.commit()
    return jsonify(success = True)


@app.route('/user/<public_id>', methods = ['DELETE'])
@token_required
def delete_user(current_user, public_id:str):
    '''deletes a user from the database'''

    if not current_user.admin:
        return jsonify({'message': 'Not authorized to do that'}), status.HTTP_401_UNAUTHORIZED

    user = User.query.filter_by(public_id = public_id).first()
    if not user:
         
        return jsonify(succes = False), status.HTTP_400_BAD_REQUEST

    db.session.delete(user)
    db.session.commit()

    return jsonify(success = True)


@app.route('/model/predict', methods = ['POST'])
@token_required

def predict(current_user):
    global model
    data = request.get_json()
    data = data['data']
    prediction  = model.predict(data)
    return prediction
    



if __name__ == '__main__':

    if not database_exists('sqlite:///ezml.db'):
        db.create_all()
        hashed_pwd = generate_password_hash('12345', method = 'sha256')
        new_user = User(public_id = str(uuid.uuid4()), name = 'admin', password = hashed_pwd, admin = True)
        db.session.add(new_user)
        db.session.commit()
    print(db.metadata.tables)
    app.run(debug=True)
