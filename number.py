#Import the random library so that we can generate random numbers.
import random

#Get a random number and assign it to a variable.
secret_number = random.randint(1, 100)

#Define a function that allows the user to user_guess a number.
def take_user_guess():
	user_guess = int(input())
	return user_guess

#Create a variable to record the number of user user_guesses.
number_of_guesses = 0

#Set the "user_guess" variable to a number outside the range of "secret_number".
user_guess = 0

#See if the user guessed correctly.
while (user_guess != secret_number) & (number_of_guesses < 5):
	print("Please give us a number between 1 and 100:")
	user_guess = take_user_guess()
	
	#If the user's guess was too low, give them another chance.
	if user_guess < secret_number:
		number_of_guesses += 1
		print("I'm sorry, that user_guess was too low. Try again.")

	#If the user's guess was too high, give them another chance.	
	elif user_guess > secret_number:
		number_of_guesses += 1
		print("I'm sorry, that user_guess was too high. Try again.")

#Tell the user if they win.		
if user_guess == secret_number:
	print("You win!")

secret_number = str(secret_number)
print("The correct number was " + secret_number + ".")
	