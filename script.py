"""
Runs the login scripts
"""

from login_signup import init_db, sign_up, log_in
from cities import create_cities_table, add_city, get_cities, delete_city
from weather import get_weather, get_tip


# menu that runs once user starts up weather app
def start_menu():
    init_db()
    create_cities_table()
    # show_table()
    action = ""
    while action.lower() not in ("a", "b"):
        action: str = input(
            "\x1b[0mWelcome to the Weather App!"
            " Would you like to...\n"
            "A. Login\nB. Sign Up\n\n>>> \x1b[0;1;3;35m"
        )

    username = input("\x1b[0mUsername: \x1b[0;1;3;35m")
    password = input("\x1b[0mPassword: \x1b[0;1;3;35m")

    if action == "b":
        print("\x1b[0msigning up...")
        while not sign_up(username, password):
            print("try again\n")
            username = input("\x1b[0mUsername: \x1b[0;1;3;35m")
            password = input("\x1b[0mPassword: \x1b[0;1;3;35m")
            print("\x1b[0msigning up...")

        # show_table()

    print("logging in...")
    while not log_in(username, password):
        print("try again\n")
        username = input("\x1b[0mUsername: \x1b[0;1;3;35m")
        password: str = input("\x1b[0mPassword: \x1b[0;1;3;35m")
        print("\x1b[0mlogging in...")

    weather_menu(username)


def weather_menu(username):
    while True:
        print("\x1b[0m")
        print("Weather Watchlist")
        print("1. Add a city")
        print("2. View my cities")
        print("3. Remove a city")
        print("4. Log out")
        choice = input(">>> ")

        if choice == "1":
            city = input("City name: ")
            add_city(username, city)
            print(city + " added.")
        elif choice == "2":
            cities = get_cities(username)
            if not cities:
                print("No cities saved yet.")
            else:
                for city in cities:
                    weather = get_weather(city)
                    if weather is None:
                        print(city + ": could not load weather.")
                    else:
                        tip = get_tip(weather)
                        print(
                            city
                            + ": "
                            + str(weather["temp"])
                            + "F, "
                            + weather["condition"]
                        )
                        print(" Tip: " + tip)
        elif choice == "3":
            city = input("City to remove: ")
            delete_city(username, city)
            print(city + " removed.")
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Pick 1, 2, 3, or 4.")


def main():
    start_menu()


if __name__ == "__main__":
    main()
