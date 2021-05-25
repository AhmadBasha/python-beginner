import art
from replit import clear


# functions ###
def addition(x,y) :
  return x+y

def multiply(x,y) :
  return x*y

def substract(x,y) :
  return x-y

def devide(x,y) :
  return x/y

def result(x,y,operation) :
  if operation == "+" :
    return addition(x,y)
  elif operation == "*" :
    return multiply(x,y)
  elif operation == "-" :
    return substract(x,y)
  elif operation == "/" :
    return devide(x,y)
  

#####

while 1 > 0 :
  print(art.logo)
  first_number = float(input("What is the first number?: "))
  status = 'y'
  while status == 'y' :
    operation = input("+\n-\n*\n/\nPick An Operation: ")
    second_number = float(input("What is the next number?: "))

    result(first_number,second_number,operation)

    print(f"{first_number}{operation}{second_number} = {result(first_number,second_number,operation)}")
    first_number = result(first_number,second_number,operation)

    status = input("type 'y' to continue calculate with the final result, or type 'n' to start a new calculation: ")
    if status == 'n':
      clear()
      break







