import os
from flask import Flask, render_template, request, redirect
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.user_repository import UserRepository
from lib.user import User

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET'])
def get_all_books():
    connection = DatabaseConnection()
    connection.connect()

    book_repository = BookRepository(connection)
    books = book_repository.all()
    print(books)
    return render_template('books.html', books=books)

@app.route('/books', methods=['POST'])
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

if __name__ == '__main__':
    APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
    app.run(host=APP_HOST, port=5001, debug=True)
    