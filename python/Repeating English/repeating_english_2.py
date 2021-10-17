"""
Repeating English 2.0
- coloring answer
- SQLite database
"""

# https://realpython.com/python-sql-libraries/#creating-tables

from termcolor import colored
from functions_repeating_english_2 import create_connection, execute_read_query


connection = create_connection('/home/don/programming/snippets/python/Repeating English/repeating_english_2.db')


select_repeating_words = "SELECT * from repeating_word"
repeating_words = execute_read_query(connection, select_repeating_words)

for row in range(len(repeating_words)):
    print(repeating_words[row][2])
    user_answer = input()
    if user_answer == repeating_words[row][1]:
        print(colored('GOOD', 'green'), '\n')
    else:
        print(colored('BAD', 'red'))
        print(colored(repeating_words[row][1], 'green'))
        print(colored(user_answer, 'blue'), '\n')
