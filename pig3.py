#This is a Pig Latin Translation Program
import os
looper = True

def pig_split(pig_string):
	"""This function splits the sentence into words."""
	pig_string = str(pig_string)
	split_pig_string = pig_string.split()
	return split_pig_string

def pig_translate(split_pig_string):
	"""This function translates each word into pig latin."""
	my_punct_list = ['?', '.', ',', '!', ':']
	my_vowels = ['a', 'e', 'i', 'o', 'u']
	lister = []
	for i in split_pig_string:
		i = i.lower()
		if i[-1] in my_punct_list:
			my_punct = i[-1]
			new_word = i[0:-1]
			if i[0] in my_vowels:
				flip = new_word + 'yay' + my_punct
			else:
				flip = new_word[1:] + new_word[0:1] + 'a' + my_punct
		elif i[-1] not in my_punct_list:
			new_word = i
			if i[0] in my_vowels:
				flip = new_word + 'yay'
			else: flip = new_word[1:] + new_word[0:1] + 'a'
		lister.append(flip)
	return lister

def pig_joiner(lister):
	"""This function joins the translated words into a sentence."""
	my_lister = ' '.join(lister)
	my_lister = my_lister.capitalize()
	return my_lister

def pig_printer(my_lister):
	"""This function prints the translated sentence."""
	print(my_lister)



def main_pig():
	"""This function takes the user sentence, passes it to the translator
	and returns the new sentence."""
	english_in = input("Enter a Sentence for Translation:")
	return english_in
	
while looper:
	english_in = main_pig()
	#print("English in:", english_in)
	split_pig_string = pig_split(english_in)
	#print("Split Pig String:", split_pig_string)
	lister = pig_translate(split_pig_string)
	#print("Lister:", lister)
	my_lister = pig_joiner(lister)
	#print("My Lister:", my_lister)
	pig_printer(my_lister)
	user_choice = input("Translate another sentence?: ")
	if user_choice == 'n': looper = False

