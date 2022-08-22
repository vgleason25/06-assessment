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

def welcome_message():
    print("==============================\nWelcome to 'Wheel of Fortune!'\n==============================\n ")
    time.sleep(2) # pause again for more dramatic effect!
    print("Three players will compete in the game to make as much money they can while \nguessing letters that make up a word.\n ")
    time.sleep(2) # pause again for more dramatic effect!
    print("A random word will be selected and each letter is represented as '_' on the board.")
    time.sleep(2) # pause again for more dramatic effect!
    print("As letters are guessed, the '_' are replaced with the correctly guessed letter.\n " )
    time.sleep(2) # pause again for more dramatic effect!
    print("In addition to spinning the wheel to get select consonants and, if correct, win \nmoney, players can also pay $250 to select a vowel or end the game by correctly \nidentifying the word on the board. \n " )
    time.sleep(2) # pause again for more dramatic effect!
    print("We will play two rounds with all three players. The player at the end of each of \nthe first two rounds with the most money will be that round's winner.The winner \nwith the most money will be selected for the Final Round, where they have the \nchance to win this week's prize, $" 
    + prize_money + '!!!\n ')
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
vowels = {"a", "e", "i", "o", "u"}
round_status = ""
final_round_text = ""
letters_guessed = []
prize_money = str(final_prize)

#==============FUNCTIONS===================
def read_dictionary_file():
    global dictionary
    # Read dictionary file in from dictionary file location SUCCESS
    # Store each word in a list. = my_dictionary SUCCESS
    my_dictionary = getattr(config, 'dictionary_loc', 'no_dictionary_found')
    #print(f'my_dictionary = {my_dictionary}')

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

def read_round_status_txt_file():
    global round_status
    # read the round status the Config round_status_loc file location 

    
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
    read_turn_txt_file()

    # read_round_status_txt_file()
    # read_final_round_txt_file() 

##IDK IF I ACTUALLY NEED THESE
    
    # get_player_info()
    
def get_word():
    global my_dictionary
    global round_underscore_word
    #choose random word from dictionary SUCCESS
    round_word = random.choice(my_dictionary)
    #make a list of the word with underscores instead of letters. SUCCESS
    round_underscore_word = ['_']* len(round_word)
    #print(round_underscore_word)
    return round_word, round_underscore_word
    

def wof_round_setup():
    global players
    global round_word
    global round_underscore_word

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
    my_spin = False
    while my_spin == False:
        # Get amount from wheel if not lose turn or bankruptcy. else hold # as value (result)
        result = spin_result
        if spin_result == 000:
            print('BANKRUPTCY!')
            round_total = 0 #TODO probably have to work on that somemore
            break
    # Check for lose turn. elif == 999 lose a turn
        elif spin_result == 999:
            print('LOSE A TURN!')
            break
        else:
            print('You spun $' + spin_result)
            consonant_eval()
            my_spin = True


def guess_letter(letter, player_num): # defines if approved letter(consonant or vowel) is in the puzzle # parameters:  take in a letter guess and player number
    good_guess = False
    while good_guess == False:
        if letter in round_word:
            #build list of positions of guessed letter(s) in the word SUCCESS
            # Change position of found letter in round_underscore_word to the letter instead of underscore 
            pos = [i for i in range(len(round_word)) if round_word.startswith(letter,i)]
            for i in pos:
                round_underscore_word = round_underscore_word[:i] + letter + round_underscore_word[i+len(letter):]
            print('Great!' + letter + 'was in the word ' + num + ' times!' ) # TODO define num as count of num of instances of letter.     # return count of letters in word. 
            print(f'The word: {round_underscore_word}')
            if "_" not in round_underscore_word:
                print ('You got the last letter! You win!')
                good_guess = True     # If letter is in the round_word let good_guess = True
                break #TODO probably dont want a break. break will end to the end of the while or for loop. probably want to go to round or game summary function or something 
            elif "_" in round_underscore_word:
                print('What would you like to do next?')
                wof_turn(player_num)
                good_guess = True     # If letter is in the round_word let good_guess = True
        #if the letter is NOT in the word
        else:
            print(letter + " is incorrect. Next player's turn") #TODO see if I can say 'Player X's turn (whoever comes next)
            break #not break, it would be the next player function 
    

def consonant_eval(player_num): #choose and define if consonant is acceptable
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
            guess_letter(letter, player_num)

    
def buy_vowel(player_num): #buys, selects, and evaluates vowel   # Take in a player number
    global players
    global vowels
    # Ensure player has 250 for buying a vowel_cost
    if player_round_bank >= 250: #TODO need to define player_round_bank
        #if yes, do you want to spend 250$
        response = input('would you like to buy a vowel for $250? [y/n]: ')
        if (response != 'y' and response != 'n'):
            print("Invalid response. Expected 'y' or 'n'.")
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
                    guess_letter(letter, player_num)
        #no i dont want to buy a vowel
        else:
            wof_turn(player_num)
    #if do not have $250
    else:
        print('You cannot afford a vowel right now!')
        wof_turn(player_num)
      
def solve_puzzle(player_num):
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
        choice = input('Would you like to (S)pin, (B)uy a vowel, or (G)uess the word? [S/B/G]: ')        
        if(choice.strip().upper() == "S"):
            still_in_turn = spin_wheel(player_num)
        elif(choice.strip().upper() == "B"):
            still_in_turn = buy_vowel(player_num)
        elif(choice.upper() == "G"):
            still_in_turn = solve_puzzle(player_num)
        else:
            print("Not a correct option")        
    
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     


def wof_round():
    global players
    global round_word
    global round_underscore_word
    global round_status
        # Return the starting player number (random) SUCCESS
    init_player = random.randint(1, 3)
    #print('Our starting player will be Player {}'.format(init_player)) original statement
    time.sleep(2) # pause again for more dramatic effect!
    print('Our starting player will be Player {}'.format(init_player))
    time.sleep(3) # pause again for more dramatic effect!
    print('The word on the board is: ')
    time.sleep(3) # pause again for more dramatic effect!
    print (round_underscore_word)
    time.sleep(3) # pause again for more dramatic effect!
    print('Player {}'.format(init_player) + ', what would you like to do?')
    player_num = init_player
    wof_turn(player_num)

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

def timer(): #SUCCESS
    for x in range(1, 5):
        print('You have {} seconds..'.format(5-x))
        time.sleep(x) # "Sleep" for x seconds
    print("Time's up!")

def main():
     

    for i in range(0,max_rounds):
        if i in [0,1]:
            round_num = str(i + 1)
            print("Let's begin round " + round_num + "...")
            wof_round()
            break
        else:
            print("Let's begin the Final Round...")
            wof_final_round()


if __name__ == "__main__":
    game_setup()   
    get_word()
    welcome_message()
    time.sleep(2) # pause again for more dramatic effect!
    main()
    
    
