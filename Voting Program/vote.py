election = {} #The election dictionary will hold all the votes.
vote = True   #The vote variable will stop the loop when all
			  #votes are in.

#The Vote loop will take in votes.			  
while vote:
	#We ask the user if they want to vote.
	print("Would you like to vote?")
	choice = input()
	if (choice == 'yes') | (choice == "Yes") | (choice == "y"):
		#This adds votes to the total count and/or 
		#adds candidates to the election dictionary.
		print("Who would you like to vote for?")
		answer = input()
		if answer in election:
			election[answer] += 1
		else:
			election[answer] = 1
	else:#This allows the user to stop voting when they are done.
		vote = False


print(election) #This prints out all the votes at the end!
winner = (max(election, key=election.get, default="No one"))
sorter = (sorted(election, key=election.get, reverse=True))
print(winner, "wins!")
print(sorter)