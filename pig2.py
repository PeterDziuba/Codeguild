import os

print('Welcome to the Pig Latin Translator!')
looper = True
lister = []

while looper:
	print('Please enter a sentence to translate:')
	pig_in = input()
	os.system('clear')
	pig_split = pig_in.split()
	for i in pig_split:
		i = i.lower()
		if i[-1] == '?':
			my_punct = '?'
			new_word = i[0:-1]
			if i[0] in ['a','e','i','o','u']:
				flip = new_word + 'yay' + my_punct
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
		lister.append(flip)
	my_lister = ' '.join(lister)
	my_lister = my_lister.capitalize()

	print(my_lister)
	lister = []
	my_lister = []

	print('')
	print('Anything else?')
	user_choice = input()
	os.system('clear')
	if user_choice == 'n': looper = False

