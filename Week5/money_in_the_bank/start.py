import sql_manager
import getpass
from datetime import datetime


def main_menu():
    print(
        "Welcome to our bank service. You are not logged in. \nPlease register or login")
    sql_manager.start_protection()
    print(datetime.now())

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            check_password(username, password)
            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            if sql_manager.cooldown(username) > 5:
                password = getpass.getpass("Enter your password: ")
                logged_user = sql_manager.login(username, password)

                if logged_user:
                    logged_menu(logged_user)
                else:
                    print("Login failed")
                    sql_manager.update_protection(username)
            else:
                print(" Please try again in less {} minutes!".format(int(6 - sql_manager.cooldown(username) // 1)))

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def check_password(username, password):
    if not any(x.isupper() for x in password):
        password = getpass.getpass(
            "Your password should have at least one upper case character:")
        check_password(username, password)
    elif not any(x.islower() for x in password):
        password = getpass.getpass(
            "Your password should have at least one lower case character:")
        check_password(username, password)
    elif not any(x.isdigit() for x in password):
        password = getpass.getpass("Your password should have at least one digit:")
        check_password(username, password)
    elif len(password) < 8:
        password = getpass.getpass("Your password should be at least 8 characters:")
        check_password(username, password)
    elif username in password:
        password = getpass.getpass("Your password should not contain your username:")
        check_password(username, password)

# def check_username(username):
# cursor =
    # cursor.execute("SELECT username FROM clients WHERE")
# make the username UNIQUE and catch the error from the sql query


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
