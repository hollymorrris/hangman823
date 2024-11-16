# %%
import random

names_of_favourite_fruit_list = ["mango", "blueberries", "strawberries", "banana", "pineapple"]
name_of_favourite_fruit = random.choice(names_of_favourite_fruit_list)

def check_guess(guess):
	guess = guess.lower()
	if guess in name_of_favourite_fruit:
		print("Good guess!", guess, "is in the word.")
	else:
		print("Sorry,", guess, " is not in the word. Try again.")

def ask_for_input():
	while True:
		print("Guess a single letter:")
		guess = input()
	
		if len(guess) == 1 and guess.isalpha():
			break
		else:
			print("Invalid letter. Please, enter a single alphabetical character.")
			continue 
	check_guess(guess)
ask_for_input()


