import random
from re import S
import time
import config
import itertools

#=======IMPORTS FROM CONFIG.PY===========
from config import dictionary_loc
from config import turn_text_loc
from config import wheel_text_loc
from config import max_rounds
from config import vowel_cost
from config import round_status_loc
from config import final_prize
from config import final_round_text_loc


#2) WELCOME MESSAGE
def welcome_message():
    print("==============================\nWelcome to 'Wheel of Fortune!'\n==============================\n ")
#     time.sleep(2) # pause again for more dramatic effect!
#     print("Three players will compete in the game to make as much money they can while \nguessing letters that make up a word.\n ")
#     time.sleep(2) # pause again for more dramatic effect!
#     print("A random word will be selected and each letter is represented as '_' on the board.\n")
#     time.sleep(2) # pause again for more dramatic effect!
#     print("As letters are guessed, the '_' are replaced with the correctly guessed letter.\n " )
#     time.sleep(2) # pause again for more dramatic effect!
#     multi = """In addition to spinning the wheel to get select consonants and, if correct, win
# money, players can also pay $250 to select a vowel or end the game by correctly
# identifying the word on the board.
#  """ 
#     str(multi)
#     print(multi)
#     time.sleep(2) # pause again for more dramatic effect!
#     multi2 = """We will play two rounds with all three players. The player at the end of each of
# the first two rounds with the most money will be that round's winner.The winner
# with the most money will be selected for the Final Round, where they have the 
# chance to win this week's prize...
#  """
#     str(multi2) 
#     print(multi2)
#     time.sleep(2) # pause again for more dramatic effect!
#     print('$' + prize_money +'!!! \n ')
    round_num = 1
    wof_round_setup(round_num)

#==========ROUND BANK AND TOTAL BANK===========
players={0:{"round_total":0,"game_total":0,"name":""},
         1:{"round_total":0,"game_total":0,"name":""},
         2:{"round_total":0,"game_total":0,"name":""},
        }

#===========VARIABLES DEFINED============
#1, 2, or final
round_num = 1
#word choices
dictionary = ['potato', 'apple', 'ferret', 'trombone', 'telephone', 'squirrel', 'elbow', 'hippopotamus', 'chicken', 'eclair']
round_word = '' #try defining it here? No, then it doesnt change
raw_round_word = round_word
#split_round_word = list(round_word) #this worked for one round but not sure abot #2
split_round_word = [] #try saying it is a vairiable list here and defining it specifically in get_word()?
#round_underscore_word = ['_']* len(round_word) #this worked for one round but not sure abot #2
round_underscore_word = []
#not sure what 'turn text' is
turn_text = ""
#what's on the wheel
wheel_list = []
vowels = {"a", "e", "i", "o", "u"}
round_status = ""
final_round_text = ""
letters_guessed = []
prize_money = str(final_prize)
answer = round_word


#==============READ IN FILES===================
def read_dictionary_file():
    global dictionary
    # Read dictionary file in from dictionary file location SUCCESS
    # Store each word in a list. = my_dictionary SUCCESS
    # my_dictionary = [] #tried defining my_dictionary seperate from dictionary
    # my_dictionary = getattr(config, 'dictionary_loc', 'no_dictionary_found')
    # print (f'my_dictionary = {my_dictionary}')
    # return 
    # dictionary.append(my_dictionary) #tried adding this on when dictionary wasnt updating 

def read_wheel_txt_file():
    global my_wheel_data
    # read the Wheel name from input using the Config wheel_loc file location SUCCESS
    my_wheel_data = getattr(config, 'wheel_text_loc', 'no_wheel_data_found' )
    #print(f'my_wheel_data = {my_wheel_data}')  
          
def read_turn_txt_file(): 
    global turn_text   
    #read in turn intial turn status "message" from file

        
def read_final_round_txt_file():
    global final_round_text   
    #read in turn intial turn status "message" from file
    final_round_text = getattr(config, 'final_round_text_loc', 'no_final_round_text_found' )

def read_round_status_txt_file():
    global round_status
    # read the round status the Config round_status_loc file location 

    
# def get_player_info():
#     global players
#     # read in player names from command prompt input

#==============FUNCTIONS===================
#1) SET UP THE BACKSTAGE
def game_setup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turn_text
    global dictionary  
    read_dictionary_file()
    read_wheel_txt_file()
    read_turn_txt_file()
    read_final_round_txt_file() 
    read_round_status_txt_file()
    welcome_message()

##IDK IF I ACTUALLY NEED THESE
    
    # get_player_info()
    
