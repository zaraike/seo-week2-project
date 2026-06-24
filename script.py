"""
Runs the login scripts
"""

from login_signup import *

# menu that runs once user starts up weather app
def start_menu():
    init_db()
    #show_table()
    action = ""
    while action.lower() not in  ('a', 'b'):
        action: str = input("\x1b[0mWelcome to the Weather App! Would you like to...\nA. Login\nB. Sign Up\n\n>>> \x1b[0;1;3;35m")

    username = input("\x1b[0mUsername: \x1b[0;1;3;35m")
    password = input("\x1b[0mPassword: \x1b[0;1;3;35m")

    if (action == 'b'):
        print("\x1b[0msigning up...")
        while(not sign_up(username, password)):
            print("try again\n")
            username = input("\x1b[0mUsername: \x1b[0;1;3;35m")
            password = input("\x1b[0mPassword: \x1b[0;1;3;35m")
            print("\x1b[0msigning up...")

        #show_table()

    print("logging in...")
    while(not log_in(username, password)):
        print("try again\n")
        username = input("\x1b[0mUsername: \x1b[0;1;3;35m")
        password: str = input("\x1b[0mPassword: \x1b[0;1;3;35m")
        print("\x1b[0mlogging in...")


def main():
    start_menu()




if __name__ == "__main__":
    main()