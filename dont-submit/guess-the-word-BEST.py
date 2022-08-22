import random
from re import T
from tkinter import E
# (above) randomizer allows choosing one random word from a list of words (below)

# this referencing file doesnt work, but just working from the list down below does  
# reference txt file of words
#f = open(r'c:\repos\06-15E-Word-Guessing-Game\words2.txt')
#words = f.read()
#f.close()
 
words = ['potato', 'apple', 'ferret', 'trombone', 'telephone', 'squirrel', 'elbow', 'hippopotamus', 'chicken', 'eclair']
 
# Function will choose one random word from the above list of words
word = random.choice(words)
 
#START
print("----------------------------") 
print("Let's play 'Guess That Word!'")
print('You have 7 turns to guess the word.')
print('Each time you guess incorrectly, you lose a turn.')
print('If you get the whole word before you are out of turns, you win!')

#SET-UP
spaces = ['_']* len(word)
print(spaces) 
print('')

guesses = ''
turns = 7
answer = word


#FUNCTIONS
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


for i in range(1, len(word)+1):
    guess = input('Guess a letter: ')
    # every input letter will be stored in guesses
    guesses += guess + ', '
    print('')
    print("---------------------------------")
    print("You have guessed: " + guesses)
    if guess in word:
        word, spaces = get_letter_position(guess, word, spaces)
        print(spaces)
    else:
        print('''Nope, not in this word.''') 
        turns -= 1
        print('you have '+str(turns)+' turns left.')
        print('')
        print(spaces)
     
    if turns == 0:
        print("")
        print("You Lost! :'(")
        # this print the correct word
        print("The word was: " + answer + "!")
        break
    
    if win_check() == 1:
        print('Yay! You won!')
        # this print the correct word
        print("The word is: " + answer + "!")
        break
