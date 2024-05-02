alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
  new_string = ""
  for letter in text:
    plain_text = alphabet.index(letter[0])
    
    # The other way is that we can copy the list alphabet and paste in it so that the index won't become out of range. And also the index function will only read the first letter in the alphabet even if there are two letters for each.
    
    if plain_text + shift > 25:
       new_string +=  alphabet[(plain_text + shift) -26]
    else:
      cipher_text =  alphabet[plain_text + shift]
      new_string += cipher_text
  print(f"The encoded text is {new_string}")
  
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

 
   
    # print(cipher_text)
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

encrypt(text, shift)
