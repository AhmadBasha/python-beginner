import art 
import random
import game_data as gd
from replit import clear


# to end the game 
gameOver = False 
# record the score
score = 0
# here to take the name and desc and the country for
# the famous accounts 
def info(name,desc,country,switch):
  if switch:
    return f"Compare A: {name}, {desc}, from {country}"
  else :
    print(art.vs)
    return f"Against B: {name}, {desc}, from {country}"
# compare the result or the followers for each A and B famouses 
def compare(famousOne, famousTwo):
  if famousOne > famousTwo :
    return "A"
  elif famousOne < famousTwo :
    return "B"
  else :
    return "C"

#check the answer of the user with the actual 
def check(actual ,userSelected):
  if actual != userSelected:
    print(f"Wrong Answer")
    return False
  elif actual == userSelected :
    print(f"Correct Answer")
    return True
  else :
    print(f"Wrong selected")
    return False


while gameOver == False :
  print(art.logo)

  A = random.choice(gd.data)
  B = random.choice(gd.data)
  # for score 
  # the result and call compare function 
  result = compare(A["follower_count"],B["follower_count"])
  # to print the info for a and b 
  print(info(A["name"],A["description"],A["country"],True))
  print(info(B["name"],B["description"],B["country"],False))
  # user answer 
  selected = input("Who has more followers? Type 'A' or 'B': ").upper()
  #check the answer 
  final = check(result,selected)
  # if the return is true from check will increase the score 
  if final == True :
    score +=1
    clear()
    print(f"You Score is : {score}")
  else :
    print(f"Try again your final score is  : {score}")
    gameOver = True 

