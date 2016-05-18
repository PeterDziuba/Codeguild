from . import models

def get_all_categories():
    category_list = models.Category.objects.all()
    return category_list

def save_category(string):
    new_string = models.Category(name=string)
    new_string.save()

def get_category_by_id(our_id):
    return models.Category.objects.get(id=our_id)

def get_subcategory_by_id(our_id):
    return models.SubCategory.objects.get(id=our_id)

def delete_subcategory(sub):
    sub.delete()


def create_sub(our_name, our_category):
    new_sub = models.SubCategory(
        name=our_name,
        category=our_category)
    new_sub.save()

def get_all_subs_for_cat(our_category):
    return models.SubCategory.objects.filter(category=our_category)

def get_all_subs():
    return models.SubCategory.objects.all

def package_categories():
    category_to_sub = {}
    categories = get_all_categories()

    for i in categories:
        subs = []
        for sub_cat in models.SubCategory.objects.filter(category=i):
            subs.append(sub_cat) #sub_cat.name
        category_to_sub[i] = subs
        # print(category_to_sub)
    # print(category_to_sub)
    return category_to_sub

        

