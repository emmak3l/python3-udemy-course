# Unit Tests for the cardsdeck.py File

import unittest
from cardsdeck import Card, Deck

class CardTests(unittest.TestCase):
	def setUp(self):
		self.card = Card("Hearts", "Q")

	def test_init(self):
		"""cards should have a suit and a value"""
		self.assertEqual(self.card.suit, "Hearts")
		self.assertEqual(self.card.value, "Q")

	def test_init_suit_error(self):
		"""a ValueError should be raised if an invalid suit is used"""
		with self.assertRaises(ValueError):
			Card("Hexagons", '2')

	def test_init_value_error(self):
		"""a ValueError should be raised if an invalid value is used"""
		with self.assertRaises(ValueError):
			Card("Clubs", '11')

	def test_repr(self):
		"""__repr__ should return a string 'VALUE of SUIT'"""
		self.assertEqual(repr(self.card), 'Q of Hearts')


class DeckTests(unittest.TestCase):
	def setUp(self):
		self.deck = Deck()

	def test_init(self):
		"""the cards attribute of the deck should be a list that contains 52 cards"""
		self.assertEqual(len(self.deck.cards), 52)
		self.assertTrue(isinstance(self.deck.cards, list))

	def test_repr(self):
		"""__repr__ should return a string 'Deck of {len(self.cards)} cards'"""
		self.assertEqual(repr(self.deck), 'Deck of 52 cards')

	def test_count(self):
		"""count should return the length of the cards list"""
		self.assertEqual(len(self.deck.cards), 52)
		self.deck.deal_card()
		self.assertEqual(len(self.deck.cards), 51)

	def test_deal_sufficient_cards(self):
		"""_deal should pop the number of cards specified and should remove them from the cards list for the deck"""
		cards = self.deck._deal(5)
		self.assertEqual(len(cards), 5)
		self.assertEqual(len(self.deck.cards), 47)

	def test_deal_insufficient_cards(self):
		"""_deal should pop the remaining cards in the deck if the user requests more dealt than what remains"""
		self.cards = self.deck._deal(50)
		self.assertEqual(len(self.deck._deal(4)), 2)
	
	def test_deal_no_cards(self):
		"""_deal should raise a ValueError when there are no cards remaining in the deck"""
		self.deck._deal(52)
		with self.assertRaises(ValueError):
		 	self.deck._deal()

	def test_shuffle_full_deck(self):
		"""a shuffled deck should not equal a non-shuffled deck"""
		self.assertNotEqual(self.deck.shuffle(), self.deck)
	
	def test_shuffle_not_full_deck(self):
		"""A ValueError should be raised if we try to shuffle a deck that's not full"""
		self.deck._deal(2)
		with self.assertRaises(ValueError):
			self.deck.shuffle()

	def test_deal_card(self):
		"""deal_card should return one card and remove it from the cards list from the deck"""
		card = self.deck.cards[-1]
		dealt_card = self.deck.deal_card()
		self.assertEqual(card, dealt_card)
		self.assertEqual(len(self.deck.cards), 51)

	def test_deal_hand(self):
		"""deal_hand should return the number of cards the user specified and remove them from the cards list of the deck"""
		cards = self.deck.deal_hand(7)
		self.assertEqual(len(cards), 7)
		self.assertEqual(len(self.deck.cards), 45)


if __name__ == "__main__":
	unittest.main()