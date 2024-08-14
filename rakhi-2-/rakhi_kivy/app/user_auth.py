# user_auth.py:
import os
import hashlib
import logging

logging.basicConfig(level=logging.INFO, filename='data/log/app.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

USER_DB_FILE = 'data/db/users.txt'


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def read_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, 'r') as f:
        users = {}
        for line in f:
            username, hashed_password = line.strip().split(',')
            users[username] = hashed_password
        return users


def write_users(users):
    with open(USER_DB_FILE, 'w') as f:
        for username, hashed_password in users.items():
            f.write(f"{username},{hashed_password}\n")


def register_user(username, password):
    users = read_users()
    if username in users:
        logging.error(f"Attempt to register already existing user: {username}")
        return False, "Username already exists."
    users[username] = hash_password(password)
    write_users(users)
    logging.info(f"User registered successfully: {username}")
    return True, "User registered successfully."


def login_user(username, password):
    users = read_users()
    if username in users and users[username] == hash_password(password):
        logging.info(f"User logged in successfully: {username}")
        return True, "Login successful."
    logging.error(f"Failed login attempt for user: {username}")
    return False, "Invalid username or password."
