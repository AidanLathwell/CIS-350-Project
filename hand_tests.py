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
        hand_value = hand.calc_hand_value()

        self.assertEqual(hand_value, 11)

    def test_hand_value_with_two_ace(self):
        card_one = Card("Spades", "Ace")
        card_two = Card("Diamonds", "Ace")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand_value = hand.calc_hand_value()

        self.assertEqual(hand_value, 12)

    def test_hand_with_two_aces_and_other_card_under_twenty_one(self):
        card_one = Card("Spades", "Ace")
        card_two = Card("Diamonds", "Ace")
        card_three = Card("Clubs", "7")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.hand.append(card_three)
        hand_value = hand.calc_hand_value()

        self.assertEqual(hand_value, 19)

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
        hand_value = hand.calc_hand_value()

        self.assertEqual(hand_value, 22)

    def test_hand_value_with_no_aces(self):
        card_one = Card("Spades", "10")
        card_two = Card("Diamonds", "7")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand_value = hand.calc_hand_value()

        self.assertEqual(hand_value, 17)

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

    def test_allowed_to_split(self):
        card_one = Card("Spades", "9")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()

        self.assertEqual(hand.allowed_to_split, True)

    def test_not_allowed_to_split(self):
        card_one = Card("Spades", "3")
        card_two = Card("Diamonds", "7")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()

        self.assertEqual(hand.allowed_to_split, False)

    def test_hand_length_longer_after_hit(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        card_one = Card("Spades", "9")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.hit(deck)

        self.assertEqual(len(hand.hand) == 3, True)

    def test_hand_value_after_hit(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        card_one = Card("Spades", "9")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.hit(deck)
        new_hand_value = 18

        if (hand.hand[-1].value == "King" or hand.hand[-1].value == "Jack" or
                hand.hand[-1].value == "Queen"):
            new_hand_value += 10
        elif hand.hand[-1].value == "Ace":
            if (hand.hand_value + 11) < 21:
                new_hand_value += 1
            else:
                new_hand_value += 11
        else:
            new_hand_value += int(hand.hand[-1].value)

        self.assertEqual(hand.hand_value, new_hand_value)

    def test_hand_value_after_stand(self):
        card_one = Card("Spades", "9")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()
        hand.stand()

        self.assertEqual(hand.hand_value, 18)

    def test_can_hit_after_hit(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        card_one = Card("Spades", "5")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()
        hand.hit(deck)

        if hand.allowed_to_hit:
            self.assertEqual(hand.allowed_to_hit, True)
        else:
            self.assertEqual(hand.allowed_to_hit, False)

    def test_can_hit_after_stand(self):
        card_one = Card("Spades", "9")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.stand()

        self.assertEqual(hand.allowed_to_hit, False)

    def test_can_double(self):
        card_one = Card("Spades", "5")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()

        self.assertEqual(hand.already_hit, False)
        self.assertEqual(hand.allowed_to_hit, True)

    def test_can_not_double_because_already_hit(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        card_one = Card("Spades", "5")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()
        hand.hit(deck)

        self.assertEqual(hand.already_hit, True)

    def test_hand_length_after_double(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        card_one = Card("Spades", "9")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.double(deck)

        self.assertEqual(len(hand.hand) == 3, True)

    def test_can_hit_after_double(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle_deck()
        card_one = Card("Spades", "5")
        card_two = Card("Diamonds", "9")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()
        hand.hit(deck)

        self.assertEqual(hand.already_hit, True)

    def test_if_hand_allowed_to_hit(self):
        card_one = Card("Spades", "7")
        card_two = Card("Diamonds", "3")
        hand = Hand()
        hand.hand.append(card_one)
        hand.hand.append(card_two)
        hand.calc_hand_value()
        hand.calc_ability_to_hit()

        self.assertEqual(hand.allowed_to_hit, True)

        # card_one = Card("Spades", "Ace")
        # card_two = Card("Diamonds", "Ace")
        # card_three = Card("Clubs", "10")
        # card_four = Card("Clubs", "10")
        # card_five = Card("Clubs", "3")
        # hand = Hand()
        # hand.hand.append(card_one)
        # hand.hand.append(card_two)
        # hand.hand.append(card_three)
        # hand.hand.append(card_four)
        # hand.hand.append(card_five)
        # hand.calc_hand_value()
        # check_hit = hand.calc_ability_to_hit()
        #
        # self.assertEqual(check_hit, False)

