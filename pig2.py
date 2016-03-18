#This is a Pig Latin Translation Program
import os #I import the os so that we can clear the terminal

#Welcome the user
print('Welcome to the Pig Latin Translator!')

looper = True #This variable will close the loop.
lister = []   #This list stores the new 'pig' version of the sentence.

while looper:
	print('Please enter a sentence to translate:')
	pig_in = input()
	os.system('clear')
	pig_split = pig_in.split() #We split the string so that we can
							   #look at it word-by-word.
	for i in pig_split: 	  #Here we iterate over each word.
		i = i.lower()		
		if i[-1] == '?':	#Compare last char in string to '?'
			my_punct = '?'
			new_word = i[0:-1] #Store the string without last char
			if i[0] in ['a','e','i','o','u']: #Compare first char to vowels
				flip = new_word + 'yay' + my_punct #Build a pig latin word
			else:	
				flip = new_word[1:] + new_word[0:1] + 'a' + my_punct
		elif i[-1] == '!':
			my_punct = '!'
			new_word = i[0:-1]
			if i[0] in ['a','e','i','o','u']:
				flip = new_word + 'yay' + my_punct
			else:	
				flip = new_word[1:] + new_word[0:1] + 'a' + my_punct
		elif i[-1] == '.':
			my_punct = '.'
			new_word = i[0:-1]
			if i[0] in ['a','e','i','o','u']:
				flip = new_word + 'yay' + my_punct
			else:	
				flip = new_word[1:] + new_word[0:1] + 'a' + my_punct
		elif i[-1] == ',':
			my_punct = ','
			new_word = i[0:-1]
			if i[0] in ['a','e','i','o','u']:
				flip = new_word + 'yay' + my_punct
			else:	
				flip = new_word[1:] + new_word[0:1] + 'a' + my_punct
		else:
			new_word = i
			if i[0] in ['a','e','i','o','u']:
				flip = new_word + 'yay'
			else:	
				flip = new_word[1:] + new_word[0:1] + 'a'
		lister.append(flip) #Add our new pig latin word to the lister
	my_lister = ' '.join(lister) #Convert the lister to a string
	my_lister = my_lister.capitalize() #Capitalize the sentence

	print(my_lister) #Print out the new sentence
	lister = [] #Empty our lists so that we can do another sentence
	my_lister = []

	print('')
	print('Anything else?')
	user_choice = input()
	os.system('clear')
	if user_choice == 'n': looper = False #Let the user quit

