import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

selected = input("select 0 => Rock , 1 => Paper , 2 => Scissors \n")

generate = random.randint(0,2)


print(game[int(selected)]+"\n")
print("Computer Choice")
print(game[generate])

if game[int(selected)] == game[generate] :  
  print("DRAW 🤝")
elif (int(selected) == 0 and generate == 2) or (int(selected) == 1 and generate == 0) or (int(selected) == 2 and generate == 1):
  print("YOU ARE THE WINNER 🥳 👍")
else :
  print("LOOOOOSER 😂 👎")


