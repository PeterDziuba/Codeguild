import random
import os
dict_of_atm_users = {}

class BankAccount:
	def __init__(self, user_name, account_number, balance):
		self.user_name = user_name
		self.account_number = account_number
		self.balance = int(balance)

	def __str__(self):
		my_string = "{}'s account number {} has a balance of {}.".format(self.account_number, self.user_name, self.balance)
		return my_string

	def deposit(self, deposit_amount):
		deposit_amount = int(deposit_amount)
		self.balance += deposit_amount
		return self.balance

	def withdraw(self, withdraw_amount):
		if self.balance > withdraw_amount:
			self.balance -= withdraw_amount
		else: print("Insufficient Funds!")
		return self.balance

	def display_interest(self):
		my_interest = (1.005 * self.balance)
		return my_interest

	def get_standing(self):
		if self.balance < 1000: return False
		elif self.balance >= 1000: return True

def cast_account_to_dict(bank_account, dict):
	my_name = bank_account.user_name
	my_number = bank_account.account_number
	my_balance = bank_account.balance
	my_list = [my_name, my_balance]
	dict[my_number] = my_list
	return dict

def user_continue():
	user_keep_going = input('Continue?')
	if user_keep_going.lower() == 'n': quit()

def query_dict_for_account(user_query, dict):
	if user_query in dict.keys():
		my_user_query = BankAccount(dict[user_query][0], user_query, dict[user_query][1])
		return my_user_query
	else: print("We don't have a listing for you. Sorry, we're new at this banking thing.")

def atm_menu(dict_of_atm_users):
	"""This is the main menu of the atm."""

	print("Hello, and welcome to bank of the Northwest!")
	print("Please enter your account number. If you do not have one, please type 'new'.")
	user_account_number = input(": ")

	if user_account_number.lower() == 'new':

		new_account_name = input("Please enter your name\n: ")
		new_account_balance = int(input("How much money would you like to put in your account?\n: "))
		new_account_number = random.randint(1, 10000)
		print("The account for {}, number {}, is being set up with a balance of {}".format(new_account_name, new_account_number, new_account_balance))
		print("Remember your account number. It's how you will access your account in the future.")
		new_user_account = BankAccount(new_account_name, new_account_number, new_account_balance)
		dict_of_atm_users = cast_account_to_dict(new_user_account, dict_of_atm_users)
		user_continue()

	elif user_account_number.lower != 'new':

		user_account_number = int(user_account_number)
		current_user_account = query_dict_for_account(user_account_number, dict_of_atm_users)

		if not current_user_account.get_standing():

			print("Your account balance is too low.")
			print("You will be assessed a $50 fee.")
			current_user_account.withdraw(50)
			print(current_user_account)
			dict_of_atm_users = cast_account_to_dict(current_user_account, dict_of_atm_users)

		print("Deposit, Withdraw, Check Balance, or Calculate Interest?")
		user_control_flow = input("Deposit/Withdraw/Balance/Interest?: ")

		if user_control_flow.lower() == 'deposit':

			print("How much would you like to deposit?")
			user_deposit_amount = int(input(": "))
			current_user_account.deposit(user_deposit_amount)
			print(current_user_account)
			dict_of_atm_users = cast_account_to_dict(current_user_account, dict_of_atm_users)
			user_continue()

		elif user_control_flow.lower() == 'withdraw':

			print("How much would you like to withdraw?")
			user_withdraw_amount = int(input(": "))
			current_user_account.withdraw(user_withdraw_amount)
			print(current_user_account)
			dict_of_atm_users = cast_account_to_dict(current_user_account, dict_of_atm_users)
			user_continue()

		elif user_control_flow.lower() == 'balance':

			print(current_user_account)
			user_continue()

		elif user_control_flow.lower() == 'interest':

			print(current_user_account.display_interest())
			user_continue()

	os.system('clear')
	
	return dict_of_atm_users

loop_bool = True

while loop_bool:

	dict_of_atm_users = atm_menu(dict_of_atm_users)



