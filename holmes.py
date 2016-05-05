#This is going to be my text manipulation program.
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
	my_punct = ['.', '?', '!', ',', '/', '\\']
	for i in lower_case_word_list:
		if i[-1] in my_punct:
			i = i[:-1]
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
	# return counted_dict

def pair_listing_funct(final_word_list):
	"""This function will count unique pairs."""
	pair_list = []
	for i in range(len(final_word_list) - 1):
		final_word_list[i] = final_word_list[i] + " " + final_word_list[i+1]
		pair_list.append(final_word_list[i])
	return pair_list

def dict_word_probability_counting_machine(final_word_list, total_words):
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



line_list = read_file('holmes.txt')
final_word_list = master_key_machine(line_list)
dict_word_count = dict_word_counting_machine(final_word_list)
list_word_count = sorted(dict_word_count, key=dict_word_count.get, reverse=True)
# print("Line List: ", line_list)
# print("Word List: ", word_list)
# print("Lower Case Word List: ", lower_case_word_list)
# print("Punctuation Stripped: ", final_word_list)
# print("Dict Word Count: ", dict_word_count)
# print("List Word Count: ", list_word_count)
dict_sort_printer(dict_word_count, list_word_count)

pair_list = pair_listing_funct(final_word_list)
# print(pair_list)
pair_count = dict_word_counting_machine(pair_list)
list_pair_count = sorted(pair_count, key=pair_count.get, reverse=True)
dict_sort_printer(pair_count, list_pair_count)
#print("Counted Dict: ", counted_dict)
total_words = total_counting_function(final_word_list)
total_pairs = total_counting_function(pair_list)
print(total_words)
print(total_pairs)

another_word_list = master_key_machine(line_list)
dict_probability_count = dict_word_probability_counting_machine(another_word_list, total_words)
list_prob_count = sorted(dict_probability_count, key=dict_probability_count.get, reverse=True)
dict_sort_printer(dict_probability_count, list_prob_count)
another_pair_list = pair_listing_funct(another_word_list)
pair_prob_count = dict_word_probability_counting_machine(another_pair_list, total_pairs)
pair_list_prob_count = sorted(pair_prob_count, key=pair_prob_count.get, reverse=True)
dict_sort_printer(pair_prob_count, pair_list_prob_count)

a_third_word_list = master_key_machine(line_list)
a_fourth_word_list = pair_listing_funct(a_third_word_list)
a_fifth_word_list = []
for words in a_fourth_word_list:
	if 'of ' in words[0:3]:
		a_fifth_word_list.append(words)
total_of = total_counting_function(a_fifth_word_list)
of_probability_count = dict_word_probability_counting_machine(a_fifth_word_list, total_of)
my_var = sorted(of_probability_count, key=of_probability_count.get, reverse=True)
dict_sort_printer(of_probability_count, my_var)
# list_of_of = []

# for words in pair_prob_count:
# 	if 'of ' in words[0:3]:
# 		list_of_of.append(words)
# total_of = total_counting_function(list_of_of)
# dict_of = dict_word_probability_counting_machine(list_of_of, total_of)
# of_of_prob_count = dict_word_probability_counting_machine(list_of_of, total_of)

# dict_sort_printer(dict_of, my_var)
