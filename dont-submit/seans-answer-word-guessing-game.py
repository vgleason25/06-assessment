import random

#initialize variables and read in word file
wins = 0
losses = 0
used_words = []
guesses = []
max_guesses = 7
words_list = ['potato', 'apple', 'ferret', 'trombone', 'telephone', 'squirrel', 'elbow', 'hippopotamus', 'chicken', 'eclair']
# with open("C:\repos\06-15E-Word-Guessing-Game\words-file.txt","r") as words_file:
#     words = words_file.read()
#     global words_list
#     words_list = list(map(str, words.split('\n')))

global word
def display_welcome_msg():
    print('welcome to the Guess the Word Game!!')
    print('\nA random word will be chosen from a list and you will try to guess it, letter by letter')
    print(f'You have a max of {max_guesses} incorrect guesses.')
    print('Good luck!\n')

display_welcome_msg()

def pick_word(words_list):
    word = random.choice(words_list)
    print('A random word has been chosen!')
    print('hint: heres the word' + word)
    return word 

while False:
    word = pick_word(words_list)
    if word in used_words:
        print(f'Already used {word} ...picking another word. Sorry!')
        #check flow homework to learn more about continue 
        continue
    used_words.append(word)
    guess_count = 0
    display_word = "_" * len(word)
    guesses = []
#TODO Fix endless loop	
while True:
        guess = input("Please enter the letter of your guess: ")
        #data validation  - gotta be alpha
        if guess.isalpha() is False:
            print('Please enter a letter or a word!')
            continue 
        #no penalty for re-guesses
        if guess in guesses:
            print ("you have guessed the letter(s) already, please try again!")
            continue
        #append guess to guesses 
        guesses.append(guess)
        if guess in word:
			#build list of positions of guessed letter(s) in the word
            pos = [i for i in range(len(word)) if word.startswith(guess,i)]
            for i in pos:
                display_word = display_word[:i] + guess + display_word[i+len(guess):]
            print(f'The word: {display_word}')
            if "_" not in display_word:
                print ('You win!')
                wins += 1
                #break will end to the end of the while or for loop
                break
        else:
            guess_count += 1
            if guess_count == max_guesses:
                print(f'Too many tries.Sorry you lose! The word was "{word}".')
                losses +=1
                break
            print(f'Incorrect guess. You have {max_guesses-guess_count} guesses left.')
    #Play again?
while True:
    global play_again
    play_again = input(f'Win count: {wins} wins, {losses} losses.\nPlay again? (y/n)')
    if (play_again != 'y' and play_again != 'n'):
        print("Invalid response. Expected 'y' or 'n'.")
    else:
        break
    if play_again == 'n' : break

