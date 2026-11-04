import os
from flask import Flask, render_template, request, redirect, session
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user_repository import UserRepository
from lib.user import User
from functools import wraps


app = Flask(__name__)
app.secret_key = 'some_really_secret_key'


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect('/sessions/new')
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()

    book_repository = BookRepository(connection)
    books = book_repository.all()
    return render_template('books.html', books=books)


@app.route('/books', methods=['POST'])
@login_required
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)

    book_details = request.form
    book = Book(title=book_details['title'], author=book_details['author'])
    book_repository.create(book)

    return redirect('/books', code=302)


@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template('signup_form.html')


@app.route('/users', methods=['POST'])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    user_details = request.form
    user = User(username=user_details['username'], password=user_details['password'])
    user_repository.create(user)

    return redirect('/books', code=302)


@app.route('/sessions/new', methods=['GET'])
def get_login_form():
    return render_template('login_form.html')


@app.route('/sessions', methods=['POST'])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)

    username = request.form["username"]
    password = request.form["password"]

    user = user_repository.find_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")

if __name__ == '__main__':
    APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
    app.run(host=APP_HOST, port=5001, debug=True)
    