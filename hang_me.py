#This is a hangman game
import os
###Function definition notes: 
###I am using 'word' to represent the updated blanks.
###I am using 'letter' to represent guess letters.
###I am using 'secret' to represent the secret word.

def user_continue():
	user_continue = input("Continue?: ")
	if user_continue == 'n':
		quit()

def print_current_word_and_guesses(word, guesses):
	"""This will show the user how many letters they have guessed so far."""
	print("Your word to guess:")
	print(word)
	if guesses:
		print("So far you have guessed:")
		print(guesses)

def take_a_letter():
	"""This takes a guess letter from the user."""
	letter = input("Please guess a letter: ")
	return letter

def letter_checker(letter, secret):
	"""This checks whether the letter is in the secret word."""
	if letter in secret:
		return True
	elif letter not in secret:
		return False

def already_guessed(letter, word):
	"""This checks whether the letter has been guessed already."""
	if letter in word:
		return True
	elif letter not in word:
		return False

def update_word(letter, secret, word):
	"""This will add the user's guess if it is correct."""
	for i in range(6):
		if secret[i] == letter:
			word[i] = letter

def wrong_guess_appender(letter, guesses):
	"""This will add to the list of wrong guesses."""
	guesses.append(letter)

def already_guessed_message():
	"""The message for if a user already guessed a letter."""
	print("You already guessed that letter.")
	print("Try again.")


secret_word = "marble"
secret_list = ['m', 'a', 'r', 'b', 'l', 'e']
blank_word = ['_', '_', '_', '_', '_', '_']
wrong_guess = []
dash_count = len(secret_word)
wrong_guess_count = 6

print("Welcome to Hangman:")
print("The Macabre Game for Word Nerds!")
user_continue()
print_current_word_and_guesses(blank_word, wrong_guess)
while (wrong_guess_count > 0) and (secret_list != blank_word):

	#print_current_word_and_guesses(blank_word, wrong_guess)
	#user_continue()
	my_letter = take_a_letter()
	os.system('clear')

	if already_guessed(my_letter, blank_word):
		already_guessed_message()
		#user_continue()

	elif not already_guessed(my_letter, blank_word):

		if letter_checker(my_letter, secret_list):
			
			update_word(my_letter, secret_list, blank_word)
			print("That's right!")
			print_current_word_and_guesses(blank_word, wrong_guess)
			#user_continue()

		elif not letter_checker(my_letter, blank_word):

			print("Sorry, that letter isn't in there.")
			wrong_guess_appender(my_letter, wrong_guess)
			wrong_guess_count -= 1
			print_current_word_and_guesses(blank_word, wrong_guess)
			#user_continue()

if secret_list == blank_word:

	print("You win! The word was:", secret_word)
	print_current_word_and_guesses(blank_word, wrong_guess)

elif secret_list != blank_word:

	print("You lose! You guessed:", blank_word)
	print("The secret word was:", secret_word)
