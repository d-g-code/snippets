"""
Repeating English 3.0
- coloring answer
- SQLite database
- added new words from file
"""


from termcolor import colored
from functions_repeating_english_2 import create_connection, execute_read_query, execute_query


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

f = open('new_words', 'r')
lines = f.readlines()
for line in range(len(lines)):
    row = lines[line]
    cluster = row[0:-1].split()
    new_word_eng = cluster[0]
    new_word_pol = ' '.join(cluster[1:])
    create_word = "INSERT INTO " \
                  "repeating_word (word_eng, word_pol, amount_repeat) " \
                  "VALUES ('{}', '{}', 0)".format(new_word_eng, new_word_pol)
    execute_query(connection, create_word)
