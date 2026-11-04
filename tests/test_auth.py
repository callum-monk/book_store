from app import app
from playwright.sync_api import Page

def test_auth(page: Page, db_connection):
	db_connection.execute("TRUNCATE TABLE users;")
	db_connection.execute("INSERT INTO users (username, password) VALUES ('testuser', 'test123');")

	page.goto("http://localhost:5001/sessions/new")
	page.get_by_placeholder("Username").fill("testuser")
	page.get_by_placeholder("Password").fill("test123")
	page.get_by_role("button", name="Log-in").click()
	
	assert page.url == 'http://localhost:5001/books'

def test_auth_failure(page: Page, db_connection):
	db_connection.execute("TRUNCATE TABLE users;")

	page.goto("http://localhost:5001/sessions/new")
	page.get_by_placeholder("Username").fill("testuser")
	page.get_by_placeholder("Password").fill("test123")
	page.get_by_role("button", name="Log-in").click()

	assert page.url == "http://localhost:5001/sessions/new"

def test_unauth_user_creates_book(page: Page, db_connection):
	page.goto("http://localhost:5001/books")
	page.get_by_placeholder("Title").fill("Test Book")
	page.get_by_placeholder("Author").fill("Test Author")
	page.get_by_role("button", name="Submit").click()

	assert page.url == 'http://localhost:5001/sessions/new'

