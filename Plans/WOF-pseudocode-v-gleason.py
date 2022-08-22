1) game_setup() #105 [.circle]
  reads in: read_dictionary_file()
  reads in: read_wheel_txt_file()
  reads in: read_turn_txt_file()
  reads in: read_final_round_txt_file()
  reads in: round_status_txt_file()
  not sure about: get_player_info()
  2) welcome_message #18
    presents: rules of the game
      calls on: 3) wof_round_setup() #134 [round_setup]
        creates: inital player
          1 calls on:get_word #123[gw]
            generates: word, underscore word 
          2 calls on: 4) main() presents lets begin #436 [.diamond][m]
              calls on: 5) wof_turn #370 shows output for player's status for the round Choose-[.diamond] [turn]
                Spin: spin_wheel(player_num}  spin the wheel
                  Bankrupt: spun 'bankrupt'
                    Update: player round total = 0 --TODO where is this?
                      still_in_turn = False [f]
                        6) wof_round() #370 [.diamond] [round]
                  Lose a turn: spun 'lose a turn'
                    (f)
                      (round)
                  Dollar value: saves $amount as spin_result
                    calls on: consonant_eval(player_num} choose a letter [.diamond]  [ce]
                      if not letter:
                        (ce)
                      if already chosen:
                        (ce)
                      if vowel:
                        (ce)
                      if viable letter:append to guessed letters - letters_guessed.append(letter]
                        calls on: guess_letter #214 (letter, player_num] [gl]
                          Evaluate: if letter in round_word
                            Success: letter in word
                              Update: round_underscore_word
                                Define: count of guessed letter
                                  Update: player's round bank by = # of letter/s x wedge value 
                                    still_in_turn = True [t]
                                      (turn)
                            Failure: (f)
                              (round)
                    Buy vowel: Player buys vowel
                      Update: player round total - 250 --TODO where is this?
                        Success: (t)
                          (turn)
                        Failure: (f)
                          (round)
                    Guess: Solve the puzzle
                      Success: Round 1 or 2 complete [.circle]
                        Updates: player round total --TODO where is this?
                          (round_setup)
                      Failure: (f)
                        (round)              
                        
                calls on: wof_final_round() TODO
                  evaluates: who is highest game_total player? 
                    presents: Who player is and what the rules are
                          calls on: final_guess_letter(player_num]