def get_word():
    global dictionary
    global round_word
    global round_underscore_word
    global split_round_word
    global raw_round_word
    #choose random word from dictionary SUCCESS
    round_word = random.choice(dictionary) #try defining it in variables?
    raw_round_word = round_word
    #make a list of the word with underscores instead of letters. SUCCESS
    split_round_word = list(round_word)
    round_underscore_word = ['_']* len(round_word) # -- try moving it to defined variables?
    #print(round_underscore_word)
    return round_word, round_underscore_word, split_round_word
    

def wof_round_setup(round_num): #getting 1st player, get_word() word set up
    global players
    global round_word
    global round_underscore_word
    global init_player 
    #round_word.clear()
    letters_guessed.clear()

    # set first player probably here? # Return the starting player number (random) SUCCESS
    init_player = random.randint(1, 3)
    time.sleep(2) # pause again for more dramatic effect!
    print('\n=======================\nOur starting player will be Player {}\n=======================\n'.format(init_player))
    # time.sleep(3) # pause again for more dramatic effect!
    # #print('The word on the board is: ')
    # time.sleep(3) # pause again for more dramatic effect!
    # # Use get_word function to retrieve the round_word and the round_underscore_word (blank word)
    get_word() 
    # print(round_underscore_word)
    # print(round_word)
    # print('')
    # time.sleep(3) # pause again for more dramatic effect!
    player_num = init_player
    main(player_num, round_num, round_word)
   # Set round total for each player = 0

    return init_player, round_word, round_underscore_word
    #The Python return statement is a special statement that you can use inside a function or 
    # method to send the function’s result back to the caller. A return statement consists of the return keyword followed by an optional return value

def spin_wheel(player_num, round_num):
    global wheel_list
    global players
    global vowels
    # Get random value for wheel_list SUCCESS
    spin_result = random.choice(my_wheel_data)
    
    # Check for bankrupcy, and take action. if ==000 then bankrupcy
    my_spin = False
    while my_spin == False:
        # Get amount from wheel if not lose turn or bankruptcy. else hold # as value (result)
        result = spin_result
        if spin_result == '000':
            print('\n==========\nBANKRUPTCY! \n==========\n')
            wof_round(player_num, round_num)
            #round_total = 0 #TODO probably have to work on that somemore
            break
    # Check for lose turn. elif == 999 lose a turn
        elif spin_result == '999':
            print('\n==========\nLOSE A TURN!\n==========\n')
            wof_round(player_num, round_num)
            break
        else:
            print('You spun $' + spin_result + '\n')
            consonant_eval(player_num, round_num)
            my_spin = True

#counts occurances of letter 

def letter_count(player_num, round_word, letter):
    global strcount
    global counts
    count = 0
    for ele in round_word:
        if (ele == letter):
            counts = count + 1
            strcount =str(counts)
            #print_letter_count(player_num, round_word, letter) from when i was trying to get my line to print about how many letters
            return (counts, strcount)

# def print_letter_count(player_num, round_word, letter):
#     print('{} has occurred {} times'.format(letter, letter_count(round_word, letter)))
   

#MOVE BELOW TO THING BEFORE LETTER COUNT
    # print('{} has occurred {} times'.format(letter, letter_count(round_word, letter))) #moved print and wof_turn out of for statements
    # wof_turn(player_num)
    
        #return count #print and return were reversed before and it worked but system having a problem now
# PART OF EVALUATION TOOL FROM MY WORD GAME
def get_letter_position(letter, round_word, round_underscore_word ):
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

#try to smush this into final_guess_letters
# def get_final_letter_position(index, round_word, round_underscore_word):
#     index1 = -2
#     while index1 != -1:
#         if index == round_word:
#             index1 = round_word.find(index)
#             removed_character ='*'
#             round_word = round_word[:index1]+removed_character+round_word[index1+1:]
#             round_underscore_word[index1] = index
#         else:
#             index1 = -1
     
#     return (round_word, round_underscore_word)

