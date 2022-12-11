# This is a program that will solve a countdown letters round.
# This will give you the 5 or more lettered words from a series of numbers.

# The logic to work out what possible words are found from a set of 9 letters
# is done through a series of three for loops.

###

#TestTest

# Import statements and necessary variables set up prior.

from english_words import english_words_lower_alpha_set

letters = []
actual_dictionary = english_words_lower_alpha_set
list_of_correct_answers = []

###

# For Loop #1 - This is for storing all the users choice of letters into a list.

print("""\nHey there! Are you stuck with your Countdown game? Let me help!\n\n\
What are the letters in your round?""")

for z in range(1,10):
    letters.append(input(f'\nPlease enter letter {z}:\n'))

print(f'\nThese are your letters:\n{letters}\n')

# For Loop #2 - This is the business logic for solving the countdown puzzle.
# The result of this is a list variable will all the possible answers.

for dict_word in actual_dictionary:
    correct_answer = []
    player_letters = letters.copy()
    for letter in dict_word:
        if letter in player_letters:
            correct_answer.append(letter)
            player_letters.remove(letter)
    correct_answer = ''.join(correct_answer)
    if (correct_answer in actual_dictionary) and \
       (correct_answer not in list_of_correct_answers):
            list_of_correct_answers.append(correct_answer)

# For Loop #3 - Prints the potential words to the user. 

for y in range(6,9):
    print(f"\nHere are the {y} letter words:\n")
    for x in list_of_correct_answers:
        if len(x) == y:
            print(x)