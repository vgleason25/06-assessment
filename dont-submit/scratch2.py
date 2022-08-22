
import config
import time 
# #READ IN WHEEL DATA SUCCESS! IMPORTED
# my_wheel_data = getattr(config, 'wheel_text_loc', 'no_wheel_data_found')
# print(f'my_wheel_data = {my_wheel_data}')

# # Given a phrase and a list of guessed letters, returns an obscured version
# # Example:
# guessed: ['L', 'B', 'E', 'R', 'N', 'P', 'K', 'X', 'Z']
# phrase:  "GLACIER NATIONAL PARK"
# #returns> "_L___ER N____N_L P_RK"
# def obscurePhrase(phrase, guessed):
#     rv = ''
#     for s in phrase:
#         if (s in LETTERS) and (s not in guessed):
#             rv = rv+'_'
#         else:
#             rv = rv+s
#     return rv
# print(rv)

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
final_letters = ['R','S','T','L','N','E']
# i=0
# while i < len(final_letters):
#     print(final_letters[i])
#     i=i+1

##Trying out the underscores
# round_word = ['a','p','p','l','e']
# round_underscore_word = ['_','_','_','_','_']
# i=0
# while i < len(final_letters):
#     i=i+1
#     if i in round_word:
#         #build list of positions of guessed letter(s) in the word SUCCESS
#         # Change position of found letter in round_underscore_word to the letter instead of underscore 
#         pos = [i for i in range(len(round_word)) if round_word.startswith(letter,i)]
#         for i in pos:
#             round_underscore_word = round_underscore_word[:i] + i + round_underscore_word[i+len(final_letters):]
#             print(round_underscore_word)    
# 
## MAKING SURE DICTIONARY READ IN WORKS        
# my_dictionary = [] 
# my_dictionary = getattr(config, 'dictionary_loc', 'no_dictionary_found')
# print(f'my_dictionary = {my_dictionary}') 
# #print(my_dictionary)

# #MOVING UP IN PLAYERS
# #COPY OVER FROM SEAN'S TOURNAMENT TRACKER
# participants = 6
# def view_participants(participants):
#     print_with_underline('View Participants')
#     # VALIDATE SLOT
#     slot = get_int_within_range(f'Starting slot #[1-{len(participants)}]:', 1, len(participants))
#     print_with_underline('Starting Slot: Participant')
#     for i in range(max(1,slot-5),min(len(participants)+1,slot+6)):
#     for i in range(max(1))
#         if participants[i-1] == None:
#             print(f'{i}: [Empty]\n')
#         else:
#             print(f'{i}: {participants[i-1]}\n')

# # def whose_turn()
# #     init_player 

# player_num = 3

# new_num = (player_num + 1)
# if new_num > 3:
#     new_num = 1
#     player_num = new_num 
#     print(player_num)

# #HERE IS THE LETTER COUNT WITHOUT DEFINED LETTER AND ROUND WORD - SUCCESS
# round_word = ['C', 'R', 'Y']
# letter = 'Y'

# def letter_count(round_word, letter):
#     count = 0
#     for ele in round_word:
#         if (ele == letter):
#             count = count + 1
                   
#     return count
# print('{} has occurred {} times'.format(letter, letter_count(round_word, letter))) 
 
# Driver Code
 # (letter, letter_count, defines which letter (round_word, letter) defines # of times

# #LETTER FINDER FROM MY WORD GUESSING GAME
# guess = 'c'
# word = ['C', 'R', 'Y']
# spaces = ['_']* len(word)
# print(spaces) 
# print('')

# round_word = ['C', 'R', 'Y']
# letter = 'Y'

# def get_letter_position(guess, word, spaces):
#     index = -2
#     while index != -1:
#         if guess in word:
#             index = word.find(guess)
#             removed_character ='*'
#             word = word[:index]+removed_character+word[index+1:]
#             spaces[index] = guess
#             print(spaces)
#             print(word)
            
#         else:
#             index = -1
# #    return (word, spaces)

##REMOVE ELEMENTS FROM LIST
# prime_numbers = [2, 3, 5, 7, 9, 11]
# print(prime_numbers)
# # remove all elements
# prime_numbers.clear()

# # Updated prime_numbers List
# print('List after clear():', prime_numbers)


# # Output: List after clear(): []

# #searching final word with given letters
# final_letters = ['c']
# round_word = ['c', 'r', 'y']
# def final_guess_letters(final_letters, round_word):# removed 'player_num' from () # defines if given and choosen letters are in the puzzle:
#     #copied from consanant eval #append guess to guesses 
#     index = 0
#     while index < len(final_letters):
#         element = final_letters[index]
#         print(len(element))
#         index += 1
        # if index in round_word:
        #     #build list of positions of guessed letter(s) in the word SUCCESS
        #     # Change position of found letter in round_underscore_word to the letter instead of underscore 
        #     round_word, round_underscore_word = get_letter_position(letter, round_word, round_underscore_word)
        #     #print(round_underscore_word)          
        #     if "_" not in round_underscore_word:
        #         print ('You spelled the whole word! You win!')
        #         # TODO get to winnings summary
        #         break #TODO probably dont want a break. break will end to the end of the while or for loop. probably want to go to round or game summary function or something 
        #     else:
        #         print(round_underscore_word)  
        
#final_guess_letters(final_letters, round_word)

b = True #declare boolean so that code can be executed only if it is still True
t1 = time.time()
answer = input("Answer: ")
t2 = time.time()
t = t2 - t1
if t > 5:
  print("You have run out of time!")
  b = False

if b == True:
  #Rest of code
