from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = Book(row['title'], row['author'], row['id'])
            books.append(item)
        return books

    def create(self, book):
        # self._connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)', [book.title, book.author])
        self._connection.execute(f"INSERT INTO books (title, author) VALUES ('{book.title}', '{book.author}')") # UNPROTECTED - Vulnerable to SQL Injection
        return None
