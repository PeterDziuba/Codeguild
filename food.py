import os
import random
import json
from nutritionix import Nutritionix
print('Powered by Nutritionix API')

file_list = []
file_list_stripped = []
with open('food.txt') as my_file:
    file_list_unstripped = my_file.readlines()

    for line in file_list_unstripped:
        file_list_stripped.append(line.strip())

class Food:
    def __init__(self, name, portion, calories, protein_grams, 
                 carbs_grams, fat_grams, category_list, times_used):
        self.name = name
        self.portion = portion
        self.calories = calories
        self.protein_grams = protein_grams
        self.carbs_grams = carbs_grams
        self.fat_grams = fat_grams
        self.category_list = category_list
        self.times_used = times_used

    def __repr__(self):
        return ("{} : {} calories, {} grams of protein,"
                " {} grams of carbs, and {} grams of" 
                " fat.").format(self.name, self.calories, self.protein_grams,
                              self.carbs_grams, self.fat_grams)

class Pantry:
    def __init__(self, name, food_list):
        self.name = name
        self.food_list = food_list

def make_a_meal_plan(pantry, user_macro_goals):
    meal_plan_list = []
    list_protein_tally = 0
    list_carb_tally = 0
    list_fat_tally = 0
    list_calories_tally = 0
    meal_plan_list.append('Food --- ')
    while ((list_protein_tally < user_macro_goals[0]) or (
       list_carb_tally < user_macro_goals[1]) or (
       list_fat_tally < user_macro_goals[2])):
      new_food = random.choice(pantry.food_list)
      list_protein_tally += new_food.protein_grams
      list_carb_tally += new_food.carbs_grams
      list_fat_tally += new_food.fat_grams
      list_calories_tally += new_food.calories
      meal_plan_list.append(new_food)
    meal_plan_list.append('Nutritional Information --- ')
    meal_plan_list.append("Total Calories: {}".format(list_calories_tally))
    meal_plan_list.append('Total Protein: {}'.format(list_protein_tally))
    meal_plan_list.append('Total Carbs: {}'.format(list_carb_tally))
    meal_plan_list.append('Total Fat: {}'.format(list_fat_tally))
    meal_plan_list.append(list_calories_tally)
    return meal_plan_list

def sort_meal_plans(pantry, user_macro_goals):
    master_food_list = my_generator(1000, pantry, user_macro_goals)

    #Save the code below, it actually works.
    #i_100_list_counter = 1000
    #while i_100_list_counter > 0:
    #while my_generator(1000):
        #food_list_one = make_a_meal_plan(pantry, user_macro_goals)
        #master_food_list.append(food_list_one)
        #i_100_list_counter -= 1
    sorted_food_list = sorted(master_food_list, key=lambda x: x[-1])
    return sorted_food_list

def my_generator(n, pantry, user_macro_goals):
    while n > 0:
        food_list_one = make_a_meal_plan(pantry, user_macro_goals)
        yield food_list_one
        n -= 1

def view_pantry(pantry):
    print('Pantry Contents:')
    print('')
    for i in pantry.food_list:
        print(i.name)
        print('')

def view_pantry_details(pantry):
    print('Pantry Details:')
    print('')
    for i in pantry.food_list:
        print(i)
        print('')

def write_foods_to_list(list_of_foods):
    list_to_write = []
    for i in list_of_foods:
        my_string = ("{},{},{}," 
                     "{},{},{},"
                     "{},{}").format(i.name, i.portion,
                                  i.calories, i.protein_grams, 
                                  i.carbs_grams, 
                                  i.fat_grams, i.category_list,
                                  i.times_used)
        list_to_write.append(my_string + '\n')
    return list_to_write

def display_suggested_foods(list_of_foods):
    food_display_dict = {}
    for i in list_of_foods:
        if i in food_display_dict.keys():
            food_display_dict[i] += 1
        else: food_display_dict[i] = 1
    return food_display_dict

