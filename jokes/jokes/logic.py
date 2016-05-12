my_joke_bank = {}
my_joke_bank['jokes'] = []

def save_to_jokebank(request):
    punchline = request.POST['punchline']
    setup = request.POST['setup']
    my_joke = {'setup':setup, 'punchline':punchline}
    my_joke_bank['jokes'].append(my_joke)

def get_all_jokes():
    return my_joke_bank['jokes']