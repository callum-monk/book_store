import pytest
from lib.database_connection import DatabaseConnection

@pytest.fixture
def db_connection():
    connection = DatabaseConnection()
    connection.connect()
    return connection
