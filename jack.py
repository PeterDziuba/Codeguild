import os
import random

class Card:
	def __init__(self, string, number, suit, value):
		self.number = number
		self.suit = suit
		self.string = string
		self.value = value

	def __str__(self):
		my_magic_str = 'The {} has a value of {}'.format(self.string, self.value)
		return my_magic_str

	def __eq__(self, other):
		return (self.number == other.number) and (self.suit == other.suit)

class Hand:
	def __init__(self, card_1, card_2):
		self.card_1 = card_1
		self.card_2 = card_2

	def __str__(self):
		my_hand_list = "{} {}".format(self.card_1, self.card_2)
		return my_hand_list

	def hand_value(self):
		hand_value = self.card_1.value + self.card_2.value
		return hand_value

def make_a_card(string, dict):
	if string in dict.keys():
		my_card = Card(string, dict[string][0], dict[string][1], dict[string][2])
		return my_card

def deal_initial_hand(list, dict):
	starting_hand = []
	while len(starting_hand) < 2:
		card_1_seed = random.choice(list)
		card_1_root = make_a_card(card_1_seed, dict)
		if card_1_root not in starting_hand: starting_hand.append(card_1_root)
		card_2_seed = random.choice(list)
		card_2_root = make_a_card(card_2_seed, dict)
		if card_2_root not in starting_hand: starting_hand.append(card_2_root)
	my_starting_hand = Hand(card_1_root, card_2_root)
	return my_starting_hand

def score_hand(hand):
	hand_score = 0
	hand_score += hand.card_1.value
	hand_score += hand.card_2.value
	return hand_score

def return_bust(hand_score):
	if hand_score > 21:
		return 'Bust!'

def user_make_a_card():
	user_card_suit = input('What suit?\n: ')
	user_card_number = input('What face or number?\n: ')
	user_card_string = '{} of {}'.format(user_card_number, user_card_suit)
	if user_card_number in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:

		user_card_value = int(my_number)

	elif user_card_number in ["Jack", "Queen", "King"]:

		user_card_value = 10

	elif user_card_number == 'Ace': user_card_value = 11
	new_card = Card(user_card_string, user_card_number, user_card_suit, user_card_value)
	return new_card



cards_52_deck_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits_4_list = ["Spades", "Diamonds", "Hearts", "Clubs"]
reference_52 = []
pickup_52 = []
card_deck_dict = {}

for i in suits_4_list:

	for j in cards_52_deck_list:

		my_number = j

		if my_number in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:

			my_value = int(my_number)

		elif my_number in ["Jack", "Queen", "King"]:

			my_value = 10

		elif my_number == 'Ace': my_value = 11

		my_suit = i
		my_line = "{} of {}".format(j, i)
		long_line = [my_line, my_value]
		reference_52.append(my_line)
		pickup_52.append(long_line)
		card_deck_dict[my_line] = [my_number, my_suit, my_value]


the_new_52 = sorted(pickup_52, key=lambda x: x[1])
print(the_new_52)
my_hand = deal_initial_hand(reference_52, card_deck_dict)
print(my_hand)
print(my_hand.hand_value())
card_test_one = user_make_a_card()
card_test_two = user_make_a_card()
hand_test_one = Hand(card_test_one, card_test_two)
print(hand_test_one)
hand_score_test = score_hand(hand_test_one)
print(hand_score_test)


