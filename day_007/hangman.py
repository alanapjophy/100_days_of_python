print("Welcome to HangMan!")
import random
list = ["apple","orange","mango"]
word = random.choice(list)
guess = input("Guess a letter : ").lower()
display = []
for _ in word:
    print("_")
end_of_game = False
while not end_of_game:
    for letter in word:
        if guess == letter:
            print("Right")
        else:
            print("Wrong")