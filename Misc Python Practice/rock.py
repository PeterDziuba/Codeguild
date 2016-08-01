#This is a Rock-Paper-Scissors Program!
import random
import os

print("Welcome to Rock-Paper-Scissors!")

looper = True
user_score = 0
computer_score = 0

while looper:
	print("Choose rock, paper, or scissors:")
	user_play = input()
	computer_choice = random.randint(1,3)
	if computer_choice == 1: computer_play = "rock"
	elif computer_choice == 2: computer_play = "paper"
	elif computer_choice == 3: computer_play = "scissors"

	os.system('clear')

	if user_play == computer_play:
		print("You both chose", computer_play + ".")
		print("Tie, play again?")
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	elif (user_play == 'rock') and (computer_play == 'paper'):
		print("You chose", user_play, "and the computer chose",
			computer_play + ".")
		computer_score += 1
		print('Computer wins! Play again?')
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	elif (user_play == 'rock') and (computer_play == 'scissors'):
		print("You chose", user_play, "and the computer chose",
			computer_play + ".")
		user_score += 1
		print("You win! Play again?")
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	elif (user_play == 'paper') and (computer_play == 'rock'):
		print("You chose", user_play, "and the computer chose",
			computer_play + ".")
		user_score += 1
		print("You win! Play again?")
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	elif (user_play == 'paper') and (computer_play == 'scissors'):
		print("You chose", user_play, "and the computer chose",
			computer_play + ".")
		computer_score += 1
		print('Computer wins! Play again?')
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	elif (user_play == 'scissors') and (computer_play == 'rock'):
		print("You chose", user_play, "and the computer chose",
			computer_play + ".")
		computer_score += 1
		print('Computer wins! Play again?')
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	elif (user_play == 'scissors') and (computer_play == 'paper'):
		print("You chose", user_play, "and the computer chose",
			computer_play + ".")
		user_score += 1
		print("You win! Play again?")
		user_choice = input()
		if user_choice == 'n':
			looper = False
		os.system('clear')

	else:
		print('Something went wrong. Please enter rock, paper,', 
			'or scissors.')
		print('Try again?')

if computer_score > user_score:
	print('Computer wins with a score of {} to'.format(computer_score),
		'your measly {}.'.format(user_score))

elif user_score > computer_score:
	print('User wins with a score of {} to the'.format(user_score),
		"computer's {}.".format(computer_score))

elif user_score == computer_score:
	print("It's a tie! You both scored {}.".format(user_score))


