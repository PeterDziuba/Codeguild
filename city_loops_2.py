#This is my second attempt at the city looping problem.
#I am going to try to implement the advanced functions
#from the beginning.
import os

def get_user_choice():
	"""This function lets the user enter a city."""
	user_choice = input("Where would you like to start?\n: ")
	return user_choice

def get_user_hops():
	"""This function lets the user enter how many hops to take."""
	user_hops = int(input("How many hops would you like to take today?\n: "))
	return user_hops

def process_choices_and_hops(user_choice, user_hops, city_dict, loop_bool):
	"""This function tells the user where they can go."""

	if user_hops < 1: print("You can't go anywhere!")

	elif user_hops == 1:
		print("You can go to the following places:")
		print(city_dict[user_choice])

	elif user_hops == 2:
		print("You can go to the following places:")
		print(city_dict[user_choice])
		print("From there, you can go to these places:")
		for i in city_dict[user_choice]:
			print(i, ":", city_dict[i])
		print("")
		my_travel_list = count_route_length(user_choice, user_hops, city_to_accessible_cities_with_travel_time)
		my_sorted_travel_list = cut_out_duplicate_cities(my_travel_list)
		print("Shortest Routes to Destinations:", my_sorted_travel_list)

	elif user_hops == 3:
		print("You can go to the following places:")
		print(city_dict[user_choice])
		print("")
		print("From there, you can go to these places:")
		for i in city_dict[user_choice]:
			print(i, ":", city_dict[i])
		print("")
		print("From there, you can go to these places:")
		for j in city_dict[i]:
			print(j, ":", city_dict[j])
		print("")
		my_travel_list = count_route_length(user_choice, user_hops, city_to_accessible_cities_with_travel_time)
		my_sorted_travel_list = cut_out_duplicate_cities(my_travel_list)
		print("Shortest Routes to Destinations:", my_sorted_travel_list)

	elif user_hops == 4:
		print("You can go to the following places:")
		print(city_dict[user_choice])
		print("")
		print("From there, you can go to these places:")
		for i in city_dict[user_choice]:
			print(i, ":", city_dict[i])
		print("")
		print("From there, you can go to these places:")
		for j in city_dict[i]:
			print(j, ":", city_dict[j])
		print("")
		print("From there, you can go to these places:")
		for k in city_dict[j]:
			print(k, ":", city_dict[k])
		print("")
		my_travel_list = count_route_length(user_choice, user_hops, city_to_accessible_cities_with_travel_time)
		my_sorted_travel_list = cut_out_duplicate_cities(my_travel_list)
		print("Shortest Routes to Destinations:", my_sorted_travel_list)

	elif user_hops == 5:
		print("You can go to the following places:")
		print(city_dict[user_choice])
		print("")
		print("From there, you can go to these places:")
		for i in city_dict[user_choice]:
			print(i, ":", city_dict[i])
		print("")
		print("From there, you can go to these places:")
		for j in city_dict[i]:
			print(j, ":", city_dict[j])
		print("")
		print("From there, you can go to these places:")
		for k in city_dict[j]:
			print(k, ":", city_dict[k])
		print("")
		print("From there, you can go to these places:")
		for l in city_dict[k]:
			print(l, ":", city_dict[l])
		print("")
		my_travel_list = count_route_length(user_choice, user_hops, city_to_accessible_cities_with_travel_time)
		my_sorted_travel_list = cut_out_duplicate_cities(my_travel_list)
		print("Shortest Routes to Destinations:", my_sorted_travel_list)

	elif user_hops > 5: print('Sorry, this program only goes to 5 hops.')

	user_continue_choice = input("Continue?\n: ")
	if user_continue_choice == 'n': loop_bool = False
	os.system('clear')
	return loop_bool

def count_route_length(user_choice, user_hops, city_dict):
	travel_length_list = []

	for city in city_dict[user_choice]:
		my_line = [city, city_dict[user_choice][city]]
		travel_length_list.append(my_line)

		if user_hops >= 2:

			for sub_city in city_dict[city]:
				my_value = city_dict[user_choice][city] + city_dict[city][sub_city]
				my_next_line = [sub_city, my_value]
				travel_length_list.append(my_next_line)

				if user_hops >= 3:

					for sub_sub_city in city_dict[sub_city]:
						my_next_value = city_dict[user_choice][city] + city_dict[city][sub_city] + city_dict[sub_city][sub_sub_city]
						my_third_line = [sub_sub_city, my_next_value]
						travel_length_list.append(my_third_line)

	return travel_length_list

def cut_out_duplicate_cities(travel_length_list):
	portland_list = []
	new_york_list = []
	boston_list = []
	albany_list = []
	philly_list = []
	minimum_list = []

	for i in travel_length_list:
		if 'Portland' in i:
			portland_list.append(i)

	for i in travel_length_list:
		if "Boston" in i:
			boston_list.append(i)

	for i in travel_length_list:
		if "New York" in i:
			new_york_list.append(i)

	for i in travel_length_list:
		if "Philadelphia" in i:
			philly_list.append(i)

	for i in travel_length_list:
		if "Albany" in i:
			albany_list.append(i)

	if portland_list: portland_min = min(portland_list, key=lambda x: x[1])
	if new_york_list: new_york_min = min(new_york_list, key=lambda x: x[1])
	if boston_list: boston_min = min(boston_list, key=lambda x: x[1])
	if albany_list: albany_min = min(albany_list, key=lambda x: x[1])
	if philly_list: philly_min = min(philly_list, key=lambda x: x[1])

	if portland_list: minimum_list.append(portland_min)
	if new_york_list: minimum_list.append(new_york_min)
	if boston_list: minimum_list.append(boston_min)
	if albany_list: minimum_list.append(albany_min)
	if philly_list: minimum_list.append(philly_min)

	sorted_minimum_list = sorted(minimum_list, key=lambda x: x[1])
	return sorted_minimum_list
		
city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

loop_bool = True
while loop_bool:
	user_choice = get_user_choice()
	user_hops = get_user_hops()
	loop_bool = process_choices_and_hops(user_choice, user_hops, city_to_accessible_cities_with_travel_time, loop_bool)

