import urllib.request
import os
import random
cheese_list = []
dates = ['01', '02', '03', '04', '05', '06', '07',
'08', '09', '10', '11', '12', '13', '14', '15', '16',
'17', '18', '19', '20', '21', '22', '23', '24', '25', 
'26', '27', '28', '29', '30', '31']
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

def monthly_sorter(month, word_list):
	master_list = []
	for i in word_list:
		if month in i:
			master_list.append(i)
	return master_list

def not_your_average_dictionary(dict, dates, months):
	average_dict = {}
	for k, v in dict.items():
		for date in dates:
			for month in months:
				if k.startswith('{}-{}'.format(date, month)):
					key = ('{}-{}'.format(date, month))
					if key not in average_dict.keys():
						average_dict[key] = (v/14)
					else: average_dict[key] += (v/14)
	return average_dict

def dict_probability_calc(average_dict, fancy_count):
	probably_dict = {}
	for k, v in average_dict.items():
		if fancy_count != 0:
			new_v = (v/7)
			probably_dict[k] = (new_v)
	return probably_dict


def read_site(site):
	"""This reads open the file."""
	line_list = []
	with urllib.request.urlopen(site) as my_site:
		for line in my_site:
			line_list.append(line.strip().decode('utf-8'))
	return line_list[11:-1]

def list_length_normalizer(list):
	new_list = []
	for line in list:
		new_list.append(line[:17])
	return new_list

def user_search(list):
	my_list = []
	user_year = input("What year would you like to search?\nIf none, enter '-': ")
	user_month = input("What month or date would you like to search?\nIf none, enter '-': ")
	for i in list:
		if (user_year in i.lower()) and (user_month in i.lower()):
			my_list.append(i)
	return my_list

def list_sorting_machine(list):
	sort_list = sorted(list, key=lambda x: x[1], reverse=True)
	my_max_value = sort_list[0]
	return my_max_value

def list_value_counter(list):
	total_count = 0
	for k, v in list:
		total_count += v
	return total_count

def probability_machine(list, total_count):
	my_probability = (total_count/(len(list)))
	return my_probability

def create_dict(data_list_tuple):
	dict = {x: y for x, y in data_list_tuple}
	return dict


def blank_space_remover(list):
	blank_list = []
	for i in list:
		while "  " in i:
			i = i.replace("  ", " ")
		i = i.replace(" ", ",")
		blank_list.append(i)
	return blank_list

def list_split_machine(list):
	split_list = []
	for i in list:
		split_list.append(i.split(','))
	return split_list

def int_maker(list):
	int_list = []
	for i in list:
		if i[1] == '-': i[1] = 0
		else: i[1] = int(i[1])
		int_list.append(i)
	return int_list

def fancy_key_counter(dict, list):
	fancy_count = 0
	for i in list:
		if i in dict.keys():
			fancy_count += 1
	return fancy_count

def list_manager(user_list):
	"""This function will run all of the list transformation functions
	and output a processed list."""
	normalized_user_list = list_length_normalizer(user_list)
	blanks_removed_list = blank_space_remover(normalized_user_list)
	split_user_list = list_split_machine(blanks_removed_list)
	integer_user_list = int_maker(split_user_list)
	return integer_user_list


unmodified_website_data = read_site('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain')
for line in unmodified_website_data:
	cheese_list.append(line[:17])
#Store the monthly data
first_jan_list = monthly_sorter('JAN', cheese_list)
first_feb_list = monthly_sorter('FEB', cheese_list)
first_mar_list = monthly_sorter('MAR', cheese_list)
first_apr_list = monthly_sorter('APR', cheese_list)
first_may_list = monthly_sorter('MAY', cheese_list)
first_jun_list = monthly_sorter('JUN', cheese_list)
first_jul_list = monthly_sorter('JUL', cheese_list)
first_aug_list = monthly_sorter('AUG', cheese_list)
first_sep_list = monthly_sorter('SEP', cheese_list)
first_oct_list = monthly_sorter('OCT', cheese_list)
first_nov_list = monthly_sorter('NOV', cheese_list)
first_dec_list = monthly_sorter('DEC', cheese_list)
jan_list = list_manager(first_jan_list)
feb_list = list_manager(first_feb_list)
mar_list = list_manager(first_mar_list)
apr_list = list_manager(first_apr_list)
may_list = list_manager(first_may_list)
jun_list = list_manager(first_jun_list)
jul_list = list_manager(first_jul_list)
aug_list = list_manager(first_aug_list)
sep_list = list_manager(first_sep_list)
oct_list = list_manager(first_oct_list)
nov_list = list_manager(first_nov_list)
dec_list = list_manager(first_dec_list)
big_list = list_manager(cheese_list)


user_list = user_search(cheese_list)

# normalized_user_list = list_length_normalizer(user_list)
# blanks_removed_list = blank_space_remover(normalized_user_list)
# split_user_list = list_split_machine(blanks_removed_list)
# integer_user_list = int_maker(split_user_list)
integer_user_list = list_manager(user_list)
max_user_value = list_sorting_machine(integer_user_list)
#for i in integer_user_list: print(i)
print("Most rain in time period selected: ", max_user_value)
total_count_of_values_in_list = list_value_counter(integer_user_list)
probability_float = probability_machine(integer_user_list, total_count_of_values_in_list)
print("Average in time period selected: ", probability_float)
my_dict = create_dict(big_list)
#print(my_dict)
average_dict = not_your_average_dictionary(my_dict, dates, months)
#print(average_dict)
jill = list(average_dict.items())
#print(jill[:10])
max_jill_value = list_sorting_machine(jill)
print("Highest Average Rainfall in time period selected: ", max_jill_value)
total_count = list_value_counter(big_list)
pineapple = fancy_key_counter(average_dict, cheese_list)
probably_dict = dict_probability_calc(average_dict, pineapple)
item_list = list(probably_dict.items())
sorted_item_list = sorted(big_list, key=lambda x: x[1], reverse=True)
#print("Sorted Items: ", sorted_item_list)
#print("Item List: ", item_list)
#print("Probably Dict: ", probably_dict)

#print(big_list)
#print(master_lister)
###Use startswith() method to sort for individual dates

#print(jan_list)
# for (k, v) in my_dict:
# 	if k[:5]

#codingbat
