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

def format_card(card):
    suit = card[0].capitalize()
    rank = card[1]

    display_rank = RANK_NAMES.get(rank, rank)
    return f"{display_rank} of {suit}"


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
    if my_blackjack.auto_win(player_hand):
        print("You got a hand of Blackjack -> You Win!")
    else:
        print("Your cards: ", [format_card(c) for c in player_hand])
        print("Total: ", my_blackjack.calculate(player_hand))
    
    print("\nOther Players:")
    for name, hand in players.items():
        bots_hand = [format_card(c) for c in hand]
        print(f"{name}: {', '.join(bots_hand)}")