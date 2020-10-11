from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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


if __name__ == '__main__':
    app.run(debug=True)
