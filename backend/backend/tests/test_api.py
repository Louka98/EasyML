from flask import json
from backend.api import app,db,User
from flask.wrappers import Response
from sqlalchemy.util.compat import b64encode
from sqlalchemy_utils import database_exists
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import os

def init():
    app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db')
    if not database_exists('sqlite:///test.db'):
        db.create_all()
        hashed_pwd = generate_password_hash('test_password', method = 'sha256')
        new_user = User(public_id = str(uuid.uuid4()), name = 'test_username', password = hashed_pwd, admin = True)
        db.session.add(new_user)
        hashed_pwd = generate_password_hash('test_password2', method = 'sha256')
        new_user = User(public_id = str(uuid.uuid4()), name = 'test_username2', password = hashed_pwd, admin = False)
        db.session.add(new_user)
        db.session.commit()

def clean_up():
    os.remove('test.db')

def login():
    credentials = b64encode(b"test_username:test_password")      
    response = app.test_client().get(
        '/login',
        content_type='application/json', headers={"Authorization": f"Basic {credentials}"}
    )
    return response

def login_not_admin():
    credentials = b64encode(b"test_username2:test_password2")      
    response = app.test_client().get(
        '/login',
        content_type='application/json', headers={"Authorization": f"Basic {credentials}"}
    )
    return response

def test_login():
    init()
    response = login()
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data['token']) != 0
    clean_up()

def test_register():
    init()
    credentials = b64encode(b"test_username3:test_password3")   #user not in the database yet 
    response = app.test_client().get(
        '/register',
        content_type='application/json', headers={"Authorization": f"Basic {credentials}"}
    )
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert len(data['token']) != 0
    clean_up()

def test_invalid_register():
    init()
    credentials = b64encode(b"test_username:test_password")     #user already in database
    response = app.test_client().get(
        '/register',
        content_type='application/json', headers={"Authorization": f"Basic {credentials}"}
    )
    assert response.status_code == 401
    data = json.loads(response.get_data(as_text=True))
    #in this case we do not get an authentication token back
    try: 
        data['token']
    except Exception as e:
        assert isinstance(e,KeyError)
    clean_up()

def test_get_all_users():
    init()
    response = login()
    data = json.loads(response.get_data(as_text=True))
    response = app.test_client().get(
        '/user',
        content_type='application/json', headers={"x-access-token": data['token']}
    )
    data = json.loads(response.get_data(as_text=True))
    assert len(data['users']) != 0 
    for u in data['users']:
        assert 'test_username' in u['name']
    clean_up()

def test_get_all_users_not_admin():
    init()
    response = login_not_admin()
    data = json.loads(response.get_data(as_text=True))
    response = app.test_client().get(
        '/user',
        content_type='application/json', headers={"x-access-token": data['token']}
    )
    response.status_code == 401
    clean_up()

def test_get_user():
    init()
    response = login()
    data = json.loads(response.get_data(as_text=True))
    response = app.test_client().get(
        '/user',
        content_type='application/json', headers={"x-access-token": data['token']}
    )
    users = json.loads(response.get_data(as_text=True))
    for u in users['users']:
        public_id = u['public_id']
        response = app.test_client().get(
        f'/user/{public_id}',
        content_type='application/json', headers={"x-access-token": data['token']})
        user = json.loads(response.get_data(as_text=True))
        print(user)
        assert 'test_user' in user['user']['name']
    clean_up()

def test_get_user_not_admin():
    init()
    response = login_not_admin()
    data = json.loads(response.get_data(as_text=True))
    
    public_id = 'random_id'
    response = app.test_client().get(
    f'/user/{public_id}',
    content_type='application/json', headers={"x-access-token": data['token']})
    assert response.status_code == 401
    clean_up()

def test_train():
    init()
    response = login()
    data = json.loads(response.get_data(as_text=True))

    payload = "{\"dataset\":[[\"100\",\"120\",\"1\",\"1\"],[\"1\",\"0\",\"1\",\"1\"],[\"0\",\"1\",\"1\",\"1\"],[\"0\",\"0\",\"0\",\"0\"],[\"0\",\"1\",\"0\",\"0\"]],\"target_column\":3,\"labels_included\":false,\"model_type\" : \"nn_custom\",\"layers\" : [10,7,5,1],\"act_func\": \"sigmoid\", \"hidden_act_func\": \"relu\", \"loss\" : \"binary_crossentropy\", \"batch_size\":3, \"epochs\": 10, \"early_stopping\":true, \"test_size\": 0.1 }"
    response = app.test_client().post(
        '/model/train',
        content_type='application/json', headers={"x-access-token": data['token']}, data = payload
    )
    assert response.status_code == 200
    data = json.loads(response.get_data(as_text=True))
    assert len(data['loss']) !=0
    clean_up()