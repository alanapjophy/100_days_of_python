print("Wlecome to HangMan")
import random
word_list = ["apple","orange","mango"]
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
display = []
for i in range(word_length):
    display += "_"
print(display)