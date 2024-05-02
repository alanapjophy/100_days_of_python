# Logo
from art import logo
print(logo)

# List
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encrypt & decrypt.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = "" 
  # If decoding changing the sign of shift_amount. 
  if cipher_direction == "decode":
    shift_amount *= -1
    # If start_text is included symbols, numbers, white spaces etc. we need to keep those in the end_text
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Main body
should_end = True
# When the condition is true the loop will be executed.
while should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # If the shift is greater than the length of the alphabet we need to do the modulus.
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  # Asking the user to continue or not
  continue_to = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if continue_to == "no":
    should_end = False
    print("Goodbye")
  
