from django.shortcuts import render
from django.http import HttpResponse
from . import logic

def jokebank(request):
    logic.save_to_jokebank(request)
    return HttpResponse(status=200)

def jokes(request):
    return render(request, 'jokes/jokes.html')

def joke_list(request):
    jokes = logic.get_all_jokes
    context = {
        'jokes':jokes
    }
    return render(request, 'jokes/joke-list.html', context)