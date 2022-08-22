import random
import itertools
# from re import T
# from tkinter import E
# (above) randomizer allows choosing one random word from dictionary (below)

# this referencing file doesnt work, but just working from the list down below does  
# reference txt file of words
#f = open(r'c:\repos\06-15E-Word-Guessing-Game\words2.txt')
#words = f.read()
#f.close()
 
dictionary = ['potato', 'apple', 'ferret', 'trombone', 'telephone', 'squirrel', 'elbow', 'hippopotamus', 'chicken', 'eclair']
 
# Function will choose one random word from the above dictionary
round_word = random.choice(dictionary)
 
#START
# print("----------------------------") 
# print("Let's play 'Guess That Word!'")
# print('You have 7 turns to guess the word.')
# print('Each time you guess incorrectly, you lose a turn.')
# print('If you get the whole word before you are out of turns, you win!')

#SET-UP
#probs dont need SET-UP after import
round_underscore_word = ['_']* len(round_word)
print(round_underscore_word) 
print('')
#BUT MAYBE NEED TO CHANGE LETTERS GUESSED TO NOT A LIST?
letters_guessed = []
#turns = 7
answer = round_word


#FUNCTIONS
def get_letter_position(letter, round_word, round_underscore_word):
    index = -2
    while index != -1:
        if letter in round_word:
            index = round_word.find(letter)
            removed_character ='*'
            round_word = round_word[:index]+removed_character+round_word[index+1:]
            round_underscore_word[index] = letter
        else:
            index = -1
     
    return (round_word, round_underscore_word)


def win_check():
    for i in range(0, len(round_underscore_word)):
        if round_underscore_word[i] == '_':
            return -1

    return 1

#USED TO BE: 'for i in range(1, len(round_word)+1):' THEN EVERYTHING ELSE WAS INDENTED BUT MAYBE THAT IS WHY IT WAS LIMITING HOW MANY TIME I COULD GUESS?
for i in itertools.count(start=1):
    letter = input('Guess a letter: ')
    # every input letter will be stored in letters_guessed
    #letters_guessed += letter + ', '
    letters_guessed.append(letter)
    print('')
    print("---------------------------------")
    print('Letters already guessed:{} \n'.format(letters_guessed))
    #print("You have guessed: " + letters_guessed)
    if letter in round_word:
        round_word, round_underscore_word = get_letter_position(letter, round_word, round_underscore_word)
        print(round_underscore_word)
    else:
        print('''Nope, not in this word.''') 
        # turns -= 1
        #print('you have '+str(turns)+' turns left.')
        print('')
        print(round_underscore_word)
     
    # if turns == 0:
    #     print("")
    #     print("You Lost! :'(")
    #     # this print the correct word
    #     print("The word was: " + answer + "!")
    #     break
    
    if win_check() == 1:
        print('Yay! You won!')
        # this print the correct word
        print("The word is: " + answer + "!")
        break
