# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 02:57:32 2021

@author: Rana Muneeb Asad
"""
import random

import hangman_art
import hangman_wordlist



num_of_lives = 6

display = []

end_of_game = False
start_logo = hangman_art.logo
chosen_word = random.choice(hangman_wordlist.word_list)

for underscore in range(len(chosen_word)):
    display += '_'

print(start_logo, "\n", "\n")

print(display, "\n", "\n")

while not end_of_game:
   
    print(f"the number of lives are {num_of_lives} \n")
    guess = input("Guess the letter? ")
    guess = guess.lower()

    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter
            
    if guess not in chosen_word:
        num_of_lives -= 1
        if num_of_lives == 0:
            end_of_game = True
            print("You loose")
            print(f"The word was {chosen_word}")
            
    print(f"\n{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print('You win')
    
    print(hangman_art.stages[num_of_lives])
