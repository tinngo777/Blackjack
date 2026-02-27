from deck import Deck

class Blackjack:
    pass

    def auto_win(self, player_hand):
        if len(player_hand) > 2:
            return False
        ranks = [card[1] for card in player_hand]
        has_ace = 1 in ranks
        has_ten_value = any(r in [10, 11, 12, 13] for r in ranks)
        if has_ace and has_ten_value:
            return True

    def calculate(self, player_hand):
        values = [(card[1] if card[1] <= 10 else 10) for card in player_hand]
        has_ace = 1 in values
        total = sum(values)

        
        if has_ace and total + 10 <= 21:
            total += 10
        
        return total
    

        

