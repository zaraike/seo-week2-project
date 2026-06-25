"""
Allows for interactions with the database
Supports user sign up and log in
"""

import pandas as pd
import sqlalchemy as db
import sqlite3

# create user accounts database
engine = db.create_engine("sqlite:///users.db")
conn = sqlite3.connect('users')     # open connection to database
c = conn.cursor()    # virtual pointer / control terminal within database


def init_db():
    """initialize account database"""

    c.execute("CREATE TABLE IF NOT EXISTS login_info("
              "username VARCHAR(50) NOT NULL UNIQUE,"
              "password VARCHAR(255) NOT NULL"
              ")")


def sign_up(username, password):
    """inserts new user into the database"""

    if not username or not password:
        print("[31m✗[0m username and password cannot be empty")
        return False
    res = c.execute("SELECT password FROM login_info WHERE username = ?",
                    (username,))
    if res.fetchone():
        print("[31m✗[0m user already exists")
        return False

    c.execute(" INSERT INTO login_info VALUES (?, ?)",
              (username, password))
    conn.commit()
    print("[32m✓[0m user creation successful")
    return True


def log_in(username, password):
    """allows user to log into application"""

    if not username or not password:
        print("[31m✗[0m username and password cannot be empty")
        return False
    res = c.execute("SELECT password FROM login_info WHERE username = ?",
                    (username,))
    p = res.fetchone()
    if p is None:   # if this user does not exist
        print("[31m✗[0m user does not exist")
        return False
    if p[0] != password:
        print("[31m✗[0m username and password does not match")
        return False

    print("[32m✓[0m Successfully logged in")
    return True


def show_table():
    """prints database table, only used for debugging"""

    print()
    c.execute("SELECT * FROM login_info;")
    rows = c.fetchall()
    for r in rows:
        print(r)
    print()
