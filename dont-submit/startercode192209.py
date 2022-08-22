#=======IMPORTS FROM CONFIG.PY===========
from config import dictionary_loc
from config import turn_text_loc
from config import wheel_text_loc
from config import max_rounds
from config import vowel_cost
from config import round_status_loc
from config import final_prize
from config import final_round_text_loc

import random
import time
import config

#==========ROUND BANK AND TOTAL BANK===========
players={0:{"round_total":0,"game_total":0,"name":""},
         1:{"round_total":0,"game_total":0,"name":""},
         2:{"round_total":0,"game_total":0,"name":""},
        }

#===========VARIABLES DEFINED============
#1, 2, or final
round_num = 0
#word choices
dictionary = [] 
#not sure what 'turn text' is
turn_text = ""
#what's on the wheel
wheel_list = []
round_word = []
round_underscore_word = []
vowels = {"a", "e", "i", "o", "u"}
round_status = ""
final_round_text = ""

#==============FUNCTIONS===================
def read_dictionary_file():
    global dictionary
    # Read dictionary file in from dictionary file location SUCCESS
    # Store each word in a list. = my_dictionary SUCCESS
    my_dictionary = getattr(config, 'dictionary_loc', 'no_dictionary_found')
    print(f'my_dictionary = {my_dictionary}')

def read_wheel_txt_file():
    global my_wheel_data
    # read the Wheel name from input using the Config wheel_loc file location SUCCESS
    my_wheel_data = getattr(config, 'wheel_text_loc', 'no_wheel_data_found' )
    print(f'my_wheel_data = {my_wheel_data}')  
          
##idk IF I AM GOING TO READ IN THESE FILES?
# def read_turn_txt_file(): 
#     global turn_text   
#     #read in turn intial turn status "message" from file

        
# def read_final_round_txt_file():
#     global final_round_text   
#     #read in turn intial turn status "message" from file

# def read_round_status_txt_file():
#     global round_status
#     # read the round status  the Config round_status_loc file location 

    
# def get_player_info():
#     global players
#     # read in player names from command prompt input


def game_setup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turn_text
    global dictionary
        
    read_dictionary_file()
    read_wheel_txt_file()

##IDK IF I ACTUALLY NEED THESE
    # read_turn_txt_file()
    # get_player_info()
    # read_round_status_txt_file()
    # read_final_round_txt_file() 
    
def get_word():
    global dictionary
    #choose random word from dictionary SUCCESS
    round_word = random.choice(my_dictionary)

    #make a list of the word with underscores instead of letters. SUCCESS - IMPORT FROM WORD GAME REV01
    round_underscore_word = ['_']* len(round_word)

    return round_word, round_underscore_word

def wof_round_setup():
    global players
    global round_word
    global round_underscore_word
    # Return the starting player number (random) SUCCESS
    init_player = random.randint(1, 3)
    print('Our starting player will be Player {}'.format(init_player))

    # Set round total for each player = 0

    # Use get_word function to retrieve the round_word and the round_underscore_word (blank word)

    return init_player


def spin_wheel(player_num):
    global wheel_list
    global players
    global vowels
    # Get random value for wheel_list SUCCESS
    spin_result = random.choice(my_wheel_data)
    
    # Check for bankrupcy, and take action. if ==000 then bankrupcy
    if spin_result == 000:

    # Check for lose turn. elif == 999 lose a turn
    # Get amount from wheel if not lose turn or bankruptcy. else hold # as value
    # Ask user for letter guess. acceptable= bcdfghijklmnpqrstvwxyz. check if letter selected has been guessed - make list of previous guesses and check against that.
    # Use guess_letter function to see if guess is in word, and return count. If 
    # Change player round total if they guess right.     
    return still_in_turn


def guess_letter(letter, player_num): 
    global players
    global round_underscore_word
    # parameters:  take in a letter guess and player number
    # Change position of found letter in round_underscore_word to the letter instead of underscore 
    # return good_guess= true if it was a correct guess
    # return count of letters in word. 
    # ensure letter is a consonate.
    
    return good_guess, count

def buy_vowel(player_num):
    global players
    global vowels
    
    # Take in a player number
    # Ensure player has 250 for buying a vowel_cost
    # Use guess_letter function to see if the letter is in the file
    # Ensure letter is a vowel
    # If letter is in the file let good_guess = True
    
    return good_guess      
        
def guess_word(player_num):
    global players
    global round_underscore_word
    global round_word
    
    # Take in player number
    # Ask for input of the word and check if it is the same as word_guess
    # Fill in blank_list with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    return False
    
    
def wof_turn(player_num):  
    global round_word
    global round_underscore_word
    global turn_text
    global players

    # take in a player number. 
    # use the string.format method to output your status for the round
    # and Ask to (s)pin the wheel, (b)uy vowel, or g(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update round_total 
    
    still_in_turn = True
    while still_in_turn:
        
        # use the string.format method to output your status for the round
        # Get user input S for spin, B for buy a vowel, G for guess the word
                
        if(choice.strip().upper() == "S"):
            still_in_turn = spin_wheel(player_num)
        elif(choice.strip().upper() == "B"):
            still_in_turn = buy_vowel(player_num)
        elif(choice.upper() == "G"):
            still_in_turn = guess_word(player_num)
        else:
            print("Not a correct option")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wof_round():
    global players
    global round_word
    global round_underscore_word
    global round_status
    initPlayer = wof_round_setup()
    
    # Keep doing things in a round until the round is done (word is solved)
        # While still in the round keep rotating through players
        # Use the wof_turn fuction to dive into each players turn until their turn is done.
    
    # Print round_status with string.format, tell people the state of the round as you are leaving a round.

def wof_final_round():
    global round_word
    global round_underscore_word 
    global final_round_text
    winplayer = 0
    amount = 0
    
    # Find highest game_total player.  They are playing.
    # Print out instructions for that player and who the player is.
    # Use the get_word function to reset the round_word and the round_underscore_word ( word with the underscores)
    # Use the guess_letter function to check for {'R','S','T','L','N','E'}
    # Print out the current round_underscore_word  with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guess_letter function to see if they are in the word
    # Print out the current round_underscore_word  again
    # Remember guess_letter should fill in the letters with the positions in round_underscore_word 
    # Get user to guess word
    # If they do, add final_prize and game_total and print out that the player won 

def timer():
    for x in range(1, 5):
        print('You have {} seconds..'.format(5-x))
        time.sleep(x) # "Sleep" for x seconds
    print("Time's up!")

def main():
    game_setup()    

    for i in range(0,max_rounds):
        if i in [0,1]:
            wof_round()
        else:
            wof_final_round()

if __name__ == "__main__":
    main()
    
    
