import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# function
def caeser(text,shift,direction):
  plain_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)

      if direction == "encode" :
        new_position = position + shift
      elif direction == "decode" :
       new_position = position - shift

      new_letter = alphabet[new_position]
      plain_text += new_letter
    else :
      plain_text += letter
  print(f"The {direction}ed text is {plain_text}")

continue_ = True
while continue_:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caeser(text,shift,direction)
  result = input("yes for again and no to exit\n")
  if result == "no":
    continue_ = False
    print("Thank you to use this app")

  