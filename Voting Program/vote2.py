#This is a voting program
import os
my_poll_dict = {}
continue_while_true_bool = True

def vote_for_candidate(poll_dict):
	"""This will allow the user to enter their vote."""
	
	user_vote = input("Who will you vote for?\n: ")
	
	if user_vote in poll_dict:
		poll_dict[user_vote] += 1
	else:
		poll_dict[user_vote] = 1

	os.system('clear')
	return poll_dict

def display_poll(poll_dict):
	"""This will display the current polling numbers."""
	print(poll_dict.items())

def poll_choice(poll_dict, continue_while_true_bool):
	"""This will allow the user to choose between voting and displaying the poll."""
	
	print("Vote, Show Current Polls, or Quit?")
	user_choice = input("Enter Vote/Polls/Quit:")

	if user_choice.lower() == "vote":
		os.system('clear')
		vote_for_candidate(poll_dict)

	elif user_choice.lower() == "polls":
		os.system('clear')
		if my_poll_dict:
			display_poll(poll_dict)

	elif user_choice.lower() == "quit":
		continue_while_true_bool = False

	return continue_while_true_bool

def calculate_and_print_winner(poll_dict):
	"""This function will return the winning candidate."""
	voting_winner = max(poll_dict, key=poll_dict.get)
	return voting_winner

while continue_while_true_bool:
	continue_while_true_bool = poll_choice(my_poll_dict, continue_while_true_bool)


voting_winner = calculate_and_print_winner(my_poll_dict)

print("Final Voting Numbers: ", my_poll_dict)
print("The winner is: ", voting_winner)