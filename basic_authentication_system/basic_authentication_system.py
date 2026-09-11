# Store usernames and passwords while the program is running.
user_credentials = {}
def register_user():
    username= input("ENTER YOUR USER NAME :")
    if username in user_credentials:
       print("Username already exists. Please choose a different username.")
    else:
        passowrd=input("ENTER YOUR PASSWORD")
        user_credentials[username]=passowrd
        print("Registration successful!")

def login_user():
    username = input("ENTER YOUR USER NAME: ")
    password = input("ENTER YOUR PASSWORD: ")
    if username in user_credentials and user_credentials[username] == password:
        print("Welcome back!")
    else:
        print("Invalid username or password.")

def authentication_system():
    # Keep showing the menu until the user chooses to exit.
    while True:
        print("\nBasic Authentication System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Enter your choice: ")
        if option == "1":
            register_user()

        elif option == "2":
            login_user()

        elif option == "3":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
        



if __name__ == "__main__":
    authentication_system()