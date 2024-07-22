# logging_script.py
import os
import logging
import hashlib

# Configure logging
log_directory = 'data/logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(level=logging.INFO, filename=os.path.join(log_directory, 'auth.log'), filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Utility functions
def read_file(filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read().splitlines()
        return []
    except Exception as e:
        logging.error(f"Error reading file {filename}: {e}")
        return []

def write_file(filename, data):
    try:
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")
    except Exception as e:
        logging.error(f"Error writing file {filename}: {e}")

def authenticate_user(user_id, password):
    logging.info(f"Authenticating user: {user_id}")
    try:
        users = read_file('data/users.txt')
        for user in users:
            stored_user_id, stored_password_hash = user.split(',')
            input_password_hash = hashlib.sha256(password.encode()).hexdigest()
            if user_id == stored_user_id and input_password_hash == stored_password_hash:
                logging.info(f"Authentication successful for user: {user_id}")
                return True
        logging.warning(f"Authentication failed for user: {user_id}")
        return False
    except Exception as e:
        logging.error(f"Error in authenticate_user: {e}")
        return False

def register_user(user_id, password):
    logging.info(f"Registering user: {user_id}")
    try:
        users = read_file('data/users.txt')
        for user in users:
            stored_user_id, _ = user.split(',')
            if user_id == stored_user_id:
                logging.warning(f"User ID already exists: {user_id}")
                return False
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        users.append(f"{user_id},{password_hash}")
        write_file('data/users.txt', users)
        user_directory = os.path.join('data/db', user_id)
        os.makedirs(user_directory, exist_ok=True)
        logging.info(f"User registered successfully: {user_id}")
        return True
    except Exception as e:
        logging.error(f"Error in register_user: {e}")
        return False

def setup_logging():
    logging.basicConfig(filename='data/logs/app.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    logging.info("Starting authentication script")

    while True:
        choice = input("Enter 'login' to log in or 'register' to create a new account: ").strip().lower()
        if choice not in ('login', 'register'):
            print("Invalid choice. Please try again.")
            continue

        user_id = input("Enter user ID: ").strip()
        password = input("Enter password: ").strip()

        if choice == 'login':
            if authenticate_user(user_id, password):
                print("Login successful!")
                break
            else:
                print("Login failed. Please try again.")
        elif choice == 'register':
            if register_user(user_id, password):
                print("Registration successful! You can now log in.")
            else:
                print("Registration failed. User ID may already exist. Please try again.")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}")
