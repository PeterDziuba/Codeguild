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
looper_1 = True
counters = [0, 0, 0, 0, 0, 0]

#Score Variables
total_score = 0
stage_score = 0

#Populate the dice dictionary before the game starts
for i in dice_dict.keys():
	rolling_set.add(i)

while looper_1:
	print("Rolling Set 1", rolling_set)
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
	


	total_score += stage_score
	print('Rolling set 2:', rolling_set)
	print("Scoring list:", scoring_list)
	print('Counters:', counters)
	print('Stage score:', stage_score)
	print('Total score:', total_score)

	if stage_score == 0:
		print('Farkle, you lose!')
		quit()


	# hold_back_number = len(rolling_set)
	# while len(rolling_set) > 0:
	# 	rolling_set.pop()
	
	# if hold_back_number:
	# 	for i in dice_dict.keys():
	# 		rolling_set.add(i)
	if not rolling_set:
		print('You scored all your dice!')
		for i in dice_dict.keys(): rolling_set.add(i)



	print('Roll Again?')
	user_choice = input()
	if user_choice == 'n':
		looper_1 = False
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







