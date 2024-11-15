# %%
import random

word_list = ["mango", "blueberries", "strawberries", "banana", "pineapple"]
word = random.choice(word_list)
print(word)

# %%
print("Enter a single letter:")

guess = input()

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")

else: 
    print("Oops! That is not a valid input.")

# %%
