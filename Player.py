from Hand import Hand

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.hand = Hand()
        self.balance = balance

    def __str__(self):
        return f"Player: {self.name}, Balance: {self.balance}, Hand: {self.hand}"

    def place_bets(self, amount):
        pass

    def hit(self, deck):
        if self.hand.hand_value <= 17:
            if self.hand.allowed_to_hit is True:
                card = deck.hit()
                if card:
                    self.hand.hand.append(card)
                    self.hand.calc_hand_value()
                if self.hand.hand_value >= 17:
                    self.hand.allowed_to_hit = False
        return self.hand

    def stand(self):
        self.hand.allowed_to_hit = False
        return self.hand

    def double(self, deck):
        if self.hand.hand_value <= 17:
            if self.hand.allowed_to_hit is True:
                card = deck.hit()
                self.hand.hand.append(card)
                self.hand.allowed_to_hit = False
                self.hand.calc_hand_value()
        return self.hand

    def split(self):
        pass

    def check_bust(self):
        bust = False
        if self.hand.hand_value > 21:
            bust = True
        return bust

# from Deck import Deck
#
# deck = Deck()
# deck.create_deck()
# deck.shuffle_deck()
#
# test = Player("Logan", 100)
# print(test)
# test.hit(deck)
# print(test)
# test.hit(deck)
# print(test)
# test.hit(deck)
# print(test)
# test.hit(deck)
# test.hit(deck)
# print(test)
#
# print(test.hand.hand_value)
# print(test.hand.allowed_to_hit)
# print(test.check_bust())
