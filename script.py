"""
Runs the login scripts
"""

from login_signup import init_db, sign_up, log_in
from cities import create_cities_table, add_city, get_cities, delete_city
from weather import get_weather, get_tip

start_text = """\n\n
\x1b[38;2;255;128;128m𝚠\x1b[0m\x1b[38;2;255;132;128m𝚎\x1b[0m\x1b[38;2;255;135;128m𝚕\x1b[0m\x1b[38;2;255;139;128m𝚌\x1b[0m\x1b[38;2;255;143;128m𝚘\x1b[0m\x1b[38;2;255;147;128m𝚖\x1b[0m\x1b[38;2;255;150;128m𝚎\x1b[0m\x1b[38;2;255;154;128m \x1b[0m\x1b[38;2;255;158;128m𝚝\x1b[0m\x1b[38;2;255;161;128m𝚘\x1b[0m\x1b[38;2;255;165;128m \x1b[0m\x1b[38;2;255;169;128m𝚝\x1b[0m\x1b[38;2;255;173;128m𝚑\x1b[0m\x1b[38;2;255;177;128m𝚎\x1b[0m

\x1b[38;2;255;227;128m⟦\x1b[0m\x1b[38;2;255;231;128m \x1b[0m\x1b[38;2;255;235;128mW\x1b[0m\x1b[38;2;255;239;128m \x1b[0m\x1b[38;2;255;243;128m⟧\x1b[0m\x1b[38;2;255;247;128m⟦\x1b[0m\x1b[38;2;255;251;128m \x1b[0m\x1b[38;2;255;255;128mE\x1b[0m\x1b[38;2;248;255;128m \x1b[0m\x1b[38;2;240;255;128m⟧\x1b[0m\x1b[38;2;233;255;128m⟦\x1b[0m\x1b[38;2;225;255;128m \x1b[0m\x1b[38;2;218;255;128mA\x1b[0m\x1b[38;2;210;255;128m \x1b[0m\x1b[38;2;203;255;128m⟧\x1b[0m\x1b[38;2;195;255;128m⟦\x1b[0m\x1b[38;2;188;255;128m \x1b[0m\x1b[38;2;180;255;128mT\x1b[0m\x1b[38;2;173;255;128m \x1b[0m\x1b[38;2;165;255;128m⟧\x1b[0m\x1b[38;2;158;255;128m⟦\x1b[0m\x1b[38;2;150;255;128m \x1b[0m\x1b[38;2;143;255;128mH\x1b[0m\x1b[38;2;135;255;128m \x1b[0m\x1b[38;2;128;255;128m⟧\x1b[0m\x1b[38;2;128;255;135m⟦\x1b[0m\x1b[38;2;128;255;143m \x1b[0m\x1b[38;2;128;255;150mE\x1b[0m\x1b[38;2;128;255;158m \x1b[0m\x1b[38;2;128;255;165m⟧\x1b[0m\x1b[38;2;128;255;173m⟦\x1b[0m\x1b[38;2;128;255;180m \x1b[0m\x1b[38;2;128;255;188mR\x1b[0m\x1b[38;2;128;255;195m \x1b[0m\x1b[38;2;128;255;203m⟧\x1b[0m
              \x1b[38;2;128;255;210m⟦\x1b[0m\x1b[38;2;128;255;218m \x1b[0m\x1b[38;2;128;255;225m \x1b[0m\x1b[38;2;128;255;233m \x1b[0m\x1b[38;2;128;255;240m⟧\x1b[0m
\x1b[38;2;128;255;248m⟦\x1b[0m\x1b[38;2;128;255;255m \x1b[0m\x1b[38;2;128;247;255mT\x1b[0m\x1b[38;2;128;239;255m \x1b[0m\x1b[38;2;128;231;255m⟧\x1b[0m\x1b[38;2;128;223;255m⟦\x1b[0m\x1b[38;2;128;215;255m \x1b[0m\x1b[38;2;128;207;255mR\x1b[0m\x1b[38;2;128;199;255m \x1b[0m\x1b[38;2;128;192;255m⟧\x1b[0m\x1b[38;2;128;184;255m⟦\x1b[0m\x1b[38;2;128;176;255m \x1b[0m\x1b[38;2;128;168;255mA\x1b[0m\x1b[38;2;128;160;255m \x1b[0m\x1b[38;2;128;152;255m⟧\x1b[0m\x1b[38;2;128;144;255m⟦\x1b[0m\x1b[38;2;128;136;255m \x1b[0m\x1b[38;2;128;128;255mC\x1b[0m\x1b[38;2;132;128;255m \x1b[0m\x1b[38;2;136;128;255m⟧\x1b[0m\x1b[38;2;140;128;255m⟦\x1b[0m\x1b[38;2;144;128;255m \x1b[0m\x1b[38;2;149;128;255mK\x1b[0m\x1b[38;2;153;128;255m \x1b[0m\x1b[38;2;157;128;255m⟧\x1b[0m\x1b[38;2;161;128;255m⟦\x1b[0m\x1b[38;2;165;128;255m \x1b[0m\x1b[38;2;169;128;255mE\x1b[0m\x1b[38;2;173;128;255m \x1b[0m\x1b[38;2;177;128;255m⟧\x1b[0m\x1b[38;2;182;128;255m⟦\x1b[0m\x1b[38;2;186;128;255m \x1b[0m\x1b[38;2;190;128;255mR\x1b[0m\x1b[38;2;194;128;255m \x1b[0m\x1b[38;2;198;128;255m⟧\x1b[0m

"""


def start_menu():
    """menu that runs once user starts up weather app"""

    init_db()
    create_cities_table()
    print(start_text)

    # login / signup loop
    while True:
        action = ""
        while action.lower() not in ("a", "b"):
            action: str = input(
                "\x1b[0m"
                "Would you like to...\n"
                "A. Login\nB. Sign Up\n\n>>> \x1b[0;1;0;35m"
            )
        print()
        username = input("\x1b[0mUsername: \x1b[0;1;0;35m")
        password = input("\x1b[0mPassword: \x1b[8;39;49m")
        print("\x1b[0m")

        if action == "b":
            print("\x1b[0msigning up...")
            if not sign_up(username, password):
                print("try again\n")
                continue

        print("logging in...")
        if not log_in(username, password):
            print("try again\n")
            continue
        else:
            print("\x1b[0m")
            break

    weather_menu(username)


def weather_menu(username):
    while True:
        print("\x1b[0m")
        print("\x1b[1;36m=== Weather Watchlist === \x1b[0m")
        print("1. Add a city")
        print("2. View my cities")
        print("3. Remove a city")
        print("4. Log out")
        choice = input(">>> \x1b[1m\x1b[38;2;255;100;128m")
        print("\x1b[0m", end='')

        if choice == "1":
            city = input("City name: \x1b[1m\x1b[38;2;255;100;128m")
            print("\x1b[0m")
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
