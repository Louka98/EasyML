from flask import json
from backend.api import app

def test_login():
    headers = {
    'Content-Type': 'application/json',
    'x-access-token': '',
    'Authorization': 'Basic YWRtaW46MTIzNDU='
    }        
    response = app.test_client().get(
        '/login',
        data=json.dumps({'name': 'admin', 'password': '12345'}),
        content_type='application/json', headers = headers
    )

    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(data['token']) != 0