def guess_letter(letter, player_num, round_num): # GENERAL defines if approved letter(consonant or vowel) is in the puzzle # parameters:  take in a letter guess and player number
    global round_word
    global round_underscore_word 
    global counts
    #global strcount
    strcount = ''
    
    for i in itertools.count(start=1):
        if letter in round_word:
            round_word, round_underscore_word = get_letter_position(letter, round_word, round_underscore_word)
            #print(round_underscore_word)
    
            if "_" not in round_underscore_word:
                print('\nYou got all the letters! You win this round!')
                round_num = round_num+1
                wof_round_setup(round_num)
                letter_count(player_num, round_word, letter)
                good_guess = True     # If letter is in the round_word let good_guess = True
                 
            elif "_" in round_underscore_word:
                print('\nGood guess!')
                letter_count(player_num, round_word, letter)
                #print('There are ' + count +'!')
                let_count = strcount
                print('There are {}'.format(let_count) + '!\n')
                #print('{} has occurred {} times'.format(letter, letter_count (round_word, letter))) 
                #print('{} has occurred' .format(letter, letter_count)) #moved print and wof_turn out of for statements
                #print('{} times' .format(round_word, letter)) tried to split it 
                wof_turn(player_num, round_num)
                break 
                #good_guess = True     # If letter is in the round_word let good_guess = True
            
        #if the letter is NOT in the word
        else:
            print("\n" + letter + " is incorrect. Next player's turn.")
            wof_round(player_num, round_num)    
        good_guess = True
     
#THIS IS THE GENERAL ONE BUT I THINK I CAN DO IT WITH THE FINAL BETTER THAN WHAT I DID BELOW    
def final_guess_letter(letter, player_num, round_word): # GENERAL defines if approved letter(consonant or vowel) is in the puzzle # parameters:  take in a letter guess and player number
    global round_underscore_word 
    
    #for i in itertools.count(start=1):
    if letter in round_word:
        round_word, round_underscore_word = get_letter_position(letter, round_word, round_underscore_word)
        return round_underscore_word

def consonant_eval(player_num, round_num): #choose and define if consonant is acceptable
    global players
    global round_underscore_word
    eval = False
    while eval == False:
        consonant = input('Choose a consonant: ')
        #data validation
        #gotta be alpha
        if consonant.isalpha() is False:
            print('Enter a letter!')
            continue 
        #no penalty for re-guesses
        elif consonant in letters_guessed:
            print ('That letter has already been choosen!')
            continue
        #if letter is vowel
        elif consonant in vowels:
            print('That is not a consonant!')
            continue 
        else:
        #append guess to guesses 
            letter = consonant
            letters_guessed.append(letter)
            eval = True
            #take letter to see if it is in the puzzle
            guess_letter(letter, player_num, round_num)

    
def buy_vowel(player_num, round_num): #buys, selects, and evaluates vowel   # Take in a player number
    global players
    global vowels
    # Ensure player has 250 for buying a vowel_cost
    #if player_round_bank >= 250: #TODO need to define player_round_bank
        #if yes, do you want to spend 250$
    decided = True
    while decided:
        response = input('would you like to buy a vowel for $250? [y/n]: ')
        if (response != 'y' and response != 'n'):
            print("Invalid response. Expected 'y' or 'n'.")
            continue
        #yes i want to buy a vowel
        elif response == 'y':
            eval = False
            while eval == False:
                vowel = input('Pick a vowel: ')
                #data validation
                #gotta be alpha
                if vowel.isalpha() is False:
                    print('Enter a letter!')
                    continue 
                #no penalty for re-guesses
                elif vowel in letters_guessed:
                    print ('That letter has already been choosen!')
                    continue
                # Ensure letter is a vowel
                elif vowel not in vowels:
                    print('That is not a vowel!')
                    continue 
                #append guess to guesses
                else:
                    letter = vowel
                    letters_guessed.append(letter)
                    eval = True
                    #take letter to see if it is in the puzzle
                    guess_letter(letter, player_num, round_num)
        #no i dont want to buy a vowel
        else:
            wof_turn(player_num, round_num)
#if do not have $250
# else:
#     print('You cannot afford a vowel right now!')
#     wof_turn(player_num, round_num)
      
def solve_puzzle(player_num, round_num):
    global players
    global round_underscore_word
    global round_word
    
    answer = input('What is the word? ')
    print(answer)
    print(raw_round_word)
    time.sleep(2) # pause again for more dramatic effect!
    if answer == raw_round_word: 
        
        print('\nCorrect! You win this round!')
        round_num = round_num+1
        wof_round_setup(round_num)
    else:
        print('\nWrong! That ends your turn.')
        wof_round(player_num, round_num)

    
    # Take in player number
    # Ask for input of the word and check if it is the same as word_guess
    # Fill in blank_list with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    return False
    
    
