import sqlite3
from sqlite3 import Error


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print(sqlite3.version)
        print('Connection to SQLite DB successful')
    except Error as name_error:
        print(f"The error '{name_error}'")
    return conn


def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as error:
        print(f"The error '{error}'")


def execute_read_query(conn, query):
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as error:
        print(f"The error '{error}'")


# Queries
create_table_repeating_word = """
CREATE TABLE IF NOT EXISTS repeating_word (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word_eng TEXT NOT NULL,
    word_pol TEXT NOT NULL,
    amount_repeat INTEGER,
    repeat_correct_session INTEGER
);
"""
# execute_query(connection, create_table_repeating_word)
#
# create_word = """
# INSERT INTO
#     repeating_word (word_eng, word_pol, amount_repeat)
# VALUES
#     ('tree', 'drzewo', 0),
#     ('grass', 'trawa', 0)
# """
# execute_query(connection, create_word)
#
# update_word = """
# UPDATE
#     repeating_word
# SET
#     word_eng = 'coverage',
#     word_pol = 'zabezpieczenie, ubezpieczenie, polisa'
# WHERE
#     id = 3
# """
# execute_query(connection, update_word)
#
# # select all repeating words
# select_repeating_words = "SELECT * from repeating_word"
# repeating_words = execute_read_query(connection, select_repeating_words)
# print('All repeating words')
# for word in repeating_words:
#     print(word)
#
# # Update word
# select_word_to_update = "SELECT word_eng, word_pol FROM repeating_word WHERE id = 3"
# selected_word = execute_read_query(connection, select_word_to_update)
# print(selected_word)

# Delete
# delete_record = "DELETE FROM repeating_word WHERE id = 2"
# execute_query(connection, delete_record)
