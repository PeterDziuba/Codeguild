#I import the os and time modules
#so that I can make the program 
#more readable for the user.
import os
import time

print("Welcome to Madlibs")

user_adjective_one = input("Please give us an adjective: ")
print("Great thank you!")

user_adjective_two = input("Please give us another adjective: ")
print("Alright, that's great!")

user_room = input("Please give us the name of a room(kitchen, bedroom, etc): ")
print("Thanks! That's all we need")

print("Your Madlib is coming soon!")

time.sleep(1)
os.system('clear')

print("No Christmas season can be really {} unless".format(user_adjective_one),
	"you have a/an {} tree in your {}.".format(user_adjective_two, user_room))