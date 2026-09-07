from random import choice 

# A class to generate random walk 
class RandomWalk:
    def __init__(self, num_points=50_000):
        self.num_points = num_points
        # All walk starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    # Calculate all the points in the walk 
    def fill_walk(self):
        
        # keep taking steps until reached the end of num_points 
        while (len(self.x_values) < self.num_points):

            # decide which direction to go and how far to go 
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject moves that go nowhere 
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position 
            x = self.x_values[-1] + x_step # x_values[-1] gets the last value of list 
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
        
        