from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)',
                                 [user.username, user.password]
                                 )
        return None

    def find_by_username(self, username):
        users_details = self._connection.execute(
            'SELECT * FROM users WHERE username = %s', [username]
        )

        if not users_details:
            return None

        details = users_details[0]
        return User(details["username"], details["password"], details["id"])