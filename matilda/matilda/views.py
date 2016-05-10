from django.shortcuts import render
from django.http import HttpResponse
from . import logic

def count(request):
    word_to_count = request.GET['w']
    my_string = logic.function_bundle(word_to_count, logic.no_punct_hamlet)
    if my_string:
        return HttpResponse(my_string)
    else:
        return HttpResponse(status=200)

def matilda(request):
    return render(request, 'matilda/matilda.html')

