import bcrypt

# Encrypt password passed
def hash_pw(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)

    return hash.decode('utf-8')

# Return true or false if input pw == hashed pw
def check_pw(pw_input, hashed_pw):
    input_bytes = pw_input.encode('utf-8')
    bytes = hashed_pw.encode('utf-8')

    return bcrypt.checkpw(input_bytes, bytes)
