print("Wlecome to HangMan")
import random
word_list = ["apple","orange","mango"]
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
display = []
for i in range(word_length):
    display += "_"
print(display)
guess = input("Guess a letter: ").lower()
# print(guess)
position = 0
for key in chosen_word:
    position += 1
    if guess == key:
        # print("right")
        display[position] = guess
    else:
        print("Wrong")
