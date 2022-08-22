import random
import itertools

 
dictionary = ['potato', 'apple', 'ferret', 'trombone', 'telephone', 'squirrel', 'elbow', 'hippopotamus', 'chicken', 'eclair']
 
# Function will choose one random word from the above dictionary
round_word = random.choice(dictionary) #in def get_word():
print(round_word) #not neccessary 
 

#SET-UP
#probs dont need SET-UP after import
round_underscore_word = ['_']* len(round_word) #in def get_word():
print(round_underscore_word) 
print('')
letters_guessed = [] #in VARIABLES DEFINED
answer = round_word #in VARIABLES DEFINED


#UPDATE LETTER POSITION ##INPUT IN WOF
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

#DEFINE WIN CHECK
def win_check():
    for i in range(0, len(round_underscore_word)):
        if round_underscore_word[i] == '_':
            return -1

    return 1

#LETTER INPUT ##INPUT IN WOF
for i in itertools.count(start=1):
    letter = input('Guess a letter: ')
    # every input letter will be stored in letters_guessed
    letters_guessed.append(letter)
    print('')
    print("---------------------------------")
    print('Letters already guessed:{} \n'.format(letters_guessed))

#CHECKS IF LETTER IN WORD
    if letter in round_word:
        round_word, round_underscore_word = get_letter_position(letter, round_word, round_underscore_word)
        print(round_underscore_word)
    else:
        print('''Nope, not in this word.''') 
        # turns -= 1
        #print('you have '+str(turns)+' turns left.')
        print('')
        print(round_underscore_word)

#IF WIN CHECK   
    if win_check() == 1:
        print('Yay! You won!')
        # this print the correct word
        print("The word is: " + answer + "!")
        break
