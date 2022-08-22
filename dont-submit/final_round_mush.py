# Use the get_word function to reset the round_word and the round_underscore_word ( word with the underscores) #CALLED ON IN MAIN, THAT HAPPENS BEFORE THIS
# 472 intro, gives letters, asks for letters and 
def wof_final_round(round_word, player_num):
    global round_underscore_word 
    global final_round_text
    winplayer = 0
    amount = 0
    # TODO Find highest game_total player.  They are playing.
    print(final_round_text) # Print out instructions for that player and who the player is.SUCCESS
        
    letter = input('R')
    final_guess_letter(letter, player_num)
    letter = input('S')
    final_guess_letter(letter, player_num)
    letter = input('T')
    final_guess_letter(letter, player_num)
    letter = input('L')
    final_guess_letter(letter, player_num)
    letter = input('N')
    final_guess_letter(letter, player_num)
    letter = input('E')
    final_guess_letter(letter, player_num)
    print(f'The word: {round_underscore_word}')
    # Gather 3 consonats and 1 vowel and use the guess_letter function to see if they are in the word
    ##THEN I WANT THE PLAYER TO APPEND THEIR 3 CONSONANTS AND 1 VOWEL TO final_letters
    letter = input('Choose one additional consonant: ')
    final_guess_letter(letter, player_num)
    letter = input('Choose another consonant: ')
    final_guess_letter(letter, player_num)
    letter = input('Choose one more consonant: ')
    final_guess_letter(letter, player_num)
    letter = input('And a vowel: ')
    final_guess_letter(letter, player_num)
    # Print out the current round_underscore_word  again
    print(f'The word: {round_underscore_word}')


    # Remember guess_letter should fill in the letters with the positions in round_underscore_word 
    # Get user to guess word
    # If they do, add final_prize and game_total and print out that the player won 

#THIS IS THE GENERAL ONE BUT I THINK I CAN DO IT WITH THE FINAL BETTER THAN WHAT I DID BELOW    
def final_guess_letter(letter, player_num): # GENERAL defines if approved letter(consonant or vowel) is in the puzzle # parameters:  take in a letter guess and player number
    global round_word
    global round_underscore_word 
    #global strcount
    strcount = ''
    
    for i in itertools.count(start=1):
        if letter in round_word:
            round_word, round_underscore_word = get_letter_position(letter, round_word, round_underscore_word)
            #print(round_underscore_word)
                # if "_" not in round_underscore_word:
            #     print ('You got the last letter! You win!')
            #     letter_count(player_num, round_word, final_letter)
            #     good_guess = True     # If letter is in the round_word let good_guess = True
            #     break #TODO probably dont want a break. break will end to the end of the while or for loop. probably want to go to round or game summary function or something 
            # elif "_" in round_underscore_word:
            #     print('Good guess!')
            #     letter_count(player_num, round_word, letter)
            #     #print('There are ' + count +'!')
            #     let_count = strcount
            #     print('There are {}'.format(let_count) + '!\n')
            #     #print('{} has occurred {} times'.format(letter, letter_count (round_word, letter))) 
            #     #print('{} has occurred' .format(letter, letter_count)) #moved print and wof_turn out of for statements
            #     #print('{} times' .format(round_word, letter)) tried to split it 
                #wof_turn(player_num, round_num)
                #break 
                #good_guess = True     # If letter is in the round_word let good_guess = True
            
        #if the letter is NOT in the word
        # else:
        #     print("\n" + letter + " is incorrect. Next player's turn.")
        #     wof_round(player_num, round_num)    
        # good_guess = True

##original final from 289
# # 289 defines if given and choosen letters are in the puzzle:
# def final_guess_letters(final_letters, round_word, player_num, round_underscore_word):# removed 'player_num' from () 
#     #copied from consanant eval #append guess to guesses 
#     index = 0
#     while index < len(final_letters):
#         if index == round_word:
#             #build list of positions of guessed letter(s) in the word SUCCESS
#             # Change position of found letter in round_underscore_word to the letter instead of underscore 
#             round_word, round_underscore_word = get_final_letter_position(index, round_word, round_underscore_word)
#             #print(round_underscore_word)          
#             if "_" not in round_underscore_word:
#                 print ('You spelled the whole word! You win!')
#                 # TODO get to winnings summary
#             else:
#                 print(round_underscore_word)   
#         index += 1
# 239if letter is in word, puts the letters in their places

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