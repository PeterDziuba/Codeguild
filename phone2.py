import os
import time
my_book = {}

def phone_book_menu(book):
	"""This is the main menu of the phonebook."""
	os.system('clear')

	print("Would you like to add, change, delete, or lookup a number?")
	user_choice = input("add/change/delete/look:")

	if user_choice.lower() == "add": phone_number_add(book)
	elif user_choice.lower() == "change": phone_number_change(book)
	elif user_choice.lower() == "delete": phone_number_delete(book)
	elif user_choice.lower() == "look": phone_number_lookup(book)

	os.system('clear')

def phone_number_add(book):
	"""This lets the user add numbers to their phonebook."""

	print("Whose number would you like to add?")
	entry_name = input()

	if entry_name in book:
		print('That user is already in the book.',
			'Add another number for them?')
		add_another_number_choice = input("(y/n): ")
		if add_another_number_choice.lower() == 'y':
			second_user_number = input("Enter the next number: ")
			book[entry_name].append(second_user_number)

	elif entry_name not in book:
		print("What is the number for {}?".format(entry_name))
		entry_number = input()
		entry_list = []
		entry_list.append(entry_number)
		book[entry_name] = entry_list

	print("Continue?")
	user_continue = input()
	if user_continue.lower() == 'y': phone_book_menu(book)

	return book


def phone_number_change(book):
	"""This allows users to change numbers in their phonebook."""
	print("Whose number would you like to change?")
	entry_name = input()
	older_number = book[entry_name]
	if entry_name in book:
		print("Warning!: If a person has more than one number",
			"in the book, changing their number might delete",
			"all other numbers for that user.")
		print("The current listing for {} is {}.".format(entry_name, older_number))
		if len(book[entry_name]) > 1:
			print("Which number would you like to access?")
			user_index_choice = int(input("1/2/etc: "))
			user_index_choice -= 1
			print("What is the new number?")
			user_newer_number = input()
			book[entry_name][user_index_choice] = user_newer_number
		elif len(book[entry_name]) == 1:
			print("What is the new number?")
			newer_number = input()
			book[entry_name] = newer_number
	elif entry_name not in book:
		print("That user is not in our book yet.")
		print("Would you like to add them?")
		user_choice = input()
		if user_choice == "y": phone_number_add(book)
	print("Continue?")
	user_continue = input()
	if user_continue.lower() == 'y': phone_book_menu(book)
	return book

def phone_number_delete(book):
	"""This allows users to delte numbers from their phonebook."""
	print("Whose entry would you like to delte?")
	entry_name = input()
	if entry_name in book:
		older_number = book[entry_name]
		print("The current number for {} is {}.".format(entry_name, older_number))
		print("Delete {} from the book?".format(entry_name))
		user_choice = input()
		if user_choice.lower() == 'y': del book[entry_name]
	else:
		print("This number is not in our dictionary yet.")
		print("Please return to the main menu.")
	print("Continue?")
	user_continue = input()
	if user_continue.lower() == 'y': phone_book_menu(book)
	return book

def phone_number_lookup(book):
	"""This allows users to look up numbers in their phonebook."""
	print("Whose number would you like to lookup?")
	entry_name = input()
	if entry_name in book:
		entry_number = book[entry_name]
		print("{}'s number is {}.".format(entry_name, entry_number))
	elif entry_name not in book:
		print("That person is not in our phonebook yet.")
		print("Please return to the main menu.")
	print("Continue?")
	user_continue = input()
	if user_continue.lower() == 'y': phone_book_menu(book)

phone_book_menu(my_book)



