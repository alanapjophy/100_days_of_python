# # Make a simple outline
# print("Wlecome to HangMan")
# import random
# word_list = ["apple","orange","mango"]
# chosen_word = random.choice(word_list).lower()
# word_length = len(chosen_word)
# display = []
# for i in range(word_length):
#     display += "_"
# print(display)
# guess = input("Guess a letter: ").lower()
# for key in chosen_word:
#     if guess == key:
#         print("right")
#     else:
#         print("Wrong")



# Make letters in list
print("Wlecome to HangMan")
import random
word_list = ["apple","orange","mango"]
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
end_of_game = false
display = []
for i in range(word_length):
    display += "_"
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for key in chosen_word:
    if guess == key:
        for i in range(word_length):

        print("right")
    else:
        print("Wrong")