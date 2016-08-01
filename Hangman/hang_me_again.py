#I don't need this anymore
#This is a hangman game
import os
import random
import time
###Function definition notes: 
###I am using 'word' to represent the updated blanks.
###I am using 'letter' to represent guess letters.
###I am using 'secret' to represent the secret word.

def user_continue():
	user_continue = input("Continue?: ")
	if user_continue == 'n':
		quit()

def dead_man_printer(wrong_guess):
	"""This prints the little hangman man."""
	if len(wrong_guess) == 1:
		print("__")
		print("  |")
		print("  o")
	elif len(wrong_guess) == 2:
		print("__")
		print("  |")
		print("  o")
		print("  |")
	elif len(wrong_guess) == 3:
		print("__")
		print("  |")
		print("  o ")
		print(" /| ")
	elif len(wrong_guess) == 4:
		print("__")
		print("  |")
		print("  o  ")
		print(" /|\ ")
	elif len(wrong_guess) == 5:
		print("__")
		print("  |")
		print("  o  ")
		print(" /|\ ")
		print(" /  ")
	elif len(wrong_guess) == 6:
		print("__")
		print("  |")
		print("  o  ")
		print(" /|\ ")
		print(" / \ ")

def print_current_word_and_guesses(word, guesses):
	"""This will show the user how many letters they have guessed so far."""
	print("Your word to guess:")
	print(word)
	if guesses:
		print("Your wrong guesses:")
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

def update_word(letter, secret, word, secret_bug):
	"""This will add the user's guess if it is correct."""
	for i in range(secret_bug):
		if secret[i] == letter:
			word[i] = letter
	return word

def wrong_guess_appender(letter, guesses):
	"""This will add to the list of wrong guesses."""
	guesses.append(letter)

def underscore_appender(word, secret):
	"""This will fill the user's word with dashes."""
	appen_counter = len(secret)
	while appen_counter > 0:
		word.append('_')
		appen_counter -= 1
	return word
	


def already_guessed_message():
	"""The message for if a user already guessed a letter."""
	print("You already guessed that letter.")
	print("Try again.")



def	main():
	blank_word = []
	wrong_guess = []
	words = ['marble', 'cheese', 'magic', 'nerd', 'sprite', 'zigzag',
	'billyclub', 'chill', 'netflix', 'hiphop', 'spanish', 'lilac',
	'lizard', 'beach', 'ocean', 'metal', 'brass', 'redhead', 'music',
	'driving', 'pizza', 'ambition', 'python']

	os.system('clear')
	print("Welcome to Hangman:")
	print("The Macabre Game for Word Nerds!")
	user_continue()
	secret_word = (random.choice(words))
	secret_bug = len(secret_word)
	print(secret_bug)
	blank_word = underscore_appender(blank_word, secret_word)

	print_current_word_and_guesses(blank_word, wrong_guess)
	while (len(wrong_guess) < 6) and (list(secret_word) != blank_word):

		my_letter = take_a_letter()
		time.sleep(0.1)
		os.system('clear')

		if already_guessed(my_letter, blank_word):

			print_current_word_and_guesses(blank_word, wrong_guess)
			already_guessed_message()

		elif not already_guessed(my_letter, blank_word):

			if letter_checker(my_letter, secret_word):

				update_word(my_letter, secret_word, blank_word, secret_bug)
				print("That's right!")
				print_current_word_and_guesses(blank_word, wrong_guess)
				dead_man_printer(wrong_guess)

			elif not letter_checker(my_letter, blank_word):

				print("Sorry, that letter isn't in there.")
				wrong_guess_appender(my_letter, wrong_guess)
				print_current_word_and_guesses(blank_word, wrong_guess)
				dead_man_printer(wrong_guess)


	if list(secret_word) == blank_word:

		print("You win! The word was: ", secret_word)
		print_current_word_and_guesses(blank_word, wrong_guess)

	elif list(secret_word) != blank_word:

		print("You lose! You guessed:", blank_word)
		print("The secret word was: ", secret_word)

my_looper = True

while my_looper:
	main()
	print("Play again?: ")
	user_choice = input("")
	if user_choice == "n": my_looper = False

