#I am going to test deriving class instances from a dict.

class TestClass:
	def __init__(self, class_instance_name, class_number):
		self.class_instance_name = class_instance_name
		self.class_number = class_number
	def __str__(self):
		my_str = ('Hey it worked! {} {}'.format(self.class_instance_name, self.class_number))
		return my_str
	def print_test_class(self):
		print(self.class_instance_name)
		print(self.class_number)

atm_database = {'Peter':['Peter', 5000], 'Kyle':['Kyle', 2000], "Jim":['Jim', 50]}

def make_test_class_instances_from_dict(dict):
	for i in dict.keys():
		i = TestClass(dict[i][0], dict[i][1])
		print(i)

def store_class_instances_to_dict(dict, my_class_instance):
	my_name = my_class_instance.class_instance_name
	my_self = my_class_instance.class_instance_name
	my_number = my_class_instance.class_number 
	my_list = [my_self, my_number]
	dict[my_self] = my_list
	return dict

def dict_query(dict, user_name):
	if user_name in dict.keys():
		my_test_class = TestClass(user_name, dict[user_name][1])
		my_test_class.print_test_class()

		
print(atm_database)
make_test_class_instances_from_dict(atm_database)

bill = TestClass('Bill', 75)
atm_database = store_class_instances_to_dict(atm_database, bill)
print(atm_database)
make_test_class_instances_from_dict(atm_database)

user_added_class_instance = input("Who would you like to add?")
user_added_class_instance_number = int(input('What is your number?'))
user_added_class_instance = TestClass(user_added_class_instance, user_added_class_instance_number)
atm_database = store_class_instances_to_dict(atm_database, user_added_class_instance)
print(atm_database)
make_test_class_instances_from_dict(atm_database)
user_request = input("Who would you like to search for?")
dict_query(atm_database, user_request)

