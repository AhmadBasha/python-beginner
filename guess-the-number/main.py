#Number Guessing Game Objectives:
import art
import random 
from replit import clear

# print the number of user attempts 
def playerAttempts(num):
  print(f"You have {num} attempts to guess the correct number")
# to check the difficulty of the game
def theLevel(level) : 
  if level == "easy" :
    playerLevel = 10
    playerAttempts(playerLevel)
    return playerLevel
  else:
    playerLevel = 5
    playerAttempts(playerLevel)
    return playerLevel

# calculate the number of attempts and compare the user answer
def logic(attempts , actualNumber):
  GameOver = False
  while attempts != 0 and GameOver == False:
    userGuess = input("Make a GUESS: ")
    if actualNumber+9 < int(userGuess):
      print("your number is too High")
      attempts -= 1
      playerAttempts(attempts)
    elif actualNumber-9 > int(userGuess):
      print("your number is too Low")
      attempts -= 1
      playerAttempts(attempts)
    elif actualNumber < int(userGuess) :
      print("your number is littile bit High")
      attempts -= 1
      playerAttempts(attempts)
    elif actualNumber > int(userGuess) :
      print("your number is littile bit Low")
      attempts -= 1
      playerAttempts(attempts)
    else :
      print(f"Correct Answer {actualNumber}")
      GameOver = True
      return True
  return False

# print the player is win or lose
def is_winning(winner , answer):
  if winner == False:
    print("Game Over You Lose 😭")
    print(f"The correct number is: {answer}")
  else:
    print("Your Guessed is Correct You WIN 🥳")


# print the logo
print(art.logo)
# random number 
actual = random.randint(1,100)

print("Welcome To The Number Guessing Game")
print("I'm thinking of a number between 1 and 100 GUESS!!! ")
# game level
gameLevel = input("Type 'easy or 'hard': ")
# return the attempt depends on the gameLevel
attempt = theLevel(gameLevel)
# here the logic if the game take the actual number and compare with the user and store the bool value
win = logic(attempt,actual)
#print if the player win or lose
is_winning(win,actual)



