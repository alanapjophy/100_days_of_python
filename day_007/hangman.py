print("Welcome to HangMan!")
import random
word_list = ["apple","orange","mango"]
chosen_word = random.choice(word_list)
# print(chosen_word)
guess = input("Guess a letter : ").lower()
chosen)letter = len(chosen_word)
display = []
for _ in range(chosen_word):
    display += "_"
print(display)