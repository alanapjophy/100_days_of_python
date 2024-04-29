print("Welcome to HangMan!")
import random
list = ["apple","orange","mango"]
word = random.choice(list)
display = []
for i in word:
    print("_")
guess = input("Guess a letter : ").lower()


# end_of_game = False
# while not end_of_game:
#     for letter in word:
#         if guess == letter:
#             print("Right")
#         else:
#             print("Wrong")
# if end_of_game:
#     print("true")