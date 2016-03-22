#Farkle me Timberrsss!
import os
import time
import random

#I store my dice in a dictionary so that I can keep track of which to roll.
dice_dict = {1 : random.randint(1,6), 2 : random.randint(1,6), 3 : random.randint(1,6),
4 : random.randint(1,6), 5 : random.randint(1,6)}
rolling_set = set()
scoring_list = []
hold_back_number = 0
looper_1 = False
counters = [0, 0, 0, 0, 0, 0]

#Score Variables
total_score = 0
stage_score = 0
player_one_score = 0
player_two_score = 0
player_turn = 0

#Populate the dice dictionary before the game starts
for i in dice_dict.keys():
	rolling_set.add(i)

print("Welcome to Farkle:")
print("A Dumb Game with Dice.")
time.sleep(1)
print('...')
time.sleep(1)
print('Begin?')
player_start = input("y/n:")
time.sleep(1)
if (player_start.lower() == 'y') or (player_start.lower() == 'yes'):
	looper_1 = True

os.system('clear')
print("Player One's Turn:")
print("")


while looper_1:
	stage_score = 0
	os.system('clear')
	if not player_turn:
		print("Player One's Roll")
		print("")
	elif player_turn:
		print("Player Two's Roll")
		print("")
	print("Rolling {} dice/die:".format(len(rolling_set)))
	print("")
	#Here we add the rolling dice to the scoring list.
	#This gives us a snapshot of the die values.
	if rolling_set:
		for i in rolling_set: 
			scoring_list.append(dice_dict[i]) 
	#These counters tell us how many of each die
	#we have.
	for i in scoring_list:
		if 1 == i: counters[0] += 1
		if 2 == i: counters[1] += 1
		if 3 == i: counters[2] += 1
		if 4 == i: counters[3] += 1
		if 5 == i: counters[4] += 1
		if 6 == i: counters[5] += 1

	#And now we write the awful nested if loops for scoring:
	if counters[0] == 3:
		stage_score += 1000
		for i in range(3):
			if rolling_set:
				rolling_set.pop()
	elif counters[0] < 3:
		stage_score += (100 * counters[0])
		for i in range(counters[0]):
			if rolling_set:
				rolling_set.pop()
	elif counters[0] > 3:
		stage_score += 1000
		stage_score += 100 * (counters[0] - 3)
		for i in range(counters[0]):
			if rolling_set:
				rolling_set.pop()
	if counters[1] >= 3:
		stage_score += 200
		for i in range(3):
			if rolling_set:
				rolling_set.pop()
	if counters[2] >= 3:
		stage_score += 300
		for i in range(3):
			if rolling_set:
				rolling_set.pop()
	if counters[3] >= 3:
		stage_score += 400
		for i in range(3):
			if rolling_set:
				rolling_set.pop()
	if counters[4] == 3:
		stage_score += 500
		for i in range(3):
			if rolling_set:
				rolling_set.pop()
	elif counters[4] > 3:
		stage_score += 500
		stage_score += (50 * (counters[4] - 3))
		for i in range(counters[3]):
			if rolling_set:
				rolling_set.pop()
	elif counters[4] < 3:
		stage_score += (50 * (counters[4]))
		for i in range(counters[4]):
			if rolling_set:
				rolling_set.pop()
	if counters[5] >= 3:
		stage_score += 600
		for i in range(3):
			if rolling_set:
				rolling_set.pop()
	
	

	#Fixed Scoring Control Flow
	if stage_score == 0:
		print('Farkle, you lose!')
		print('Stealable Score:', total_score)
		print('Player One Score:', player_one_score)
		print('Player Two Score:', player_two_score)
		print('')
		print("{} dice/die left to roll.".format(len(rolling_set)))

		if player_turn:
			print("Player One's Turn")
			player_turn -= 1
		elif not player_turn:
			print("Player Two's Turn")
			player_turn += 1

		if total_score >= 500:
			if rolling_set:
				print("Would you like to steal the dice?")
				user_steal = input('y/n:')
				if user_steal == 'y':
					print("You stole {} die/dice!".format(len(rolling_set)))
					print("Rolling with {} points!".format(total_score))
				elif user_steal == 'n':
					for i in range(1, 6):rolling_set.add(i)
					total_score = 0
			else:
				print("Continue?")
				user_choice = input("y/n:")
				time.sleep(1)
				if user_choice == 'n': looper_1 = False

	elif stage_score > 0:
		total_score += stage_score
		print("Your Roll:", scoring_list)
		print('Your Score this Roll:', stage_score)
		print('Your Score this Round:', total_score)
		print('Player One Score:', player_one_score)
		print('Player Two Score:', player_two_score)
		print("")
		print("{} dice/die left to roll.".format(len(rolling_set)))
		print("")
		if total_score < 500:
			if rolling_set:
				print("Keep rolling?")
				user_choice = input('y/n:')
				time.sleep(1)
				if user_choice == 'n':
					looper_1 = False
			elif not rolling_set:
				print("Sorry, score too low to continue.")
				if player_turn:
					print("Player One's Turn")
					player_turn -= 1
				elif not player_turn:
					print("Player Two's Turn")
					player_turn += 1
				total_score = 0
				print("Continue?")
				user_choice = input("y/n:")
				time.sleep(1)
				if user_choice == "n":
					looper_1 = False
				for i in range(1, 6):rolling_set.add(i)
		elif total_score >= 500:
			if rolling_set:
				print("Roll again or save your score?")
				user_continue = input("Roll/Save:")
				time.sleep(1)
				if user_continue.lower() == 'save':
					if player_turn:
						player_two_score += total_score
						player_turn -= 1
						total_score = 0
						for i in range(1, 6):rolling_set.add(i)
					elif not player_turn:
						player_one_score += total_score
						player_turn += 1
						total_score = 0
						for i in range(1, 6):rolling_set.add(i)
				elif user_continue.lower() == 'roll':
					print("Ready?")
					user_choice = input("y/n:")
					if user_choice == "n": looper_1 = False
			elif not rolling_set:
				print("You scored all your dice!")
				print("Roll again?")
				time.sleep(1)
				user_choice = input()
				if user_choice == 'n': looper_1 = False
				for i in range(1, 6):rolling_set.add(i)

		#Keep coding here




	os.system('clear')
	del scoring_list[:]
	stage_score = 0
	counters = [0, 0, 0, 0, 0, 0]
	dice_dict.clear()
	dice_dict = {1 : random.randint(1, 6), 2 : random.randint(1, 6), 3 : random.randint(1, 6), 4 : random.randint(1, 6), 5: random.randint(1, 6)}
	
players = {"Player One": player_one_score, "Player Two": player_two_score}
winner = (max(players, key=winner.get, default="No one"))

print("Player One's Final Score: {}".format(player_one_score))
print("Player Two's Final Score: {}".format(player_two_score))
print(winner, "wins!")
winners = (max(election, key=election.get, default="No one"))


