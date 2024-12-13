import random

class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def move(self, Delta_x, Delta_y):
        return Location(self.x + Delta_x, self.y + Delta_y)

    def distance(self, the_other_object):
        # Pythagorean theorem for distance: c^2 = a^2 + b^2     
        # Same for points: distance = sqrt( (x1-x2)^2 + (y1-y2)^2 ) -- > Euclidean distance 
        return ( (self.x - the_other_object.get_x() )**2 + (self.y - the_other_object.get_y() )**2 )**0.5
    
class Walker:
    
    def __init__(self, name=None):
        self.name = name
        
    def takeStep(self) -> tuple:
        choices = [(0,0), (0,1), (1,0), (1,1)]
        return random.choice(choices)
    
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
    
class Land:

    def __init__(self):
        self.walkers = {}
    
    def addWalker(self, walker, location):
        if walker in self.walkers:
            raise ValueError('This walker already exist')
        else:
            self.walkers[walker] = location
    
    def moveWalker(self, walker):
        if walker not in self.walkers:
            raise ValueError('This walker does not exist')
        else:
            deltax, deltay = walker.takeStep()
            self.walkers[walker] = self.walkers[walker].move(deltax, deltay)

    def locate(self, walker):
        if walker not in self.walkers:
            raise ValueError('This walker does not exist')
        return self.walkers[walker]