def wof_turn(player_num, round_num):  
    global round_word
    global round_underscore_word
    global turn_text
    global players

    # take in a player number. 
    print('==================================================')
    print('Letters already guessed:{} \n'.format(letters_guessed))
    print('Our word on the board is:')
    print('cheat: the word is * {}' .format(split_round_word))
    print('{} \n'.format(round_underscore_word))
    

    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or g(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update round_total 
    
    still_in_turn = True
    while still_in_turn:
        print('Player {}'.format(player_num) + ', what would you like to do?\n')
        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
        choice = input('Would you like to (S)pin, (B)uy a vowel, or (G)uess the word? [S/B/G]: ')        
        if(choice.strip().upper() == "S"):
            still_in_turn = spin_wheel(player_num, round_num)
        elif(choice.strip().upper() == "B"):
            still_in_turn = buy_vowel(player_num, round_num)
        elif(choice.upper() == "G"):
            still_in_turn = solve_puzzle(player_num, round_num)
        else:
            print("No! You need to enter S or B or G.\n")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wof_round(player_num, round_num):
    global players
    global round_word
    global round_underscore_word
    global round_status
    
    new_num = (player_num + 1)
    if new_num > 3:
        new_num = 1
    player_num = new_num
    wof_turn(player_num, round_num)
    
    # Keep doing things in a round until the round is done (word is solved)
        # While still in the round keep rotating through players
        # Use the wof_turn fuction to dive into each players turn until their turn is done.
    
    # Print round_status with string.format, tell people the state of the round as you are leaving a round.

# 472 intro, gives letters, asks for letters and 
def wof_final_round(player_num, round_num, round_word):
    global round_underscore_word 
    global final_round_text
    winplayer = 0
    amount = 0
    # TODO Find highest game_total player.  They are playing.
    print(final_round_text) # Print out instructions for that player and who the player is.SUCCESS
        
    letter = ('r')
    letters_guessed.append(letter)
    if len(letter) > 0:
        final_guess_letter(letter, player_num, round_word)

    letter = ('s')
    letters_guessed.append(letter)
    if len(letter) > 0:
        final_guess_letter(letter, player_num, round_word)

    letter = ('t')
    letters_guessed.append(letter)
    if len(letter) > 0:
        final_guess_letter(letter, player_num, round_word)

    letter = ('l')
    letters_guessed.append(letter)
    if len(letter) > 0:
        final_guess_letter(letter, player_num, round_word)

    letter = ('n')
    letters_guessed.append(letter)
    if len(letter) > 0:
        final_guess_letter(letter, player_num, round_word)
    
    letter = ('e')
    letters_guessed.append(letter)
    print(f'The letters: {letters_guessed}')
    print('')
    if len(letter) > 0:
        final_guess_letter(letter, player_num, round_word)
    print(f'The word: {round_underscore_word}')
    print('')
    # Gather 3 consonats and 1 vowel and use the guess_letter function to see if they are in the word
    ##THEN I WANT THE PLAYER TO APPEND THEIR 3 CONSONANTS AND 1 VOWEL TO final_letters
    letter = input('Choose one additional consonant: ')
    letters_guessed.append(letter)
    final_guess_letter(letter, player_num, round_word)
    letter = input('Choose another consonant: ')
    letters_guessed.append(letter)
    final_guess_letter(letter, player_num, round_word)
    letter = input('Choose one more consonant: ')
    letters_guessed.append(letter)
    final_guess_letter(letter, player_num, round_word)
    letter = input('And a vowel: ')
    letters_guessed.append(letter)
    final_guess_letter(letter, player_num, round_word)
    # Print out the current round_underscore_word  again
    print(f'The word: {round_underscore_word}')
    b = True #declare boolean so that code can be executed only if it is still True
    t1 = time.time()
    answer = input("The word is: ")
    t2 = time.time()
    t = t2 - t1
    if t > 5:
        print("You have run out of time!")
        b = False

    if b == True:

        if answer == raw_round_word: 
            
            print('\nCorrect! You win the GRAND PRIZE!')
            print('${}!!! \n'.format(prize_money))
            round_num=4
            main(player_num, round_num, round_word)

        else:
            print("\nWrong! Better luck next time!")
            round_num=4
            main(player_num, round_num, round_word)


def main(player_num, round_num, round_word):
    if round_num < max_rounds:
        print("Let's begin round {}... \n".format(round_num))
        time.sleep(2) # pause again for more dramatic effect!
        wof_turn(player_num, round_num)   

    elif round_num == max_rounds:
        print("Let's begin the Final Round...")
        time.sleep(2) # pause again for more dramatic effect!
        wof_final_round(player_num, round_num, round_word)
    
    else:
        print("Hope you enjoyed my game! Goodbye!")


if __name__ == "__main__":
    game_setup()   

    
    
