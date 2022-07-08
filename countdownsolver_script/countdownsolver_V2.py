from english_words import english_words_lower_alpha_set

letters = []
actual_dictionary = english_words_lower_alpha_set
list_of_correct_answers = []

def collect_player_letters():
    for z in range(1,10):
        letters.append(input(f'\nPlease enter letter {z}:\n'))
    return letters

def countdown_solver():
    for dict_word in actual_dictionary:
        correct_answer = [] 
        player_letters = user_letters.copy()
        for letter in dict_word:
            if letter in player_letters:
                correct_answer.append(letter)
                player_letters.remove(letter)
        correct_answer = ''.join(correct_answer) 
        if (correct_answer in actual_dictionary) and\
            (correct_answer not in list_of_correct_answers):
                list_of_correct_answers.append(correct_answer)
    
    return list_of_correct_answers

def sort_answers():
    for y in range(6,9):
        print(f"\nHere are the {y} letter words:\n")
        for x in list_of_correct_answers:
            if len(x) == y:
                print(x)


user_letters = collect_player_letters()
list_of_correct_answers = countdown_solver()
sort_answers()