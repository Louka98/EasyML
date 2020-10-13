from flask import Flask, request, jsonify
from flask import json
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfdgd123'  #to use token encoding
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ezml.db'

db = SQLAlchemy(app)  #database

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


@app.route('/user', methods = ['GET'])
def get_all_users():
    '''returns all users from the databse'''
    users = User.query.all()
    users = [user.as_dict() for user in users] 
    
    return jsonify({'users' : users})


@app.route('/user/<user_id>', methods = ['GET'])
def get_user():
    '''return one user specified by the user id'''
    
    return ''


@app.route('/user', methods = ['POST'])
def create_user():
    '''create a user from json containing the name and password'''
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


@app.route('/user/<user_id>', methods = ['PUT'])
def promote_user():
    '''promotes any user to admin'''
    
    return ''


@app.route('/user/<user_id>', methods = ['DELETE'])
def delete_user():
    
    return ''

if __name__ == '__main__':
    app.run(debug=True)
