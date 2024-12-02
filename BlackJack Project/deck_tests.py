import unittest
from Deck import Deck

class test_deck(unittest.TestCase):

    def test_deck_empty(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 0)

    def test_deck_created(self):
        deck = Deck()

        self.assertEqual(len(deck.deck), 0)
        deck.create_deck()
        self.assertEqual(len(deck.deck), 312)

    def test_deck_is_randomized(self):
        deck = Deck()
        deck_two = Deck()

        """ Deck always creates in the same order, by creating 2 decks, I am 
            checking that after creating deck one and two, which will be the
            same state, that deck two is different after randomizing."""
        deck.create_deck()
        starting_card_before_shuffle = deck.hit()
        deck_two.create_deck()
        deck_two.shuffle_deck()
        starting_card_before_shuffle_2 = deck_two.hit()

        self.assertIsNot(starting_card_before_shuffle.value, starting_card_before_shuffle_2.value)

    def test_deck_hit(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        deck.hit()

        # deck should be one less because hitting removes a card
        self.assertEqual(len(deck.deck), 311)