import urllib.request
import os
import random
jan_list = []
feb_list = []
mar_list = []
april_list = []
may_list = []
jun_list = []
july_list = []
aug_list = []
sep_list = []
oct_list = []
nov_list = []
dec_list = []
l_2002_list = []
l_2003_list = []
l_2004_list = []
l_2005_list = []
l_2006_list = []
l_2007_list = []
l_2008_list = []
l_2009_list = []
l_2010_list = []
l_2011_list = []
l_2012_list = []
l_2013_list = []
l_2014_list = []
l_2015_list = []
l_2016_list = []

def list_split_machine(list):
	split_list = []
	for i in list:
		split_list.append(i.split(','))
	for i in split_list:
		if i[1] == '-': i[1] = 0
		else: i[1] = int(i[1])
	return split_list

def integer_converter(list):
	for i in list:
		i[1] = int(i[1])
	return list



def user_search(list):
	my_list = []
	user_year = input("What year would you like to search?: ")
	user_month = input("What month would you like to search?: ")
	for i in list:
		if (user_year in i) and (user_month in i.lower()):
			my_list.append(i)
	return my_list

def list_sorting_machine(list):
	sort_list = sorted(list, key=lambda x: x[1], reverse=True)
	my_max_value = sort_list[0]
	return my_max_value


def read_site(site):
	"""This reads open the file."""
	line_list = []
	with urllib.request.urlopen(site) as my_site:
		for line in my_site:
			line_list.append(line.strip().decode('utf-8'))
	return line_list

def rain_fall_data_sort(some_list):
	"""This function will turn our list into a dict with keys.
	I want to use the date as the key and the rainfall data as
	the value."""
	some_dict = {}
	for i in some_list:
		some_dict[i[3:14]] = i[18:]
	return some_dict


my_site = read_site('http://or.water.usgs.gov/non-usgs/bes/sunnyside.rain')
data_i_actually_care_about = []
number_list = []

for line in my_site:

	data_i_actually_care_about.append(line[:17])

for i in data_i_actually_care_about:
	while "  " in i:
		i = i.replace("  ", " ")
	i = i.replace(" ", ",")
	number_list.append(i)


for i in number_list:
	if '2002' in i: l_2002_list.append(i)
	elif '2003' in i: l_2003_list.append(i)
	elif '2004' in i: l_2004_list.append(i)
	elif '2005' in i: l_2005_list.append(i)
	elif '2006' in i: l_2006_list.append(i)
	elif '2007' in i: l_2007_list.append(i)
	elif '2008' in i: l_2008_list.append(i)
	elif '2009' in i: l_2009_list.append(i)
	elif '2010' in i: l_2010_list.append(i)
	elif '2011' in i: l_2011_list.append(i)
	elif '2012' in i: l_2012_list.append(i)
	elif '2013' in i: l_2013_list.append(i)
	elif '2014' in i: l_2014_list.append(i)
	elif '2015' in i: l_2015_list.append(i)
	elif '2016' in i: l_2016_list.append(i)

for i in number_list:
	if 'jan' in i.lower(): jan_list.append(i)
	elif 'feb' in i.lower(): feb_list.append(i)
	elif 'mar' in i.lower(): mar_list.append(i)
	elif 'apr' in i.lower(): april_list.append(i)
	elif 'may' in i.lower(): may_list.append(i)
	elif 'jun' in i.lower(): jun_list.append(i)
	elif 'jul' in i.lower(): july_list.append(i)
	elif 'aug' in i.lower(): aug_list.append(i)
	elif 'sep' in i.lower(): sep_list.append(i)
	elif 'oct' in i.lower(): oct_list.append(i)
	elif 'nov' in i.lower(): nov_list.append(i)
	elif 'dec' in i.lower(): dec_list.append(i)



new_jan = list_split_machine(jan_list)
new_feb = list_split_machine(feb_list)
new_march = list_split_machine(mar_list)
new_april = list_split_machine(april_list)
new_may = list_split_machine(may_list)
new_jun = list_split_machine(jun_list)
new_july = list_split_machine(july_list)
new_aug = list_split_machine(aug_list)
new_sep = list_split_machine(sep_list)
new_oct = list_split_machine(oct_list)
new_nov = list_split_machine(nov_list)
new_dec = list_split_machine(dec_list)
new_2002 = list_split_machine(l_2002_list)
new_2003 = list_split_machine(l_2003_list)
new_2004 = list_split_machine(l_2004_list)
new_2005 = list_split_machine(l_2005_list)
new_2006 = list_split_machine(l_2006_list)
new_2007 = list_split_machine(l_2007_list)
new_2008 = list_split_machine(l_2008_list)
new_2009 = list_split_machine(l_2009_list)
new_2010 = list_split_machine(l_2010_list)
new_2011 = list_split_machine(l_2011_list)
new_2012 = list_split_machine(l_2012_list)
new_2013 = list_split_machine(l_2013_list)
new_2014 = list_split_machine(l_2014_list)
new_2015 = list_split_machine(l_2015_list) 
new_2016 = list_split_machine(l_2016_list)

