class Players:
    def __init__(self):
        pass

    def num_bots(self):
        num = int(input("Number of players you want to play with (Max: 6): "))
        while num <= 0 or num > 6:
            num = int(input("Can't be less than 1 or more than 6. Try again: "))
        
        return num
    


        