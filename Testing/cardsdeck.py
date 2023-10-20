# ** This is a copy of the original deck-of-cards-exercise.py solution,
# I made a copy so that the file name didn't have any dashes when I try to import it to the test file **

# Deck of Cards OOP Exercise

# Introduction
# Your goal in this exercise is to implement two classes, Card  and Deck 


# Specifications
# Card:
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

# Deck:
# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

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