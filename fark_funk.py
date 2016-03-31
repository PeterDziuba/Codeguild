#This is my farkle program, built using functions!
import os
import time
import random

def rolling_length(rolling_set):
	"""This tells the player how many dice they have to roll."""
	print("{} dice/die left to roll.".format(len(rolling_set)))

def winner_printer(player_one_score, player_two_score):
	"""This function prints the winner at the end of the game."""
	if player_one_score > player_two_score:
		print("Player One Wins!")
		print("Player One Score:", player_one_score)
		print("Player Two Score:", player_two_score)
	elif player_two_score > player_one_score:
		print("Player Two Wins!")
		print("Player One Score:", player_one_score)
		print("Player Two Score:", player_two_score)
	elif player_one_score == player_two_score:
		print("It's a tie! That's highly unlikely!")
		print("Player One Score:", player_one_score)
		print("Player Two Score:", player_two_score)

def player_turn_banner(player_turn):
	"""This tells the user whose turn it is."""
	if player_turn: print("Player Two's Roll:")
	elif not player_turn: print("Player One's Roll:")

def empty_dice_dict(dice_dictionary):
	"""This function gives us a fresh dictionary full with 5d6."""
	dice_dictionary.clear()
	dice_dictionary = {1 : random.randint(1,6), 2 : random.randint(1,6), 3 : random.randint(1,6),
	4 : random.randint(1,6), 5 : random.randint(1,6)}
	return dice_dictionary

def user_boolean_choice(looper):
	"""This lets the user choose to quit or continue. I do this a lot."""
	if looper:
		user_choice = input("Continue?: ")
		if user_choice == 'n': looper = False
		else: looper = True
	print("")
	return looper

def empty_counters(counters):
	"""This function will clear the number counters."""
	counters = [0, 0, 0, 0, 0, 0]
	return counters

def empty_scoring_list(scoring_list):
	"""This function empties the scoring list."""
	del scoring_list[:]
	return scoring_list

def reset_rolling_set(rolling_set):
	"""This function resets the rolling set of dice."""
	for i in range(1, 6):rolling_set.add(i)
	return rolling_set

def reset_score(score):
	"""This resets any score."""
	score = 0
	return score


def change_players(player_turn):
	"""This function switches whose turn it is."""
	if player_turn:
		print("Player One's Turn")
		player_turn -= 1
	elif not player_turn:
		print("Player Two's Turn")
		player_turn += 1
	return player_turn

def add_total_score(stage_score, total_score):
	"""This adds the stage score to the total score."""
	total_score += stage_score
	return total_score

def counter_tally(scoring_list, counters):
	"""This function uses the number counters to score the current hand."""
	for i in scoring_list:
		if i == 1: counters[0] += 1
		elif i == 2: counters[1] += 1
		elif i == 3: counters[2] += 1
		elif i == 4: counters[3] += 1
		elif i == 5: counters[4] += 1
		elif i == 6: counters[5] += 1
	return counters

def counter_score(counters, stage_score):
	"""This function scores the dice!"""
	if counters[0] == 3:
		stage_score += 1000
	elif counters[0] < 3:
		stage_score += (100 * counters[0])
	elif counters[0] > 3:
		stage_score += 1000
		stage_score += (100 * (counters[0] - 3))
	if counters[1] >= 3:
		stage_score += 200
	if counters[2] >= 3:
		stage_score += 300
	if counters[3] >= 3:
		stage_score += 400
	if counters[4] == 3:
		stage_score += 500
	elif counters[4] > 3:
		stage_score += 500
		stage_score += (50 * (counters[4] - 3))
	elif counters[4] < 3:
		stage_score += 50 * counters[4]
	if counters[5] >= 3:
		stage_score += 600
	return stage_score

def counter_pop(counters, rolling_set):
	"""This function takes the scoring dice out of the rolling set."""
	if counters[0] > 0:
		for i in range(counters[0]):
			rolling_set.pop()
	if counters[1] >= 3:
		for i in range(3): rolling_set.pop()
	if counters[2] >= 3:
		for i in range(3): rolling_set.pop()
	if counters[3] >= 3:
		for i in range(3): rolling_set.pop()
	if counters[4] > 0:
		for i in range(counters[4]):
			rolling_set.pop()
	if counters[5] >= 3:
		for i in range(3): rolling_set.pop()
	return rolling_set

