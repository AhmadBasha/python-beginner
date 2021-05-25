from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")

bidders = {}

bidders_status = True
while bidders_status :
  name = input("What Is Your Name?: ")
  bid = input("What Is Your Bid?: $")
  bidders[name] = bid

  status = input("Are There Any Other Bidders? 'yes' OR 'no': ")
  if status == 'no':
    bidders_status = False
  else :
    clear()
i = 0
winner = ""
amount = 0
for key in bidders:
  if int(bidders[key]) > i : 
     i = int(bidders[key])
     winner= key
     amount = int(bidders[key])
  
  

print(f"The Winner is {winner} with a bid of ${amount}")
