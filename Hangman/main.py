#Step 5

import random
import hangman_words
import hangman_art

from replit import clear

print(hangman_art.logo)

# randmly choosing a word
chosen_word = random.choice(hangman_words.word_list)
# for the - - - - symbols
display = []
for i in range(len(chosen_word)):
  display.append("_")

lives = 6

while '_' in display:
  print(display)
  # user guessing a letter 
  guess = input("Guess a letter\n")
  guess = guess.lower()
  clear()
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
     display[i] = guess
  
  if guess not in chosen_word:
    lives -=1
    print(hangman_art.stages[lives])
    if lives == 0:
      break
 
if lives == 0 :
  print("You Lose")
else :
  print("You win")