#Import the random library so that we can generate random numbers.
import random

#Get a random number and assign it to a variable.
check = random.randint(1, 100)

#Define a function that allows the user to guess a number.
def checker():
	guess = int(input())
	return guess

#Create a variable to record the number of user guesses.
answer = 0

#Set the "guess" variable to a number outside the range of "check".
guess = 0

#See if the user guessed correctly.
while (guess != check) & (answer < 3):
	print("Please give us a number between 1 and 100:")
	guess = checker()
	#If the user's guess was too low, give them another chance.
	if guess < check:
		answer += 1
		print("I'm sorry, that guess was too low. Try again.")

	#If the user's guess was too high, give them another chance.	
	elif guess > check:
		answer += 1
		print("I'm sorry, that guess was too high. Try again.")

#Tell the user if they win.		
if guess == check:
	print("You win!")

check = str(check)
print("The correct number was " + check + ".")
	