from flask import json
from backend.api import app,db,User
from sqlalchemy.util.compat import b64encode
from sqlalchemy_utils import database_exists
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

def init():
    app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db')
    if not database_exists('sqlite:///test.db'):
        db.create_all()
        hashed_pwd = generate_password_hash('test_password', method = 'sha256')
        new_user = User(public_id = str(uuid.uuid4()), name = 'test_username', password = hashed_pwd, admin = True)
        db.session.add(new_user)
        db.session.commit()


def test_login():
    init()
    credentials = b64encode(b"test_username:test_password")      
    response = app.test_client().get(
        '/login',
        content_type='application/json', headers={"Authorization": f"Basic {credentials}"}
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data['token']) != 0
