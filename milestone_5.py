# %%
import random

class Hangman:
	'''
	This class is used to represent a game called Hangman.

	Attributes:
		word: The word to be guessed, picked randomly from the word_list. 
		word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed.
		num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
		num_lives (int): The number of lives the player has at the start of the game.
		word_list (list): A list of words.
		list_of_guesses (list): A list of the guesses that have already been tried.
	'''
	def __init__ (self, word_list, num_lives=5):
		self.word = random.choice(word_list)
		self.word_guessed = ["_" for _ in self.word]
		self.num_letters = len(set(self.word))
		self.num_lives = num_lives
		self.word_list = word_list
		self.list_of_guesses = []

	def check_guess(self, guess):
		'''
		This function is used to check if the guessed letter is in the word and to reduce the number of lives if the guess is not in the word.
		
		Args:
			guess (str): the string input by user.

		Returns:
			str: string to represent congratulating user and show position of guessed letters in word, if the guessed letter is in the word; string to notify user guess is not in word and reduced number of lives left otherwise.

		'''
		guess = guess.lower()
		if guess in self.word:
			print("Good guess!", guess, " is in the word.")
			for letter_in_word_guessed, letter in enumerate(self.word):
				if letter == guess:
					self.word_guessed[letter_in_word_guessed] = guess
			print(self.word_guessed)
			self.num_letters -= 1
		else:
			self.num_lives -= 1
			print("Sorry,", guess, " is not in the word.")
			print("You have", self.num_lives, "lives left.")
	
	def ask_for_input(self):
		'''
		This function is used to ask the user to input a letter and check it is a single letter that they haven't input before.

		Returns:
			str: string to represent prompt for correct input from user. 
		'''
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
				break
		
def play_game(word_list):
	'''
	This function is used to run all of the code to run the hangman game.

	Args:
		word_list (str): the list of words from which computer generates random word.

	Returns: string to represent if user has won or lost.
	
	'''
	num_lives = 5 
	game = Hangman(word_list, num_lives)
	while True:
		if game.num_lives == 0:
			print("You lost!")
			break
		elif game.num_letters > 0:
			game.ask_for_input()
		else:
			print("Congratulations. You won the game!")
			break
	
word_list = ["mango", "blueberries", "strawberries", "banana", "pineapple"]
play_game(word_list)

# %%
