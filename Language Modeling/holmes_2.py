#This second version of my text manipulation program should allow
#the user to enter one word. The program will return the most likely
#word to follow that in the source text.

def total_counting_function(list):
	"""This counts the number of elements in a list."""
	word_count = 0
	for i in list:
		word_count += 1
	return word_count


def read_file(file):
	"""This reads open the file."""
	line_list = []
	with open(file) as my_file:
		for line in my_file:
			line_list.append(line.strip())
	return line_list

def word_list(line_list):
	"""Hopefully this separates the lines into words."""
	word_list = []
	for i in line_list:
		word_list.append(i.split())
	return word_list

def lower_case_machine(word_list):
	"""This lower-cases all of our words"""
	lower_case_word_list = []
	for i in word_list:
		for sub_i in i:
			lower_case_word_list.append(sub_i.lower())
	return lower_case_word_list

def punctuation_stripper(lower_case_word_list):
	"""This will strip the punctuation off, Andrew"""
	final_word_list = []
	my_punct = ['.', '?', '!', ',', '/', '\\', '"', '*']
	for i in lower_case_word_list:
		if i[-1] in my_punct:
			i = i[:-1]
		if i[0] in my_punct:
			i = i[1:]
		final_word_list.append(i)

	return final_word_list

def dict_word_counting_machine(final_word_list):
	"""This will count the individual unique words."""
	dict_word_count = {}
	for i in final_word_list:
		if i in dict_word_count:
			dict_word_count[i] += 1
		elif i not in dict_word_count:
			dict_word_count[i] = 1
	return dict_word_count

def dict_sort_printer(dict_word_count, list_word_count):
	for i in list_word_count[:10]:
		print(i[:10], dict_word_count[i])

def pair_listing_funct(final_word_list):
	"""This function will count unique pairs."""
	pair_list = []
	for i in range(len(final_word_list) - 1):
		final_word_list[i] = final_word_list[i] + " " + final_word_list[i+1]
		pair_list.append(final_word_list[i])
	return pair_list

def dict_word_probability_counting_machine(final_word_list, total_words):
	"""This function takes a list of words. It places them into a dict
	and assigns the value as the number of times that word appeared in
	the first list."""
	dict_prob_count = {}
	for i in final_word_list:
		if i in dict_prob_count:
			dict_prob_count[i] += 1
		elif i not in dict_prob_count:
			dict_prob_count[i] = 1
	for i in dict_prob_count:
		dict_prob_count[i] = (dict_prob_count[i]/total_words)
	return dict_prob_count

def master_key_machine(line_list):
	"""This function runs a bunch of other functions."""
	word_lister = word_list(line_list)
	lower_case_word_list = lower_case_machine(word_lister)
	final_word_list = punctuation_stripper(lower_case_word_list)
	return final_word_list

def user_word_appender(user_word, my_pair_list):
	"""This function will create a list of pairs that
	begin with the user's word."""
	user_word_list = []
	for pair in my_pair_list:
		if user_word in pair[0:len(user_word)]:
			user_word_list.append(pair)
	return user_word_list

def main():
	"""This will be the main body of the program."""
	file = input("What file would you like to access?: ")
	line_list = read_file(file)
	final_word_list = master_key_machine(line_list)
	my_pair_list = pair_listing_funct(final_word_list)
	user_word = input('What word would you like to start with?')
	if " " not in user_word:
		user_word = user_word + " "
	user_word_list = user_word_appender(user_word, my_pair_list)
	total_user_word_count = total_counting_function(user_word_list)
	user_word_probability = dict_word_probability_counting_machine(user_word_list, total_user_word_count)
	sorted_user_word_list = sorted(user_word_probability, key=user_word_probability.get, reverse=True)
	dict_sort_printer(user_word_probability, sorted_user_word_list)

main()
