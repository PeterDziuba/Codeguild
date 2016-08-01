#This is a Magic 8-Ball Program
import os
import random
import time
os.system('clear')

print("You hear the spirits call to you as you grasp the 8-ball",
	"tightly.")
print("Do you dare to shake it?")
print('\n')
user_choice = input('yes/no:')

if user_choice == 'no':
	quit()

os.system('clear')
time.sleep(2)
print('What question will you ask?')
empty_set = input()
print('')
print('')
time.sleep(4) 
computer_choice = random.randint(1, 20)
print('Thinking...')
time.sleep(3)
print('............')
time.sleep(2)
print('.............')
time.sleep(2)
print('')
print('')

if computer_choice == 1:
	print('It is certain')
elif computer_choice == 2:
	print('It is decidedly so')
elif computer_choice == 3:
	print('Without a doubt')
elif computer_choice == 4:
	print('Yes, definitely')
elif computer_choice == 5:
	print('You may rely on it')
elif computer_choice == 6:
	print('As I see it, yes')
elif computer_choice == 7:
	print('Most likely')
elif computer_choice == 8:
	print('Outlook good')
elif computer_choice == 9:
	print('Yes')
elif computer_choice == 10:
	print('Signs point to yes')
elif computer_choice == 11:
	print('Reply hazy, try again')
elif computer_choice == 12:
	print('Ask again later')
elif computer_choice == 13:
	print('Better not tell you now')
elif computer_choice == 14:
	print('Cannot predict now')
elif computer_choice == 15:
	print('Concentrate and ask again')
elif computer_choice == 16:
	print("Don't count on it")
elif computer_choice == 17:
	print('My reply is no')
elif computer_choice == 18:
	print('My sources say no')
elif computer_choice == 19:
	print('Outlook not so good')
elif computer_choice == 20:
	print('Very doubtful')

print('')
time.sleep(5)
os.system('clear')
