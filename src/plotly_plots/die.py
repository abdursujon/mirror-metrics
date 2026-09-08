from random import randint 

# A class representing a single die 
class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        # return a random value 1, to 6 
        return randint(1, self.num_sides)