# new_new_jan = integer_converter(new_jan)
# new_new_aug = integer_converter(new_aug)

# user_search_list = user_search(number_list)
# split_list = []
# for i in user_search_list:
# 	split_list.append(i.split(','))


# user_max_value = list_sorting_machine(split_list)
# print("The highest rain for that year and month was: ", user_max_value)

jan_max_value = list_sorting_machine(new_jan)
feb_max_value = list_sorting_machine(new_feb)
mar_max_value = list_sorting_machine(new_march)
apr_max_value = list_sorting_machine(new_april)
may_max_value = list_sorting_machine(new_may)
june_max_value = list_sorting_machine(new_jun)
july_max_value = list_sorting_machine(new_july)
aug_max_value = list_sorting_machine(new_aug)
sep_max_value = list_sorting_machine(new_sep)
oct_max_value = list_sorting_machine(new_oct)
nov_max_value = list_sorting_machine(new_nov)
dec_max_value = list_sorting_machine(new_dec)

v_2002_max_value = list_sorting_machine(new_2002)
v_2003_max_value = list_sorting_machine(new_2003)
v_2004_max_value = list_sorting_machine(new_2004)
v_2005_max_value = list_sorting_machine(new_2005)
v_2006_max_value = list_sorting_machine(new_2006)
v_2007_max_value = list_sorting_machine(new_2007)
v_2008_max_value = list_sorting_machine(new_2008)
v_2009_max_value = list_sorting_machine(new_2009)
v_2010_max_value = list_sorting_machine(new_2010)
v_2011_max_value = list_sorting_machine(new_2011)
v_2012_max_value = list_sorting_machine(new_2012)
v_2013_max_value = list_sorting_machine(new_2013)
v_2014_max_value = list_sorting_machine(new_2014)
v_2015_max_value = list_sorting_machine(new_2015)
v_2016_max_value = list_sorting_machine(new_2016)


print("The highest rainfall in January was: ", jan_max_value)
print("The highest rainfall in February was: ", feb_max_value)
print("The highest rainfall in March was: ", mar_max_value)
print("The highest rainfall in April was: ", apr_max_value)
print("The highest rainfall in May was: ", may_max_value)
print("The highest rainfall in June was: ", june_max_value)
print("The highest rainfall in July was: ", july_max_value)
print("The highest rainfall in August was: ", aug_max_value)
print("The highest rainfall in September was: ", sep_max_value)
print("The highest rainfall in October was: ", oct_max_value)
print("The highest rainfall in November was: ", nov_max_value)
print("The highest rainfall in December was: ", dec_max_value)
print("The highest rainfall in 2002 was: ", v_2002_max_value)
print("The highest rainfall in 2003 was: ", v_2003_max_value)
print("The highest rainfall in 2004 was: ", v_2004_max_value)
print("The highest rainfall in 2005 was: ", v_2005_max_value)
print("The highest rainfall in 2006 was: ", v_2006_max_value)
print("The highest rainfall in 2007 was: ", v_2007_max_value)
print("The highest rainfall in 2008 was: ", v_2008_max_value)
print("The highest rainfall in 2009 was: ", v_2009_max_value)
print("The highest rainfall in 2010 was: ", v_2010_max_value)
print("The highest rainfall in 2011 was: ", v_2011_max_value)
print("The highest rainfall in 2012 was: ", v_2012_max_value)
print("The highest rainfall in 2013 was: ", v_2013_max_value)
print("The highest rainfall in 2014 was: ", v_2014_max_value)
print("The highest rainfall in 2015 was: ", v_2015_max_value)
print("The highest rainfall in 2016 so far was: ", v_2016_max_value)
# new_new_jan_max = list_sorting_machine(new_new_jan)
# new_new_aug_max = list_sorting_machine(new_new_aug)
# print(new_new_jan_max)
# print(new_new_aug_max)
