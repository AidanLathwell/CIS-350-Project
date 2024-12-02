import unittest
from Deck import Deck
from Player import Player

class test_player(unittest.TestCase):

    def test_hit_once(self):
        player = Player("Player", 100)
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()

        self.assertEqual(len(player.hand.hand), 0)
        player.hit(deck)
        self.assertEqual(len(player.hand.hand), 1)

    def test_hit_twice_same_hand(self):
        player = Player("Player", 100)
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()

        self.assertEqual(len(player.hand.hand), 0)
        player.hit(deck)
        player.hit(deck)
        self.assertEqual(len(player.hand.hand), 2)

    def test_stand(self):
        player = Player("Player", 100)
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        player.stand()

        self.assertEqual(len(player.hand.hand), 0)

    def test_double(self):
        player = Player("Player", 100)
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()

        self.assertEqual(len(player.hand.hand), 0)
        player.double(deck)
        self.assertEqual(len(player.hand.hand), 1)