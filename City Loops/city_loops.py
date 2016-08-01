import os
import random
already_visited_list = []


def user_start_choice(dict):
	"""This allows the user to enter which city they want to visit."""
	user_select = input("Which city would you like to look up?\n: ")
	#user_select = user_select.capitalize()
	return user_select

def user_go_choice(can_access_list, already_visited_list):
	user_go_away = input('Where would you like to go?\n: ')
	#user_go_away = user_go_away.capitalize()
	if user_go_away not in can_access_list:
		print("You can't go there from here. Silly user.")
		user_go_choice(can_access_list, already_visited_list)
	if already_visited_list:
		if (user_go_away in can_access_list) and (user_go_away in already_visited_list):
			print("You have already been here.")
			user_go_choice(can_access_list, already_visited_list)
		elif (user_go_away in can_access_list) and (user_go_away not in already_visited_list):
			return user_go_away
	elif not already_visited_list:
		return user_go_away

def sort_and_store_can_access(user_select, dict):
	"""This uses list comprehension to manipulate the user's chosen city."""
	can_access_list = []
	for (k, v) in dict.items():
		for i in v:
			if user_select in k:
				can_access_list.append(i)
	return can_access_list

def store_already_visited(user_select, already_visited_list):
	already_visited_list.append(user_select)

def have_not_visited_printer(dict, already_visited_list):
	have_not_visited_list = []
	for i in dict.keys():
		if i not in already_visited_list:
			have_not_visited_list.append(i)
	print("You haven't been to: ", have_not_visited_list)



#def sort_and_store_have_been_to(user_select, dict)


city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

user_select = user_start_choice(city_to_accessible_cities)
can_access_list = sort_and_store_can_access(user_select, city_to_accessible_cities)
print("From {} you can access: {}.".format(user_select, can_access_list))
user_go_away = user_go_choice(can_access_list, already_visited_list)
store_already_visited(user_select, already_visited_list)
store_already_visited(user_go_away, already_visited_list)
can_access_list = []
can_access_list = sort_and_store_can_access(user_go_away, city_to_accessible_cities)
print("From {} you can access: {}.".format(user_go_away, can_access_list))
print("Already Visited: ", already_visited_list)
have_not_visited_printer(city_to_accessible_cities, already_visited_list)






