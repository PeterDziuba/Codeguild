import urllib.request
import os

def read_site(site):
	"""This reads open the file."""
	line_list = []
	with urllib.request.urlopen(site) as my_site:
		for line in my_site:
			line_list.append(line.strip().decode('utf-8'))
	return line_list[11:-1]

def list_length_normalizer(list):
	normal_length_list = []
	for line in list:
		normal_length_list.append(line[:17])
	return normal_length_list

def blank_space_remover(list):
	blank_space_list = []
	for i in list:
		while "  " in i:
			i = i.replace("  ", " ")
		i = i.replace(" ", ",")
		blank_space_list.append(i)
	return blank_space_list

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

def dictionary_from_tuple_list_machine(list):
	dictionary_from_tuple = {}
	for k, v in list:
		if k in dictionary_from_tuple:
			dictionary_from_tuple[k] += v
		elif k not in dictionary_from_tuple:
			dictionary_from_tuple[k] = v
	return dictionary_from_tuple

def print_highest_value_from_dictionary(dict):
	highest_dict_value = max(dict, key=dict.get)
	return highest_dict_value

def remove_dates_from_list(list):
	dates_removed_list = []
	for line in list:
		dates_removed_list.append(line[7:])
	return dates_removed_list

def remove_year_from_list(list):
	year_removed_list = []
	for line in list:
		my_new_line = line[:6] + line[11:]
		year_removed_list.append(my_new_line)
	return year_removed_list

def element_occurrence_counter(list, dict):
	"""This function returns a list of lists.
	The first element is the date, which are dict keys.
	The second element is the count of keys."""
	list_of_averages = []
	for i in dict.keys():
		i_count = 0
		for j in list:
			if i in j:
				i_count += 1
			count_list = [i, i_count]
		list_of_averages.append(count_list)
	return list_of_averages

def average_calculator(list, dict):
	for i in list:
		for k, v in dict.items():
			if i[0] == k:
				new_v = (v/(i[1]))
				dict[k] = new_v
	return dict

def automate_list_functions(list):
	blank_spaces_removed_list = blank_space_remover(list)
	split_list = list_split_machine(blank_spaces_removed_list)
	integer_converted_list = int_maker(split_list)
	tuple_dictionary = dictionary_from_tuple_list_machine(integer_converted_list)
	return tuple_dictionary

os.system('clear')

#This section reads the website and prepares our initial list.
unmodified_website_data_list = read_site('https://raw.githubusercontent.com/selassid/codeguild/master/sunnyside.rain')
sliced_website_data_list = list_length_normalizer(unmodified_website_data_list)

#This section finds the day with the most rainfall overall.
processed_data_dict = automate_list_functions(sliced_website_data_list)
highest_rain_day = print_highest_value_from_dictionary(processed_data_dict)
print("The day with the most rain overall was:", highest_rain_day, "with", processed_data_dict[highest_rain_day])


#This section finds the year with the most rainfall overall.
day_and_month_removed_list = remove_dates_from_list(sliced_website_data_list)
processed_day_and_month_removed_dict = automate_list_functions(day_and_month_removed_list)
highest_rain_year = print_highest_value_from_dictionary(processed_day_and_month_removed_dict)
print("The year with the most rain overall was:", highest_rain_year, "with", processed_day_and_month_removed_dict[highest_rain_year])

#This section finds the date with the highest average rainfall.
year_removed_list = remove_year_from_list(sliced_website_data_list)
year_removed_processed_dict = automate_list_functions(year_removed_list)
my_average_list = element_occurrence_counter(year_removed_list, year_removed_processed_dict)
my_average_dict = average_calculator(my_average_list, year_removed_processed_dict)
my_highest_day = max(my_average_dict, key=my_average_dict.get)
print("The highest average rainfall occurs on:")
print(my_highest_day, my_average_dict[my_highest_day])

#This section allows the user to predict rainfall on a date
#by returning the average rainfall for that date.
user_day = input("What day would you like to predict?\n: ")
if user_day in my_average_dict.keys():
	print("The average rainfall for that day:")
	print(user_day, my_average_dict[user_day])
else: print("That day isn't in there. Something went wrong.")

print("All rainfall amounts are in hundredths of inches.")