def print_dict_info(list_of_foods, food_display_dict):
    already_printed_list = []
    print(list_of_foods[0])
    print('')
    for i in list_of_foods[1: -7]:
        if i not in already_printed_list:
            if isinstance(i, Food):
                print("{}: {} x {}".format(i.name, food_display_dict[i], i.portion))
            else: print("{}: {}".format(i, food_display_dict[i]))
            already_printed_list.append(i)
    print('')
    print(list_of_foods[-6])
    print('')
    for i in list_of_foods[-5: -1]:
        print(i)

def user_search(string):
    '''This function takes a string from the user
    and searches the nutritionix database for that
    search term. Then, it takes the first five hits
    and returns them in a list.'''
    nix = Nutritionix(app_id="79c91dc3", api_key="72d996fc49df21a052dacdc132d65cb9")
    search = nix.search(string).json()
    search_list = []
    results_list = []
    for i in range(5):
        search_list.append(search['hits'][i]['_id'])
    for i in search_list:
        search_item = nix.item(id=i).json()
        new_food = Food(search_item['item_name'], 
                        search_item['nf_serving_size_qty'],
                        search_item['nf_calories'],
                        search_item['nf_protein'],
                        search_item['nf_total_carbohydrate'],
                        search_item['nf_total_fat'],
                        ['User Search'],
                        0)
        results_list.append(new_food)
    return results_list

def save_results(list):
    user_save = input('Save any of these items?'
                      ' Enter a number 1-5 or press n\n: ')
    if user_save == 'n': return None
    else: 
        user_number = int(user_save)
        user_number -= 1
        return list[user_number]

def add_food_to_pantry(pantry, food_item):
    pantry.food_list.append(food_item)

def make_a_list_of_categories(list):
    still_adding = 1
    while still_adding:
        user_item = input('What category would you like to add?\n: ')
        list.append(user_item)
        user_continue = input('Add more categories?\n: ')
        if user_continue == 'n': still_adding -= 1

def user_add_food_to_pantry(pantry):
    user_food_category_list = []
    user_food_name = input('What kind of food are you adding?\n: ')
    user_food_portion = input('What is the serving size for that?\n: ')
    user_food_calories = int(input('How many calories does that have?\n: '))
    user_food_protein = int(
        input('How much protein does that have, in grams?\n: '))
    user_food_carbs = int(
        input('How many carbs does that have, in grams?\n: '))
    user_food_fat = int(
        input('How much fat does that have, in grams?\n: '))
    user_food_category_choice = input('Add categories?')
    if user_food_category_choice != 'n':
        make_a_list_of_categories(user_food_category_list)
    new_food = Food(user_food_name, user_food_portion, user_food_calories,
                    user_food_protein, user_food_carbs, user_food_fat,
                    user_food_category_list, 0)
    pantry.food_list.append(new_food)

def get_user_macro_goals():
    print('Tell us your macro goals so we can sort your food!')
    user_protein_goal = int(
        input('How many grams of protein do you need?\n: '))
    user_carb_goal = int(input('How many grams of carbs do you need?\n: '))
    user_fat_goal = int(input('How many grams of fat do you need?\n: '))
    macro_list = [user_protein_goal, user_carb_goal, user_fat_goal]
    return macro_list



banana = Food('Banana', 'One-Medium', 105, 1.3, 27, 0.4, 
              ['Breakfast', 'Snack', 'Carbs', 'Fruit'], 0)
turkey = Food('Turkey', '4oz', 118, 19.4, 4.8, 1.9, 
              ['Lunch', 'Ingredients', 'Protein'], 0)
oatmeal = Food('Oatmeal: Quaker Oats Apple Cinnamon', '2 Packets',
               320, 8, 66, 4, ['Breakfast', 'Snack', 'Carbs'], 0)
cereal = Food('Honey Bunches of Oats with Fat Free Milk', '2.25 Cups',
              496, 19, 93.4, 5.4, ['Breakfast', 'Snack', "Carbs"], 0)
