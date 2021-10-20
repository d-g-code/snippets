"""
Repeating English 4.0
- coloring answer
- SQLite database
- added new words from file
- repeat mistook words once time
"""


from termcolor import colored
from functions_repeating_english_2 import create_connection, execute_read_query, execute_query, \
    create_table_repeating_word


connection = create_connection('/home/don/programming/snippets/python/Repeating English/repeating_english_2.db')
execute_query(connection, create_table_repeating_word)

# RESET VALUE repeat_correct_session
reset_value_repeat_correct_session = "UPDATE repeating_word SET repeat_correct_session=0"
execute_query(connection, reset_value_repeat_correct_session)

# SELECT repeating words
select_repeating_words = "SELECT * from repeating_word"
repeating_words = execute_read_query(connection, select_repeating_words)

# CREATE TABLE WITH WORDS, AND SET DEFAULT
# f = open('new_words', 'r')
# lines = f.readlines()
# for line in range(len(lines)):
#     row = lines[line]
#     cluster = row[0:-1].split()
#     new_word_eng = cluster[0]
#     new_word_pol = ' '.join(cluster[1:])
#     create_word = "INSERT INTO " \
#                   "repeating_word (word_eng, word_pol, amount_repeat, repeat_correct_session ) " \
#                   "VALUES ('{}', '{}', 0, 0)".format(new_word_eng, new_word_pol)
#     execute_query(connection, create_word)


def repeat(rw):
    for row in range(len(rw)):
        print(rw[row][2])
        user_answer = input()
        if user_answer == rw[row][1]:
            print(colored('GOOD', 'green'), '\n')
            modify_repeat_correct_session = "UPDATE repeating_word SET repeat_correct_session=1 WHERE id={}".format(
                row + 1)
            execute_query(connection, modify_repeat_correct_session)
        else:
            print(colored('BAD', 'red'))
            print(colored(rw[row][1], 'green'))
            print(colored(user_answer, 'blue'), '\n')


repeat(repeating_words)
rerun_words = "SELECT * FROM repeating_word WHERE repeat_correct_session=0"
print('Repeat mistake words')
repeat(execute_read_query(connection, rerun_words))

