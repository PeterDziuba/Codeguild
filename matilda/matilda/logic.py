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

def return_most_common_string(list, dict):
    i = list[0]
    my_string = i + " : " + str(dict[i])
    return my_string

def sort_for_one_user_word(user_word, word_list):
    user_word_list = []
    for word in word_list:
        if user_word == word:
            user_word_list.append(word)
    return user_word_list

def function_bundle(user_word, no_punct_hamlet):
    user_word_list = sort_for_one_user_word(user_word, no_punct_hamlet)
    user_word_dict = make_a_dict(user_word_list)
    most_common_user_words = sorted(user_word_dict, key=user_word_dict.get, reverse=True)
    my_string = return_most_common_string(most_common_user_words, user_word_dict)
    return my_string




hamlet_stripped = read_file('/Users/htdzi/Documents/codeguild/hamlet.txt')
words_of_hamlet = make_lines_into_words(hamlet_stripped)
lower_case_hamlet = down_case(words_of_hamlet)
no_punct_hamlet = strip_punctuation(lower_case_hamlet)
my_string = function_bundle('hamlet', no_punct_hamlet)
print(my_string)