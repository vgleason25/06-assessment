import random
import time
import config


# #READ IN DICTIONARY SUCCESS! IMPORTED
# my_dictionary = getattr(config, 'dictionary_loc', 'no_dictionary_found' )
# print(f'my_dictionary = {my_dictionary}')

# # READING NEED TO HAPPEN IN THE WHEEL GAME FILE
# f = open('wheel_data.txt')
# wheel_text_loc =f.read().splitlines()
# f.close()
# print(wheel_text_loc)

#READ IN WHEEL DATA SUCCESS! IMPORTED
my_wheel_data = getattr(config, 'wheel_text_loc', 'no_wheel_data_found')
print(f'my_wheel_data = {my_wheel_data}')
print(my_wheel_data)

##GET A RANDOM WORD SUCCESS! IMPORTED
# round_word = random.choice(my_dictionary)
# print(round_word)

# #GET A RANDOM WHEEL VALUE SUCCESS! IMPORTED
spin_result = random.choice(my_wheel_data)
print(spin_result)

#CHECK THE SPIN FOR VALUE, BANKRUPTCY, LOSE A TURN
my_spin = False
while my_spin == False:
    # Get amount from wheel if not lose turn or bankruptcy. else hold # as value
    result = spin_result
    if spin_result == '000':
        print('You spun BANKRUPTCY!\nYour round bank is now $0.\nThis completes your turn.')
        round_total = 0 #TODO probably have to work on that somemore
        next_player_turn() # TODO define this
# Check for lose turn. elif == 999 lose a turn
    elif spin_result == '999':
        print('You spun LOSE A TURN!\nThis completes your turn.')
        next_player_turn() # TODO define this
    else:
        print('You spun $' + spin_result)
        my_spin = True


##ENTERED IN STARTED CODE IN VERSIONS FOR CONSONANT AND VOWEL
# # # Ask user for letter guess. check if letter selected has been guessed - make list of previous guesses and check against that.
#EVALUATING LETTER BASED ON SEAN'S EXAMPLE
eval = False
while eval == False:
        consonant = input('Choose a consonant: ')
        #data validation
        #gotta be alpha
        if consonant.isalpha() is False:
            print('Please enter a letter!')
            continue 
        #no penalty for re-guesses
        elif consonant in letters_guessed:
            print ('That letter has already been choosen!')
            continue
        #if letter is vowel
        elif consonant in vowels:
            print('Sorry, that is not a consonant')
            continue 
        else:
        #append guess to guesses 
            letter = consonant
            letters_guessed.append(letter)
            eval = True

# LETTER IN ROUND WORD SHOULD PROBABLY BE A FUNCTION SO IT CAN BE CALLED ON FOR LETTER GUESS AND VOWEL GUESS
def guess_letter(letter, player_num):
    if letter in round_word:
        #build list of positions of guessed letter(s) in the word SUCCESS
        pos = [i for i in range(len(round_word)) if round_word.startswith(letter,i)]
        for i in pos:
            round_underscore_word = round_underscore_word[:i] + letter + round_underscore_word[i+len(letter):]
        
        print(f'The word: {round_underscore_word}')
        if "_" not in round_underscore_word:
            print ('You got the last letter! You win!')
            wins += 1
            break #TODO probably dont want a break. break will end to the end of the while or for loop. probably want to go to round or game summary function or something 
    else:
        print(letter + " is incorrect. Next player's turn") #TODO see if I can say 'Player X's turn (whoever comes next)
        break #not break, it would be the next player function 

##GETTING LETTER INPUT AND CHECKING IF IT IS IN THE WORD FROM REV01 - gunna use seans instead 
# for i in range(1, 100):
#     guess = input('Guess a letter: ')

#     ## every input letter will be stored in guesses
#     guesses += guess + ', '
#     print("---------------------------------")
#     print("Letters guessed: " + guesses)
#     if guess in round_word:
#         round_word, spaces = get_letter_position(guess, round_word, spaces)
#         print(spaces)
#     else:
#         print('That is not correct.') 
#         print('Next player is up.')
#         print('')
#         print(spaces)
    
