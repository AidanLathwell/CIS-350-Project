import unittest
from Card import Card
from Deck import Deck
from Hand import Hand


class test_hand(unittest.TestCase):

    def test_hand_length(self):
        card_one = Card("Spades", "1")
        card_two = Card("Diamonds", "Jack")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)

        self.assertEqual(len(hand.hand), 2)

    def test_hand_value_with_one_ace(self):
        card_one = Card("Diamonds", "Ace")
        hand = Hand()
        hand.hand.append(card_one)
        hand.calc_hand_value()

        self.assertEqual(hand.hand_value, 11)

    def test_hand_value_with_two_ace(self):
        card_one = Card("Spades", "Ace")
        card_two = Card("Diamonds", "Ace")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()

        self.assertEqual(hand.hand_value, 12)

    def test_hand_with_two_aces_and_other_card_under_twenty_one(self):
        card_one = Card("Spades", "Ace")
        card_two = Card("Diamonds", "Ace")
        card_three = Card("Clubs", "7")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.hand.append(card_three)
        hand.calc_hand_value()

        self.assertEqual(hand.hand_value, 19)

    def test_hand_with_aces_and_other_cards_over_twenty_one(self):
        card_one = Card("Spades", "Ace")
        card_two = Card("Diamonds", "Ace")
        card_three = Card("Clubs", "10")
        card_four = Card("Clubs", "10")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.hand.append(card_three)
        hand.hand.append(card_four)
        hand.calc_hand_value()

        self.assertEqual(hand.hand_value, 22)

    def test_hand_value_with_no_aces(self):
        card_one = Card("Spades", "10")
        card_two = Card("Diamonds", "7")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()

        self.assertEqual(hand.hand_value, 17)

    def test_can_hit_with_less_than_seventeen(self):
        card_one = Card("Spades", "12")
        card_two = Card("Diamonds", "4")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)

        self.assertEqual(hand.allowed_to_hit, True)

    def test_can_hit_with_more_than_seventeen_with_ace(self):
        card_one = Card("Spades", "Ace")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)

        self.assertEqual(hand.allowed_to_hit, True)