import random


class Card:
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return f"{self.rank}"


class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(rank) for rank in ranks]
        self.cards *= 4
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_cards(self):
        self.player_hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer_hand = [self.deck.draw_card(), self.deck.draw_card()]

    def get_hand_value(self, hand):
        value = 0
        aces = 0
        for card in hand:
            if card.rank == 'Ace':
                aces += 1
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                value += int(card.rank)

        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        return value

    def player_turn(self):
        while self.get_hand_value(self.player_hand) <= 21:
            print("Player hand:", ', '.join(str(card) for card in self.player_hand))
            print("Player hand value:", self.get_hand_value(self.player_hand))
            print("Dealer hand :", self.dealer_hand[0])
            hit_again = input("Hit or Stand ? (h/s): ")
            if hit_again == 'h':
                self.player_hand.append(self.deck.draw_card())
            elif hit_again == 's':
                break

    def dealer_turn(self):
        while self.get_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw_card())

    def check_win(self):
        player_value = self.get_hand_value(self.player_hand)
        dealer_value = self.get_hand_value(self.dealer_hand)

        print("Player hand:", ', '.join(str(card) for card in self.player_hand))
        print("Player hand value:", player_value)

        print("Dealer hand:", ', '.join(str(card) for card in self.dealer_hand))
        print("Dealer hand value:", dealer_value)

        if player_value > 21:
            print("Player lose")
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player win")
        elif player_value == dealer_value:
            print("Equal")
        else:
            print("dealer wins")

    def play(self):
        print("start")
        self.deal_initial_cards()
        self.player_turn()
        if self.get_hand_value(self.player_hand) <= 21:
            self.dealer_turn()
            self.check_win()
        else:
            print('Player lose')

if __name__ == "__main__":
    game = Blackjack()
    game.play()
