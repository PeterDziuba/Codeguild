import random
print("How many d6 would you like to roll?")
loops = int(input())
total = 0
total_rolls = loops
while loops > 0:
	die_num = random.randint(1, 6)
	print (die_num)
	total += die_num
	loops -= 1

print(total/total_rolls)