cookie = Food('Cookie: Pepperidge Farm Double Chocolate Nantucket',
              'One Cookie', 140, 1, 19, 7, 
              ['Snack', 'Dessert', 'Cheat', 'Treat'], 0)
lettuce = Food('Mixed Greens', '3 Cups', 20, 2, 2, 0, 
               ['Healthy', 'Vegetable'], 0)
salmon = Food('Smoked Salmon', '4oz', 132, 20, 0, 4.8, 
              ['Protein', 'Fish', 'Snack'], 0)

initial_food_list = [banana, turkey, oatmeal, cereal, cookie, lettuce,
                     salmon]
my_pantry = Pantry("Peter's Pantry", initial_food_list)

# view_pantry(my_pantry)
# user_add_food_to_pantry(my_pantry)
# view_pantry_details(my_pantry)

def user_menu(my_pantry, user_macro_goals):
    user_prompt_list = ['Search Online', 'Add to Pantry', 
                        'View Pantry', 'Enter Macro Goals', 
                        'Get a Meal Plan']
    print('Welcome to "What Should I Eat"!')
    print('\nThings We Can Do:')
    for i in user_prompt_list:
        print(i)

    print('\nTo begin, enter the first word of the option you want.')
    user_menu_nav = input(': ')
    lower_user_menu_nav = user_menu_nav.lower()
    if lower_user_menu_nav == 'search':
        user_search_param = input('Search the Nutritionix Database: ')
        user_search_results = user_search(user_search_param)
        for i in user_search_results:
            print(i)
        user_save = save_results(user_search_results)
        if user_save:
            add_food_to_pantry(my_pantry, user_save)
    elif lower_user_menu_nav == 'add':
        user_add_food_to_pantry(my_pantry)
    elif lower_user_menu_nav == 'view':
        print('Overview:')
        view_pantry(my_pantry)
        print('\n---\n')
        print('Details:')
        view_pantry_details(my_pantry)
    elif lower_user_menu_nav == 'enter':
        user_macro_goals = get_user_macro_goals()
    elif lower_user_menu_nav == 'get':
        my_meal_plan = sort_meal_plans(my_pantry, user_macro_goals)
        my_meal_dict = display_suggested_foods(my_meal_plan[0])
        print_dict_info(my_meal_plan[0], my_meal_dict)
    return user_macro_goals


go_on = 1
count = 1
while go_on:
    if count > 0:
        user_macro_goals = get_user_macro_goals()
        count -= 1
    user_macro_goals = user_menu(my_pantry, user_macro_goals)
    user_loop = input('Continue?\n: ')
    if user_loop == 'n': go_on -= 1
    os.system('clear')


# user_protein_goal = 140
# user_carb_goal = 280
# user_fat_goal = 38
# user_macro_goals = [140, 280, 38]
# master_food_list = []

# my_meal_plan = sort_meal_plans(my_pantry, user_macro_goals)
# my_meal_dict = display_suggested_foods(my_meal_plan[0])
# print_dict_info(my_meal_plan[0], my_meal_dict)


#########----------------

#food_list_to_write = write_foods_to_list(my_pantry.food_list)
#print(food_list_to_write)
#my_file = open('food.txt', 'w')
#for i in food_list_to_write:
    #my_file.write(i)

#my_file.close()
#print(file_list_stripped)



# quick_list = []

# while ((list_protein_tally < user_protein_goal) or (
#        list_carb_tally < user_carb_goal) or (
#        list_fat_tally < user_fat_goal)):
#       new_food = random.choice(my_pantry.food_list)
#       list_protein_tally += new_food.protein_grams
#       list_carb_tally += new_food.carbs_grams
#       list_fat_tally += new_food.fat_grams
#       list_calories_tally += new_food.calories
#       quick_list.append(new_food.name)

# print(quick_list)
# print('Protein Total: ', list_protein_tally)
# print('Carbs Total: ', list_carb_tally)
# print('Fat Total: ', list_fat_tally)
# print('Calories Total: ', list_calories_tally)




