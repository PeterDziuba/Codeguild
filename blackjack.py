import random
import os


class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.face, self.suit)

    def __repr__(self):
        return "{} of {}".format(self.face, self.suit)

    def __eq__(self, other):
        return (self.suit == other.suit) and (self.face == other.face)


class Hand:
    def __init__(self, card_list):
        self.card_list = card_list

    def __str__(self):
        return self.card_list

    def __repr__(self):
        return self.card_list

    def score_hand(self):
        score_counter = 0
        ace_counter = 0

        for i in self.card_list:
            score_counter += i.value

        for i in self.card_list:
            if i.value == 11:
                ace_counter += 1

        while (score_counter > 21) and (ace_counter > 0):
            if ace_counter:
                score_counter -= 10
                ace_counter -= 1

        return score_counter


class Deck:
    def __init__(self, name, card_list):
        self.name = name
        self.card_list = card_list


def make_a_deck(face_list, suit_list):
    card_list = []
    for i in suit_list:

        for j in face_list:

            my_face = j

            if my_face in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:

                my_value = int(my_face)

            elif my_face in ["Jack", "Queen", "King"]:

                my_value = 10

            elif my_face == 'Ace':
                my_value = 11

            my_suit = i
            new_card = Card(my_suit, my_face, my_value)
            card_list.append(new_card)

    new_deck = Deck('Bicycle', card_list)
    return new_deck


def deal_a_card(my_hand, your_hand, deck):
    new_card = random.choice(deck.card_list)
    deal_count = 0

    while deal_count < 1:

        new_card = random.choice(deck.card_list)

        if ((new_card not in my_hand.card_list) and
        (new_card not in your_hand.card_list)):

            my_hand.card_list.append(new_card)
            deck.card_list.remove(new_card)
            deal_count += 1

    return my_hand


def print_a_card_list(hand):
    for i in hand.card_list:
        print(i)


def double_deal_hands(my_hand, your_hand, deck):
    deal_a_card(my_hand, your_hand, deck)
    deal_a_card(my_hand, your_hand, deck)
    deal_a_card(your_hand, my_hand, deck)
    deal_a_card(your_hand, my_hand, deck)


def dealer_play_blackjack(my_hand, your_hand, deck):
    while (your_hand.score_hand() < 17):
        deal_a_card(your_hand, my_hand, deck)
    return your_hand


def hit_or_stay(my_hand, your_hand, deck):
    print('Chance to Bust:')
    print(bust_probability(deck, my_hand))
    print('Hit or Stay?')
    user_play_blackjack = input(': ')
    if user_play_blackjack != 'stay':
        if my_deck.card_list:
            os.system('clear')
            deal_a_card(my_hand, your_hand, deck)
            print('Your Hand: ')
            print('')
            print_a_card_list(my_hand)
            print('')
            print('Your Current Score: ')
            print(my_hand.score_hand())
            print('')
            if (my_hand.score_hand() > 21):
                print('You Bust!')
            else:
                hit_or_stay(my_hand, your_hand, deck)
        elif not my_deck.card_list:
            print('You ran out of cards!')
    return my_hand


def bust_probability(deck, hand):
    bust_list = []
    current_score = hand.score_hand()
    check_value = 22 - current_score
    for i in deck.card_list:
        if i.value >= check_value:
            bust_list.append(i)
    bust_chance = (len(bust_list))/(len(deck.card_list))
    return bust_chance


def score_the_game(my_hand, dealer_hand):
    if my_hand.score_hand() > 21:

        print('Player Busts! Dealer Wins!')

    elif (dealer_hand.score_hand() > 21) and (my_hand.score_hand() <= 21):

        print('Dealer Busts! Player Wins!')

    elif (dealer_hand.score_hand() <= 21) and (my_hand.score_hand() <= 21):

        if my_hand.score_hand() > dealer_hand.score_hand():

            print('Player Wins!')

        elif dealer_hand.score_hand() > my_hand.score_hand():

            print('Dealer Wins!')

        elif dealer_hand.score_hand() == my_hand.score_hand():

            print('A Tie! How Unlikely!')


face_list = ['2', '3', '4', '5', '6', '7', '8',
             '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suit_list = ["Spades", "Diamonds", "Hearts", "Clubs"]

my_deck = make_a_deck(face_list, suit_list)

loop_bool = True

while loop_bool:
    if len(my_deck.card_list) <= 4:
        print('You ran out of cards!')
        print('Goodbye')
        quit()
    my_hand = Hand([])
    dealer_hand = Hand([])
    double_deal_hands(my_hand, dealer_hand, my_deck)

    print('Your Hand: ')
    print_a_card_list(my_hand)
    print('')
    print('Your Current Score: ')
    print(my_hand.score_hand())
    print('')

    hit_or_stay(my_hand, dealer_hand, my_deck)
    os.system('clear')

    dealer_play_blackjack(my_hand, dealer_hand, my_deck)

    print('Your Cards:')
    print_a_card_list(my_hand)
    print('')
    print('Your Score:')
    print(my_hand.score_hand())
    print('')
    print('Dealer Cards: ')
    print_a_card_list(dealer_hand)
    print('')
    print('Dealer Score: ')
    print(dealer_hand.score_hand())
    print('')

    score_the_game(my_hand, dealer_hand)

    print('Play Again?')
    user_continue = input(': ')
    if user_continue == 'n':
        loop_bool = False
    os.system('clear')
