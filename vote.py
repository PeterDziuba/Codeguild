election = {"Kyle":0, "Peter":0, "Jeff":0}
vote = True

while vote:
	print("Would you like to vote?")
	choice = input()
	if (choice != 'n'):
		print("Who would you like to vote for?")
		answer = input()
		if answer in election:
			election[answer] += 1
	else: 
		vote = False

print(election)