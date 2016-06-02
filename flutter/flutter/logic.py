from . import models

def get_all_flutts():
    category_list = models.Flutt.objects.all()
    return category_list

def save_flutt(user_name, user_text):
    new_flutt = models.Flutt(user=user_name, text=user_text)
    new_flutt.save()

def get_flutt_by_id(our_id):
    return models.Flutt.objects.get(id=our_id)

def delete_flutt(flutt):
    flutt.delete()

def get_all_flutts_for_user(our_user):
    return models.Flutt.objects.filter(user=our_user)

def get_flutt_by_contents(query):
    return models.Flutt.objects.filter(text__contains=query)