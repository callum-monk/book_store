from lib.pw_encryption import hash_pw, check_pw

def test_hashing_a_password():
    password = "test123"
    stored_hash = hash_pw(password)

    assert stored_hash != password

def test_hashed_password_check():
    password = "test456"
    stored_hash = hash_pw('test456')

    assert check_pw(password, stored_hash) == True

def test_password_check_failure():
    password = "test789"
    stored_hash = hash_pw("test456")

    assert check_pw(password, stored_hash) == False
    