import art
import random
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def compare(player_score , computer_score):
  if player_score == computer_score :
    return "DRAW"
  elif computer_score == "BlackJack" :
    return "You Lose , The Other Player Has Blackjack"
  elif player_score == "BlackJack" :
    return "You Win , With a Blackjack"
  elif player_score > 21:
    return "You Went Over. You Lose"
  elif player_score > 21:
    return "You Win . The Other Player Went Over"
  elif player_score > computer_score :
    return "Your Score Is Higher , You Win"
  else :
    return "The Other Player has a Higher Score , You Lose"

def playGame():
  print(art.logo)
  computersCards = []
  playerCards = []
  gameOver = False

  for i in range(2):
    computersCards.append(deal_card())
    playerCards.append(deal_card())
  def caculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2 :
      return "BlackJack"
    if 11 in cards and sum(cards) > 21 :
      cards.remove(11)
      cards.append(1)
    return sum(cards)

  while not gameOver:
    computerScore = caculate_score(computersCards)
    playerScore = caculate_score(playerCards)

    print(f"Your Cards are : {playerCards} , Your Score is : {playerScore}")
    print(f"Computer First Card is : {computersCards[0]}")

    if computerScore == "BlackJack" or playerScore == "BlackJack" or playerScore > 21:
      gameOver = True
    else:
      status = input("Type 'y' to get another card, type 'n' to pass: ")
      if status == "y":
        playerCards.append(deal_card())
      else :
        gameOver = True

  while computerScore < 17 and computerScore != "BlackJack":
    computersCards.append(deal_card())
    computerScore = caculate_score(computersCards)

  print(f" Your Final Hand is : {playerCards} With Score {playerScore} ")
  print(f" The Other Player's Hand is : {computersCards} With Score {computerScore} ")

  print(compare(playerScore,computerScore))

while input("Do You Want To Play A Game of Blackjack? Type 'y' For Yes & 'n' For No : \n") == "y" :
  clear()
  playGame()



