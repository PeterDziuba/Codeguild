from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from . import models
from . import logic


def index(request):
    cat_to_sub_list = logic.package_categories()
    context = {
        'cat_to_sub_list':cat_to_sub_list
    }
    return render(request, 'todo/index.html', context)

def add(request):
    return render(request, 'todo/add.html')

def submit(request):
    string = request.POST['our-input']
    logic.save_category(string)
    return render(request, 'todo/ack.html')

def render_add_sub(request, category_id):
    category = logic.get_category_by_id(category_id)

    template_args = {
        'category': category,
    }
    return render(request, 'todo/add_sub.html', template_args)

def render_category(request, category_id):
    category = logic.get_category_by_id(category_id)
    subs = logic.get_all_subs_for_cat(category)

    template_args = {
        'category': category,
        'subs': subs,
    }
    return render(request, 'todo/list.html', template_args)

def render_add_sub_ack(request, category_id):
    subcategory = request.POST['our-name']
    category = logic.get_category_by_id(category_id)

    logic.create_sub(subcategory, category)

    
    return render(request, 'todo/ack.html')

def delete_sub(request, subcategory_id):
    subcategory = logic.get_subcategory_by_id(subcategory_id)
    print(subcategory)
    logic.delete_subcategory(subcategory)
    cat_to_sub_list = logic.package_categories()
    context = {
        'cat_to_sub_list':cat_to_sub_list
    }
    return render(request, 'todo/index.html', context)







