# %%
import random

names_of_favourite_fruit_list = ["mango", "blueberries", "strawberries", "banana", "pineapple"]
name_of_favourite_fruit = random.choice(names_of_favourite_fruit_list)
print(name_of_favourite_fruit)

# %%
print("Enter a single letter:")

guessed_letter = input()

if len(guessed_letter) == 1 and guessed_letter.isalpha():
    print("Good guess!")

else: 
    print("Oops! That is not a valid input.")

# %%
