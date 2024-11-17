# %%
import random

class Hangman:
	def __init__ (self, word_list, num_lives=5):
		self.word = random.choice(word_list)
		self.word_guessed = ["_" for _ in self.word]
		self.num_letters = len(set(self.word))
		self.num_lives = num_lives
		self.word_list = word_list
		self.list_of_guesses = []

	def check_guess(self, guess):
		guess = guess.lower()
		if guess in self.word:
			print("Good guess!", guess, " is in the word.")
			for i, letter in enumerate(self.word):
				if letter == guess:
					self.word_guessed[i] = guess
			print(self.word_guessed)
			self.num_letters -= 1
		else:
			self.num_lives -= 1
			print("Sorry,", guess, " is not in the word.")
			print("You have", self.num_lives, "lives left.")
	
	def ask_for_input(self):
		while True:
			print("Guess a single letter")
			guess = input()
			if len(guess) != 1 or not guess.isalpha():
				print("Invalid letter. Please, enter a single alphabetical character.")
			elif guess in self.list_of_guesses:
				print("You already tried that letter!")
			else:
				self.check_guess(guess)
				self.list_of_guesses.append(guess)

word_list = ["mango", "blueberries", "strawberries", "banana", "pineapple"]
game = Hangman(word_list)
game.ask_for_input()

# %%
