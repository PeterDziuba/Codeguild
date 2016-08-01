import os
phonebook = {} #The phonebook is our dictionary.
looper = True  #The looper variable allows people to do
			   #more than one thing
#Welcome the user!
print("Welcome to the Rose City Phone Guide!")

#Our main loop
while looper:
	#Let the user choose which task to perform.
	print("Would you like to add a name and phone number,",
		"change a phone number, lookup a phone number, or",
		"list all the names? Type add/change/lookup/list.")
	print("If you would like to see the whole book, type 'book'.")
	user_choice = input()
	os.system('clear')
	#If the user wants to add a name and number:
	if user_choice == "add":
		print("Please enter the name of the person you",
			"would like to add:")
		user_name = input()
		print("What number should we associate with", user_name + "?")
		user_number = input()
		phonebook[user_name] = user_number
		print("Thank you!")
		print("Would you like to do anything else?")
		user_choice2 = input()
		os.system('clear')
		if user_choice2 == "n":
			looper = False

	#If the user wants to change a pre-existing number:
	if user_choice == "change":
		print("Whose number would you like to change?")
		user_name = input()
		if user_name not in phonebook:
			print("That user is not in the book yet. Please",
				"select 'add'.")
		else:
			print("The number for", user_name, "is currently",
				user_number + ". What is the new number?")
			user_number = input()
			phonebook[user_name] = user_number
		print("Thank you!")
		print("Would you like to do anything else?")
		user_choice2 = input()
		os.system('clear')
		if user_choice2 == "n":
			looper = False

	#If the user wants to lookup a number:
	if user_choice == "lookup":
		print("Whose number would you like to search?")
		user_name = input()
		if user_name not in phonebook:
			print("That user is not in the book yet. I'm sorry.")
		else:
			print(user_name + "'s number is", phonebook[user_name] + ".")	
		print("Thank you!")
		print("Would you like to do anything else?")
		user_choice2 = input()
		os.system('clear')
		if user_choice2 == "n":
			looper = False

	#If the user wants to see all the names in the book:
	if user_choice == "list":
		print(sorted(phonebook))
		print("Thank you!")
		print("Would you like to do anything else?")
		user_choice2 = input()
		os.system('clear')
		if user_choice2 == "n":
			looper = False

	if user_choice == "book":
		print(sorted(phonebook.items()))
		print("Thank you!")
		print("Would you like to do anything else?")
		user_choice2 = input()
		os.system('clear')
		if user_choice2 == "n":
			looper = False


