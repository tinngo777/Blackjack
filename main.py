import random
from blackjack import Blackjack
from deck import Deck
from players import Players

RANK_NAMES = {
    1: "Aces",
    11: "Jack",
    12: "Queen",
    13: "King"
}




if __name__ == "__main__":
    my_deck = Deck()
    new_deck = my_deck.deck
    used_cards = set()
    player_hand = [my_deck.shuffle() for _ in range(2)]
    used_cards.update(player_hand)

    my_players = Players()
    num_players = my_players.num_bots()
    
    names = ['Dean', 'Sam', 'Jo', 'Castiel', 'John', 'Garth']
    player_names = random.sample(names, num_players)
    players = {name: [] for name in player_names}
    for name in players:
        players[name] = list(my_deck.shuffle() for _ in range(2))



    my_blackjack = Blackjack()
    blackjack21 = False
    blackjack21 = my_blackjack.auto_win(player_hand)
    
    
    if blackjack21:
        print("You got a hand of Blackjack -> Automatically win")
        print(player_hand)
    else:
        print("Here's your cards: ")
        print(player_hand)
        print("\nThe total is: ")
        print(my_blackjack.calculate(player_hand))

    print("Here are other players' hands.\n")
    print(players)