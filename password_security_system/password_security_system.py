import re
import hashlib
from datetime import datetime


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def is_strong_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    if not re.search(r'[A-Z]', password):
        return False, "Password must include at least one uppercase letter."

    if not re.search(r'[0-9]', password):
        return False, "Password must include at least one number."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must include at least one special symbol."

    return True, "Password is strong."


def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("audit_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {event}\n")


def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    is_valid, feedback = is_strong_password(password)

    if not is_valid:
        print(feedback)
        log_event(f"Registration failed for user {username}")
        return

    hashed_password = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(f"{username}:{hashed_password}\n")

    print("User registered successfully.")
    log_event(f"{username} successfully registered")


def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open("users.txt", "r") as file:
            users = file.readlines()

    except FileNotFoundError:
        print("No users are registered yet.")
        return

    for user in users:
        stored_username, stored_password = user.strip().split(":")

        if username == stored_username and hash_password(password) == stored_password:
            print("Login successful.")
            log_event(f"{username} successfully logged in")
            post_login_menu(username)
            return

    print("Invalid username or password.")
    log_event(f"Failed login attempt for user {username}")


def view_logs(username):
    print(f"\nLogs for user '{username}'")

    try:
        with open("audit_log.txt", "r") as log_file:
            logs = log_file.readlines()

    except FileNotFoundError:
        print("No logs found.")
        return

    user_logs = [log.strip() for log in logs if username in log]

    if user_logs:
        for log in user_logs:
            print(log)
    else:
        print("No logs were found for your account.")


def post_login_menu(username):
    while True:
        print("\nPost-Login Menu")
        print("1. View my logs")
        print("2. Logout")

        choice = input("What would you like to do? ")

        if choice == "1":
            view_logs(username)

        elif choice == "2":
            log_event(f"{username} logged out")
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\nWelcome to the User Registration System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("What would you like to do? ")

        if choice == "1":
            register_user()

        elif choice == "2":
            login_user()

        elif choice == "3":
            log_event("System exit")
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")


main()