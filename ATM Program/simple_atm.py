import random
import os

class CheckingAccount:
	def __init__(self, checking_balance, checking_account_number):
		self.checking_balance = int(checking_balance)
		self.checking_account_number = int(checking_account_number)

	def __eq__(self, other):
		return (self.checking_account_number == other.checking_account_number)

	def __str__(self):
		account_string = "Checking Account #: {}\nhas a balance of: {}".format(self.checking_account_number, self.checking_balance)
		return account_string

	def deposit_to_checking_account(self, deposit_amount):
		self.checking_balance += deposit_amount
		return self.checking_balance

	def withdraw_from_checking_account(self, withdrawal_amount):
		if self.checking_balance > withdrawal_amount:
			self.checking_balance -= withdrawal_amount
		elif self.checking_balance <= withdrawal_amount:
			print("You don't have enough money for this transaction.")
		return self.checking_balance

	def calculate_interest(self, interest_rate):
		interest_amount = (1 + interest_rate) * self.checking_balance
		return interest_amount

class SavingAccount:
	def __init__(self, saving_balance, saving_account_number):
		self.saving_balance = int(saving_balance)
		self.saving_account_number = int(saving_account_number)

	def __eq__(self, other):
		return (self.saving_account_number == other.saving_account_number)

	def __str__(self):
		s_account_string = "Saving Account #: {}\nhas a balance of: {}".format(self.saving_account_number, self.saving_balance)
		return s_account_string

	def deposit_to_saving_account(self, deposit_amount):
		self.saving_balance += deposit_amount
		return self.saving_balance

	def withdraw_from_saving_account(self, withdrawal_amount):
		if self.saving_balance > withdrawal_amount:
			self.saving_balance -= withdrawal_amount
		elif self.saving_balance <= withdrawal_amount:
			print("You don't have enough money for this transaction.")
		return self.saving_balance

	def calculate_interest(self, interest_rate):
		interest_amount = (1 + interest_rate) * self.saving_balance
		return interest_amount

class Person:
	def __init__(self, name, checking_account, saving_account):
		self.name = name
		self.saving_account = saving_account
		self.checking_account = checking_account

	def __eq__(self, other):
		return (self.saving_account == other.saving_account) and (self.checking_account == other.checking_account)

	def __str__(self):
		my_string = self.name
		return my_string

peter_checking_account = CheckingAccount(5000, 503)





peter_saving_account = SavingAccount(20000, 541)
peter = Person('Peter', peter_checking_account, peter_saving_account)

def atm_menu(loop_bool):
	print("Deposit/Withdraw/Balance/Interest?")
	user_choice = input(': ')

	if user_choice.lower() == 'deposit':

		print("Savings or Checking?")
		user_savings_or_checking = input(": ")
		print('How much would you like to deposit?')
		user_deposit_amount = int(input(": "))

		if user_savings_or_checking.lower() == 'checking':

			peter.checking_account.deposit_to_checking_account(user_deposit_amount)
			print(peter.checking_account)

		elif user_savings_or_checking.lower() == 'savings':

			peter.saving_account.deposit_to_saving_account(user_deposit_amount)
			print(peter.saving_account)

	elif user_choice.lower() == 'withdraw':

		print("Savings or Checking?")
		user_savings_or_checking = input(": ")
		print('How much would you like to withdraw?')
		user_withdraw_amount = int(input(": "))

		if user_savings_or_checking.lower() == 'checking':
			peter.checking_account.withdraw_from_checking_account(user_withdraw_amount)
			print(peter.checking_account)

		elif user_savings_or_checking.lower() == 'savings':
			peter.saving_account.withdraw_from_saving_account(user_withdraw_amount)
			print(peter.saving_account)

	elif user_choice.lower() == 'balance':

		print("Savings or Checking?")
		user_savings_or_checking = input(": ")

		if user_savings_or_checking.lower() == 'checking':
			print(peter.checking_account)

		elif user_savings_or_checking.lower() == 'savings':
			print(peter.saving_account)

	elif user_choice.lower() == 'interest':

		print("Savings or Checking?")
		user_savings_or_checking = input(": ")

		if user_savings_or_checking.lower() == 'checking':
			check_interest = peter.checking_account.calculate_interest(0.005)
			print(check_interest)

		elif user_savings_or_checking.lower() == 'savings':
			save_interest = peter.saving_account.calculate_interest(0.005)
			print(save_interest)

	user_continue = input('Continue?')
	if user_continue == 'n': loop_bool = False
	os.system('clear')
	return loop_bool


loop_bool = True
while loop_bool:
	loop_bool = atm_menu(loop_bool)

