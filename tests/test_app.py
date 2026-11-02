import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_get_index_returns_200():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_get_books_returns_200():
    client = app.test_client()
    response = client.get('/books')
    assert response.status_code == 200