
def get_a_string():
    my_str = input('Enter a string please.\n: ')
    return my_str


def remove_snakes(string):
    string = string.replace('_', ' ')
    return string


def remove_kebab(string):
    string = string.replace('-', ' ')
    return string


def capitalize(string):
    string = string.title()
    return string


def remove_spaces(string):
    string = string.replace(' ', '')
    return string


def convert_camels(string):
    list_string = list(string)
    for i in range(len(list_string)):
       if list_string[i] == list_string[i].upper():
           list_string[i] = list_string[i].lower()
           if i > 0:
            my_str = "_{}".format(list_string[i])
            list_string[i] = my_str
    string_string = "".join(list_string)
    return string_string


def detect_case(string):
    if string == string.upper() and '_'  in string:
        return 'Constant Case'
    elif string == string.lower() and '_' in string:
        return 'Snake Case'
    elif string == string.lower() and '-' in string:
        return 'Kebab Case'
    elif ' ' not in string:
        return 'Camel Case'


def master_converter(string, case):
    if case == 'Constant Case':
        my_string = string.title()
        snakeless_string = remove_snakes(my_string)
        return snakeless_string

    elif case == 'Snake Case':
        my_string = string.title()
        my_snakeless_string = remove_snakes(my_string)
        my_capital_string = capitalize(my_snakeless_string)
        return my_capital_string

    elif case == 'Kebab Case':
        kebabless_string = remove_kebab(string)
        my_string = kebabless_string.title()
        return my_string

    elif case == 'Camel Case':
        converted_string = convert_camels(string)
        snakeless_string = remove_snakes(converted_string)
        title_snakeless_string = snakeless_string.title()
        return title_snakeless_string


if __name__ == '__main__':
    my_string = get_a_string()
    my_case = detect_case(my_string)
    print("Your string is in", my_case)
    super_case = master_converter(my_string, my_case)
    print("Your string in Title Case:", super_case)