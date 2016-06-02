my_joke_bank = []

def save_to_jokebank(punchline, setup):
    my_joke = {'setup':setup, 'punchline':punchline}
    my_joke_bank.append(my_joke)

def get_all_jokes():
    return my_joke_bank