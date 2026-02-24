import random


class Deck:
    def __init__(self):
        clubs = [("clubs", i) for i in range(1,14)]
        spades = [("spades", i) for i in range(1,14)]
        hearts = [("hearts", i) for i in range(1,14)]
        diamonds = [("diamonds", i) for i in range(1,14)]
        self.deck = clubs + spades + hearts + diamonds


    def shuffle(self):
        random.shuffle(self.deck)
        card1, card2 = self.deck.pop()
        return card1, card2


    def pick_card(self):
        card_picked = self.deck.pop()
        return card_picked


if __name__ == "__main__":
    my_deck = Deck()
    new_deck = my_deck.deck 
    print(new_deck, '\n')

    
    player_hand = [my_deck.shuffle() for _ in range(2)]
    print(player_hand)