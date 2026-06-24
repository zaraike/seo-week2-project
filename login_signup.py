"""
Allows for interactions with the database
Supports user sign up and log in
"""

import pandas as pd
import sqlalchemy as db
import sqlite3

# create user_info database
engine = db.create_engine("sqlite:///users.db")
conn = sqlite3.connect('users') # open connection to database
c = conn.cursor() # virtual pointer / control terminal within database

# initialize database
def init_db():
    conn = sqlite3.connect('users') # open connection to database
    c = conn.cursor() # virtual pointer / control terminal within database
    c.execute("CREATE TABLE IF NOT EXISTS login_info("
              "username VARCHAR(50) NOT NULL UNIQUE,"
              "password VARCHAR(255) NOT NULL"
              ")")
    

# insert new user
def sign_up(username, password):
    if not username or not password:
        print("ERROR: username and password cannot be empty")
        return False
    res = c.execute("SELECT password FROM login_info WHERE username = ?", (username,))
    if res.fetchone(): # if this user does not exist
        print("ERROR: user already exists")
        return False
    
    c.execute(" INSERT INTO login_info VALUES (?, ?)", 
              (username, password))
    conn.commit()
    print("user creation successful")
    return True

# allow user to log in
def log_in(username, password):
    if not username or not password:
        print("ERROR: username and password cannot be empty")
        return False
    res = c.execute("SELECT password FROM login_info WHERE username = ?", (username,))
    p = res.fetchone()
    if p == None: # if this user does not exist
        print("user does not exist")
        return False
    if p[0] != password:
        print("username and password does not match")
        return False

    print("logged in")
    return True

# print the database table, just used for debugging
def show_table():
    print()
    c.execute("SELECT * FROM login_info;")
    rows = c.fetchall()
    for r in rows:
        print(r)
    print()