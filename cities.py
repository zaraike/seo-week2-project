"""City storafe functions for the Weather Watchlist app."""

import sqlite3

DB_NAME = "users"


def get_connection():
    """Open a connections to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def create_cities_table():
    """Create the cities table if it does not exist."""
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS cities("
        "username VARCHAR(50) NOT NULL,"
        "city_name VARCHAR(100) NOT NULL"
        ")"
    )
    conn.commit()
    conn.close()


def add_city(username, city):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO cities VALUES (?, ?)",
        (username, city),
    )
    conn.commit()
    conn.close()


def get_cities(username):
    conn = get_connection()
    c = conn.cursor()
    res = c.execute(
        "SELECT city_name FROM cities WHERE username = ?",
        (username,),
    )
    rows = res.fetchall()
    conn.close()
    cities = []
    for row in rows:
        cities.append(row[0])
    return cities


def delete_city(username, city):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "DELETE FROM cities WHERE username = ? AND city_name = ?",
        (username, city),
    )
    conn.commit()
    conn.close()
