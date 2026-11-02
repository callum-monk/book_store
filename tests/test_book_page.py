from playwright.sync_api import Page, expect

def test_book_list(page: Page, db_connection):
    db_connection.seed('seeds/book_store.sql')
    page.goto("http://localhost:5001/books")

    books = page.locator('li')

    expected_books = [
      'The Gruffalo by Julia Donaldson',
      'Ada Twist, Scientist by Andrea Beaty',
      'The Girl Who Drank the Moon by Kelly Barnhill',
      'Dragons in a Bag by Zetta Elliott'
    ]

    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_form_input(page: Page):
    page.goto("http://localhost:5001/books")

    page.get_by_placeholder("Title").fill("The Chroicles of Geronimo (the cat)")
    page.get_by_placeholder("Author").fill("Geronimo")

    page.get_by_role("button", name="Submit").click()
    books = page.locator('li')
    new_book = books.all_inner_texts()[-1]

    assert new_book == "The Chroicles of Geronimo (the cat) by Geronimo"
