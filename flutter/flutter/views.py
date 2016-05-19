from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from . import models
from . import logic

def index(request):
    flutts = logic.get_all_flutts()
    flutt_length = len(flutts)
    less_flutt_length = (flutt_length - 10)
    if less_flutt_length > 0:
        ten_flutts = flutts[less_flutt_length : flutt_length]
    else: ten_flutts = flutts[:10]
    context = {
        'ten_flutts':ten_flutts
    }
    return render(request, 'flutter/index.html', context)

def render_post(request):
    return render(request, 'flutter/post.html')

def post_ack(request):
    user = request.POST['our-user']
    text = request.POST['our-text']
    logic.save_flutt(user, text)
    return render(request, 'flutter/ack.html')

def render_user(request):
    flutt_user = request.POST['flutt-user']
    flutts = logic.get_all_flutts_for_user(flutt_user)
    flutt_length = len(flutts)
    if flutt_length > 0:
        less_flutt_length = (flutt_length - 10)
        if less_flutt_length > 0:
            ten_flutts = flutts[less_flutt_length : flutt_length]
        else: ten_flutts = flutts[:10]

        context = {
            'flutt_user':flutt_user,
            'flutts': ten_flutts
        }
        return render(request, 'flutter/user.html', context)
    else: return render(request, 'flutter/error-user.html')

def search_flutts(request):
    query = request.POST['query']
    flutts = logic.get_flutt_by_contents(query)
    flutt_length = len(flutts)
    if flutt_length > 0:
        less_flutt_length = (flutt_length - 10)
        if less_flutt_length > 0:
            ten_flutts = flutts[less_flutt_length : flutt_length]
        else: ten_flutts = flutts[:10]

        context = {
            'flutts':ten_flutts,
        }
        return render(request, 'flutter/search-results.html', context)
    else: return render(request, 'flutter/error-flutt.html')

def render_search(request):
    return render(request, 'flutter/search.html')

def user_search(request):
    return render(request, 'flutter/user-search.html')





