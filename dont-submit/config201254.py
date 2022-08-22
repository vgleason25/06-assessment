
# TEMP dict
dictionary_loc = ['potato']

# NEED THIS TO ACCESS 'SUPER SECRET dictionary INFORMATION' 
# f = open('dictionary.txt')
# dictionary_loc =f.read().splitlines()
# f.close()

# NEED THIS TO ACCESS 'SUPER SECRET turn text INFORMATION' will be useful for adding up how much a player makes in a turn and at 
# the end of the turn, adding turn total to round total 
f = open('turn_text.txt')
turn_text_loc =f.read()
f.close()
#print(turn_text_loc)

# NEED THIS TO ACCESS 'SUPER SECRET wheel text INFORMATION' 
f = open('wheel_data.txt')
wheel_text_loc =f.read().splitlines()
f.close()
#print(wheel_text_loc)

# NEED THIS TO ACCESS 'SUPER SECRET round status INFORMATION' will be useful for defining winner of round 1 and 2 and who goes to round 3
f = open('round_status.txt')
round_status_loc =f.read()
f.close()
#print(round_status_loc)

# number of rounds in a game
max_rounds = 3 #or is it 2 (0,1,2) or is it 3(1,2,3)?

# Vowel cost
vowel_cost = 250

# final prize, you fill this in
final_prize = 1,000,000


# NEED THIS TO ACCESS 'SUPER SECRET final round INFORMATION' not sure what goes here. Maybe default letters?
f = open('final_round.txt')
final_round_text_loc =f.read()
f.close()
#print(final_round_text_loc)
