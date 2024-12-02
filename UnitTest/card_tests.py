import unittest
from Deck import Deck
from Card import Card


class test_card(unittest.TestCase):

    def test_is_ace(self):
        card = Card("Diamonds", "Ace")
        self.assertEqual(card.value, "Ace")

    def test_is_two(self):
        card = Card("Diamonds", "2")
        self.assertEqual(card.value, "2")

    def test_is_three(self):
        card = Card("Diamonds", "3")
        self.assertEqual(card.value, "3")

    def test_is_four(self):
        card = Card("Diamonds", "4")
        self.assertEqual(card.value, "4")

    def test_is_five(self):
        card = Card("Diamonds", "5")
        self.assertEqual(card.value, "5")

    def test_is_six(self):
        card = Card("Diamonds", "6")
        self.assertEqual(card.value, "6")

    def test_is_seven(self):
        card = Card("Diamonds", "7")
        self.assertEqual(card.value, "7")

    def test_is_eight(self):
        card = Card("Diamonds", "8")
        self.assertEqual(card.value, "8")

    def test_is_nine(self):
        card = Card("Diamonds", "9")
        self.assertEqual(card.value, "9")

    def test_is_ten(self):
        card = Card("Diamonds", "10")
        self.assertEqual(card.value, "10")

    def test_is_jack(self):
        card = Card("Diamonds", "Jack")
        self.assertEqual(card.value, "Jack")

    def test_is_queen(self):
        card = Card("Diamonds", "Queen")
        self.assertEqual(card.value, "Queen")

    def test_is_king(self):
        card = Card("Diamonds", "King")
        self.assertEqual(card.value, "King")

    def test_is_cut_card(self):
        card = Card("Diamonds", "Cut Card")
        self.assertEqual(card.value, "Cut Card")

    def test_is_diamonds(self):
        card = Card("Diamonds", "1")
        self.assertEqual(card.suit, "Diamonds")

    def test_is_spades(self):
        card = Card("Spades", "1")
        self.assertEqual(card.suit, "Spades")

    def test_is_hearts(self):
        card = Card("Hearts", "1")
        self.assertEqual(card.suit, "Hearts")

    def test_is_clubs(self):
        card = Card("Clubs", "1")
        self.assertEqual(card.suit, "Clubs")

    def test_is_correct_suit_and_value(self):
        card = Card("Spades", "Ace")
        self.assertEqual(card.value, "Ace")
        self.assertEqual(card.suit, "Spades")