#     if win_check() == 1:
#         print('Yay! You won!')
#         # this print the correct word
#         print("The word is: " + answer + "!")
#         break

# #IMPORTED FROM WORD GAME REV01 NOT MODIFIED --- fill the spaces
# def get_letter_position(guess, word, spaces):
#     index = -2
#     while index != -1:
#         if guess in word:
#             index = word.find(guess)
#             removed_letter ='*'
#             word = word[:index]+removed_letter+word[index+1:]
#             spaces[index] = guess
#         else:
#             index = -1
     
#     return (word, spaces)

# #IMPORTED FROM WORD GAME REV01 NOT MODIFIED ---- was that the last letter?
# def win_check():
#     for i in range(0, len(spaces)):
#         if spaces[i] == '_':
#             return -1
     
#     return 1
        
# # Use guess_letter function to see if guess is in word, and return count. If 
# # Change player round total if they guess right.     
# return still_in_turn

##TEST TIMER SUCCESS! IMPORTED
# for x in range(1, 5):
#     print('You have {} seconds..'.format(5-x))
#     time.sleep(x) # "Sleep" for x seconds
# print("Time's up!")

# RETURNS A STRING REPRESENTING THE CURRENT STATE OF THE GAME - IMPORTED FROM end of block 4 on https://runestone.academy/ns/books/published/fopp/Inheritance/chapterProject.html
def showBoard(obscuredPhrase, guessed):
    return """
Phrase:   {}
Guessed:  {}""".format(obscuredPhrase, ', '.join(sorted(guessed)))

from tkinter import Y

# Given a phrase and a list of guessed letters, returns an obscured version  - IMPORTED FROM end of block 4 on https://runestone.academy/ns/books/published/fopp/Inheritance/chapterProject.html
# Example:
#     guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
#     phrase:  "GLACIER NATIONAL PARK"
#     returns> "_L___ER N____N_L P_RK"
def obscurePhrase(phrase, guessed):
    rv = ''
    for s in phrase:
        if (s in LETTERS) and (s not in guessed):
            rv = rv+'_'
        else:
            rv = rv+s
    return rv


## TRYING TO MAKE A LETTER COUNTER - COUNTS HOW MANY TIMES A SUCCESSFUL LETTER APPEARS IN WORD
# def countX(round_underscore_word, x):
#     x = letter 
#     count = 0
#     for ele in round_underscore_word:
#         if (ele == x):
#             count = count + 1
#     return count

# letter = 'y'
# round_underscore_word = ['_', '_', 'y']

# count = phrase.count(move) # returns an integer with how many times this letter appears
# if count > 0:
#     if count == 1:
#         print("There is one {}".format(move))
#     else:
#         print("There are {} {}'s".format(count, move))


#I THINK THIS IS THE MAGIC THAT FINDS IF THE LETTER IS IN THE WORD - FROM WORD FIND REV01
def get_letter_position(guess, word, spaces):
    index = -2
    while index != -1:
        if guess in word:
            index = word.find(guess)
            removed_character ='*'
            word = word[:index]+removed_character+word[index+1:]
            spaces[index] = guess
        else:
            index = -1
     
    return (word, spaces)


def win_check():
    for i in range(0, len(spaces)):
        if spaces[i] == '_':
            return -1

    return 1

##GETTING LETTER INPUT AND CHECKING IF IT IS IN THE WORD - FROM WORD FIND REV01
for i in range(1, 100):
    guess = input('Guess a letter: ')
    ## every input letter will be stored in guesses
    guesses += guess + ', '
    print("---------------------------------")
    print("Letters guessed: " + guesses)
    if guess in round_word:
        round_word, spaces = get_letter_position(guess, round_word, spaces)
        print(spaces)
    else:
        print('That is not correct.') 
        print('Next player is up.')
        print('')
        print(spaces)
    
    if win_check() == 1:
        print('Yay! You won!')
        # this print the correct word
        print("The word is: " + answer + "!")
        break