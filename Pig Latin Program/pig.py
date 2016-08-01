#Pig Latin Program
import os

print('Welcome to the Pig Latin Translator!')
your_punct = ['.,!?']
vowels = ['aeiou']

looper = True
lister = []

while looper:
	print('Please enter a sentence to translate:')
	pig_win = input()
	os.system('clear')

	question_count = pig_win.count('?')
	period_count = pig_win.count('.')
	ex_count = pig_win.count('!')
	print(pig_win[-1])
	print(pig_win[0:-1])

	if pig_win[-1] in your_punct:
		my_punct = pig_win[-1]
		pig_in = pig_win[0:-1]

	elif pig_win[-1] not in your_punct: 
		my_punct = '.'
		pig_in = pig_win

	pig_split = pig_in.split()
	for i in pig_split:
		i = i.lower()
		new_word = i[1:] + i[0:1] + 'a'
		lister.append(new_word)
	my_lister = ' '.join(lister) + my_punct
	my_lister = my_lister.capitalize()

	print(my_lister)
	my_lister = []



	print('Anything else?')
	user_choice = input()
	os.system('clear')
	if user_choice == 'n': looper = False