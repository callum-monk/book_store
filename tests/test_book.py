from lib.book import Book

def test_book_constructs():
    book = Book('Test Book', 'Test Author', 1)
    assert book.id == 1
    assert book.title == 'Test Book'
    assert book.author == 'Test Author'

def test_book_format_nicely():
    book = Book('Test Book', 'Test Author', 1)
    assert str(book) == 'Book(1, Test Book, Test Author)'

def test_books_are_equal():
    book1 = Book('Test Book', 'Test Author', 1)
    book2 = Book('Test Book', 'Test Author', 1)
    assert book1 == book2