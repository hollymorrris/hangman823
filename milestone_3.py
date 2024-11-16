# %%
import random

names_of_favourite_fruit_list = ["mango", "blueberries", "strawberries", "banana", "pineapple"]
name_of_favourite_fruit = random.choice(names_of_favourite_fruit_list)

def check_guess(guessed_letter):
	guessed_letter = guessed_letter.lower()
	if guessed_letter in name_of_favourite_fruit:
		print("Good guess!", guessed_letter, "is in the word.")
	else:
		print("Sorry,", guessed_letter, " is not in the word. Try again.")

def ask_for_input():
	while True:
		print("Guess a single letter:")
		guessed_letter = input()
	
		if len(guessed_letter) == 1 and guessed_letter.isalpha():
			break
		else:
			print("Invalid letter. Please, enter a single alphabetical character.")
			continue 
	check_guess(guessed_letter)
ask_for_input()



# %%
