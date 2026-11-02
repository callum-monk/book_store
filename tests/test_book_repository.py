from lib.book_repository import BookRepository
from lib.book import Book

def test_get_all_records(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repository = BookRepository(db_connection)

    books = repository.all()

    assert books == [
        Book('The Gruffalo', 'Julia Donaldson', 1), 
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2), 
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3), 
        Book('Dragons in a Bag', 'Zetta Elliott', 4)
        ]

def test_create_record(db_connection):
    db_connection.seed('seeds/book_store.sql')
    repository = BookRepository(db_connection)

    repository.create(Book(title='Christmas Carol', author='Charles Dickens'))

    result = repository.all()
    assert result == [
        Book('The Gruffalo', 'Julia Donaldson', 1), 
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2), 
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3), 
        Book('Dragons in a Bag', 'Zetta Elliott', 4),
        Book('Christmas Carol', 'Charles Dickens', 5)
        ]