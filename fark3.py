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
player_one_name = "Player One"
player_two_name = "Player Two"
player_turn = 0
steal_score = 0

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
if (player_start.lower() == 'y') or (player_start.lower() == 'yes'):
	looper_1 = True

os.system('clear')
print("Player One's Turn:")
print("")


while looper_1:
	stage_score = 0
	if steal_score: stage_score += steal_score
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
	

	if stage_score:
		if not player_turn:
			player_one_score += stage_score
		elif player_turn: 
			player_two_score += stage_score
		total_score += stage_score
		if steal_score:
			if not player_turn:
				player_one_score += steal_score
			elif player_turn:
				player_two_score += steal_score
			total_score += steal_score
	elif not stage_score:
		total_score = 0


	
	print("Your Roll:", scoring_list)
	print("Score Stolen:", steal_score)
	print('Your Score this Roll:', stage_score)
	print('Your Score this Round:', total_score)
	print('Player One Score:', player_one_score)
	print('Player Two Score:', player_two_score)
	print("")
	print("{} dice/die left to roll.".format(len(rolling_set)))
	print("")
	steal_score = 0

	if stage_score == 0:
		print('Farkle, you lose!')
		print('Continue?')
		user_choice = input()
		if user_choice == 'n':
			looper_1 = False
		os.system('clear')
		if player_turn:
			player_turn -= 1
			print("Player One's Turn:")
			if rolling_set:
				print("")
				print("Steal the dice?")
				user_steal = input()
				if user_steal == 'y':
					steal_score += total_score
				else:
					for i in range(1, 6):rolling_set.add(i)
				total_score = 0
		elif not player_turn:
			player_turn += 1
			print("Player Two's Turn:")
			if rolling_set:
				print("")
				print("Steal the dice?")
				user_steal = input()
				if user_steal == 'y':
					steal_score += total_score
				else:
					for i in range(1, 6):rolling_set.add(i)
				total_score = 0


	# hold_back_number = len(rolling_set)
	# while len(rolling_set) > 0:
	# 	rolling_set.pop()
	
	# if hold_back_number:
	# 	for i in dice_dict.keys():
	# 		rolling_set.add(i)
	total_score += stage_score
	if not rolling_set:
		print('You scored all your dice!')
		for i in dice_dict.keys(): rolling_set.add(i)



	print('Continue?')
	user_choice = input()
	if user_choice == 'n':
		looper_1 = False
	os.system('clear')
	del scoring_list[:]
	stage_score = 0
	counters = [0, 0, 0, 0, 0, 0]
	dice_dict.clear()
	dice_dict = {1 : random.randint(1, 6), 2 : random.randint(1, 6), 3 : random.randint(1, 6), 4 : random.randint(1, 6), 5: random.randint(1, 6)}
	

	



print('Rolling set:', rolling_set)
print("Scoring list:", scoring_list)
print('Counters:', counters)



#I'm keeping this code at the bottom in case I forget my logic
# print("1", rolling_set)
# for i in dice_dict.keys():
# 	if (i % 2 == 0) : rolling_set.add(i)
# print("2", rolling_set)


# for i in rolling_set:
# 	print(dice_dict[i])







