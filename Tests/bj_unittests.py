import unittest
from Dealer import Dealer
from Card import Card
from BlackjackGUI import BlackjackGUI
from Blackjack_Game import Blackjack_Game
from Player import Player
import time 


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

    def test_randomness_of_card_dealing(self):
        game = Blackjack()
        cards = [game.deck.hit() for _ in range(100)]
        unique_cards = set(cards)
        self.assertGreater(len(unique_cards), 10, "Cards are not being dealt randomly.")

class test_dealer(unittest.TestCase):
    def test_deal(self):
        game = Blackjack()
        game.start()
        self.assertEqual(len(game.player.hand.hand), 2, "Player does not have 2 cards.")
        self.assertEqual(len(game.dealer.hand.hand), 2, "Dealer does not have 2 cards.")

    def test_stand(self):
        game = Blackjack()
        game.start()
        game.player.stand()
        self.assertFalse(game.game_over, "Game delayed after player's decision to stand.")

    def test_determine_winner_after_comparing_hands(self):
        game = Blackjack()
        game.start()
        game.determine_winner()
        self.assertTrue(game.winner is not None, "Winner was not determined after comparing hands.")

    def test_fairness_in_winner_calculation(self):
        game = Blackjack()
        game.start()
        game.determine_winner()
        self.assertTrue(game.winner in [game.player, game.dealer], "Winner calculation was not fair.")

    def test_exit_or_new_round_after_result(self):
        game = Blackjack()
        game.start()
        game.determine_winner()
        self.assertTrue(game.allow_exit_or_new_round(), "Exit or new round was not allowed.")

    def test_end_game_on_quit(self):
        game = Blackjack()
        game.quit()
        self.assertTrue(game.game_over, "Game was not ended after clicking quit.")

    def test_exit_game_within_5_seconds(self):
        start_time = time.time()
        game = Blackjack()
        game.quit()
        end_time = time.time()
        self.assertLess(end_time - start_time, 5, "Game did not exit within 5 seconds.")

    def test_compare_hands_after_played(self):
        game = Blackjack()
        game.start()
        game.player.play(game.deck)
        game.dealer.play(game.deck)
        self.assertTrue(game.compare_hands(), "Hands were not compared correctly.")

class test_blackjack(unittest.TestCase):
    def test_start(self):
        game = Blackjack()
        game.start()
