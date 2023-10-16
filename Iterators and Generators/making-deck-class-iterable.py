# Making the Deck Class Iterable

from random import shuffle

class Card:
	# Class Attributes
	suits_allowed = ["Hearts", "Diamonds", "Clubs", "Spades"]
	values_allowed = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	def __init__(self, suit, value):
		if suit not in Card.suits_allowed:
			raise ValueError(f"You can't have a {suit} card!")
		if value not in Card.values_allowed:
			raise ValueError(f"You can't have a {value} card!")
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:
	def __init__(self):
		self.cards = [Card(s,v) for s in Card.suits_allowed for v in Card.values_allowed]

	def __repr__(self):
		return f"Deck of {len(self.cards)} cards"

	# **This method allows us to iterate through the deck of cards
	def __iter__(self):
		return iter(self.cards)

	# *Once we learn generators, we can also write it this way:
	# def __iter__(self):
	#	for card in self.cards:
	#		yield card

	def count(self):
		return len(self.cards)

	def _deal(self, value=1):
		if len(self.cards) < value:
			if len(self.cards) == 0:
			    raise ValueError("All cards have been dealt")
			return [self.cards.pop() for c in range(len(self.cards))]
		return [self.cards.pop() for c in range(value)]

	def shuffle(self):
		if len(self.cards) != 52:
			raise ValueError("Only full decks can be shuffled")
		return shuffle(self.cards)

	def deal_card(self):
		return self._deal()[0]

	def deal_hand(self, hand):
		return self._deal(hand)

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
	print(card)