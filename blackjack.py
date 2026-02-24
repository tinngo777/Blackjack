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
        ranks = [card[1] for card in player_hand]
        has_ace = 1 in ranks

        
        total = sum(card[1] for card in player_hand)
        if total < 21 and has_ace == True:
            if total + 10 > 21:
                if total + 9 <= 21:
                    total += 9
            else:
                total += 10
        
        return total
    

        

