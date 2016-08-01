def read_file(file):
	file_list_stripped = []
	with open(file) as my_file:
		file_list_unstripped = my_file.readlines()
	for line in file_list_unstripped:
		file_list_stripped.append(line.strip())
	return file_list_stripped

def make_lines_into_words(list):
	word_list = []
	for i in list:
		word_list.append(i.split())
	return word_list

def down_case(list):
	lower_case_word_list = []
	for i in list:
		for sub_i in i:
			lower_case_word_list.append(sub_i.lower())
	return lower_case_word_list

def strip_punctuation(list):
	no_punct_list = []
	my_punct_list = ['.', '?', '!', ',', '/', '\\', ':', '"', "'", ';']
	for i in list:
		if i[-1] in my_punct_list:
			i = i[:-1]
		no_punct_list.append(i)
	return no_punct_list

def make_a_dict(list):
	word_count_dict = {}
	for i in list:
		if i in word_count_dict:
			word_count_dict[i] += 1
		elif i not in word_count_dict:
			word_count_dict[i] = 1
	return word_count_dict

def print_first_ten_list_items(list, dict):
	for i in list[:10]:
		print(i, dict[i])

def pair_listing_funct(list):
	"""This function will count unique pairs."""
	pair_list = []
	for i in range(len(list) - 1):
		list[i] = list[i] + " " + list[i+1]
		pair_list.append(list[i])
	return pair_list

def triple_listing_funct(list):
	"""This doesn't work the way I want it to."""
	triple_list = []
	for i in range(len(list) - 2):
		list[i] = list[i] + " " + list[i+1] + " " + list[i+2]
		triple_list.append(list[i])
	return triple_list

def sort_for_user_word(user_word, my_pair_list):
	"""This function will create a list of pairs that
	begin with the user's word."""
	user_word_list = []
	for pair in my_pair_list:
		if user_word in pair[0:len(user_word)]:
			user_word_list.append(pair)
	return user_word_list

hamlet_stripped = read_file('/Users/htdzi/Documents/codeguild/hamlet.txt')
words_of_hamlet = make_lines_into_words(hamlet_stripped)
lower_case_hamlet = down_case(words_of_hamlet)
no_punct_hamlet = strip_punctuation(lower_case_hamlet)
hamlet_word_count_dict = make_a_dict(no_punct_hamlet)
most_common_list = sorted(hamlet_word_count_dict, key=hamlet_word_count_dict.get, reverse=True)

#Debugging Prints:
# print(words_of_hamlet[:50])
# print(lower_case_hamlet[:50])
# print(no_punct_hamlet[:50])
# print(hamlet_word_count_dict)

print("")
print("The ten most common words are:")
print_first_ten_list_items(most_common_list, hamlet_word_count_dict)
print("")

hamlet_pairs = pair_listing_funct(no_punct_hamlet)
hamlet_pair_dict = make_a_dict(hamlet_pairs)
most_common_pairs = sorted(hamlet_pair_dict, key=hamlet_pair_dict.get, reverse=True)
print_first_ten_list_items(most_common_pairs, hamlet_pair_dict)
print("")

#Debugging Prints:
#print(hamlet_pairs[:50])

user_word = input('What word would you like to start with?')
if " " not in user_word:
	user_word = user_word + " "

user_pair_list = sort_for_user_word(user_word, hamlet_pairs)
user_pair_dict = make_a_dict(user_pair_list)
most_common_user_pairs = sorted(user_pair_dict, key=user_pair_dict.get, reverse=True)
print_first_ten_list_items(most_common_user_pairs, user_pair_dict)