def dice_roller(scoring_list, rolling_set, dice_dictionary):
	"""This function saves some values for our dice."""
	if rolling_set:
		for i in rolling_set:
			scoring_list.append(dice_dictionary[i])
	return scoring_list

def farkle_no_score(total_score, player_one_score, player_two_score, rolling_set):
	"""This function displays the game stats when someone farkles. It also runs the change player function."""
	print('Farkle, you lose!')
	print('Player One Score:', player_one_score)
	print('Player Two Score:', player_two_score)
	print('')
	
def boolean_steal_choice(total_score, looper):
	"""This function gives you the chance to steal points when your opponent farkles."""
	if total_score >= 500:
		user_choice = input("Would you like to steal the dice?")
		if user_choice.lower() == 'y':
			return True
		elif user_choice.lower() == 'n':
			return False

def rolling_set_stealer(boolean_steal_choice, rolling_set, total_score):
	if boolean_steal_choice:
		print("You stole {} die/dice!".format(len(rolling_set)))
		print("Rolling with {} points!".format(total_score))
	elif not boolean_steal_choice:
		reset_rolling_set(rolling_set)
		reset_score(total_score)

def intro_to_farkle(looper):
	"""This function plays the intro!"""
	print("Welcome to Farkle:")
	print("A Dumb Game with Dice.")
	print("")
	user_boolean_choice(looper)

def score_board(stage_score, total_score, player_one_score, player_two_score, player_turn, scoring_list, rolling_set):
	"""This displays the current score for the user."""
	print("Your Roll:", scoring_list)
	print('Your Score this Roll:', stage_score)
	print('Your Score this Round:', total_score)
	print('Player One Score:', player_one_score)		
	print('Player Two Score:', player_two_score)
	print("")
	print("{} dice/die left to roll.".format(len(rolling_set)))
	print("")

my_looper = True
my_dice = {}
counters = []
player_turn = 0
scoring_list = []
rolling_set = set()
player_one_score = 0
player_two_score = 0
total_score = 0
stage_score = 0

intro_to_farkle(my_looper)
reset_rolling_set(rolling_set)

while my_looper:
	#Empty the counters, the scoring list, and the dice dict
	empty_scoring_list(scoring_list)
	my_dice = empty_dice_dict(my_dice)
	counters = empty_counters(counters)
	#Tell the player whose turn it is and how many dice to roll
	player_turn_banner(player_turn)
	rolling_length(rolling_set)
	#my_looper = user_boolean_choice(my_looper)
	os.system('clear')
	#Roll the dice, add to the counters, and tally the current score
	scoring_list = dice_roller(scoring_list, rolling_set, my_dice)
	counters = counter_tally(scoring_list, counters)
	stage_score = counter_score(counters, stage_score)
	rolling_set = counter_pop(counters, rolling_set)
	#If the player doesn't farkle:
	if stage_score:
		total_score = add_total_score(stage_score, total_score)
		player_turn_banner(player_turn)
		print("")
		score_board(stage_score, total_score, player_one_score, player_two_score, player_turn, scoring_list, rolling_set)
		#If the player has at least 500 points, they can choose to score their turn
		if total_score >= 500:
			if rolling_set:
				roll_saver = input("Save your roll or keep rolling? (save/roll):")
				if roll_saver == 'save':
					if player_turn: player_two_score += total_score
					elif not player_turn: player_one_score += total_score
					if not boolean_steal_choice(total_score, my_looper):
						total_score = reset_score(total_score)
						rolling_set = reset_rolling_set(rolling_set)
					player_turn = change_players(player_turn)
					player_turn_banner(player_turn)
			if not rolling_set:
				print("You scored all your dice!")
				rolling_set = reset_rolling_set(rolling_set)
		elif total_score < 500:
			if not rolling_set:
				print("You scored all your dice!")
				rolling_set = reset_rolling_set(rolling_set)
				
	#If the player does farkle:
	elif not stage_score:
		player_turn_banner(player_turn)
		print("")
		print("Your Roll:", scoring_list)
		farkle_no_score(total_score, player_one_score, player_two_score, rolling_set)
		print("")
		player_turn = change_players(player_turn)
		player_turn_banner(player_turn)
		print("")
		#if not boolean_steal_choice(total_score, my_looper):
		total_score = reset_score(total_score)
		rolling_set = reset_rolling_set(rolling_set)
	stage_score = reset_score(stage_score)
	my_looper = user_boolean_choice(my_looper)
	os.system('clear')
winner_printer(player_one_score, player_two_score)


		
