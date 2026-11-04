import sys
import os

from app import app
from lib.database_connection import DatabaseConnection

def test_create_user_is_saved_to_database(db_connection):
    client = app.test_client()

    # DELETES EVERYTHING IN TABLE EXCLUDING RECORD NAMES
    db_connection.execute("TRUNCATE TABLE users;")

    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    assert response.status_code == 302
    
    result = db_connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    assert len(result) == 1
    assert result[0]['username'] == 'testuser'