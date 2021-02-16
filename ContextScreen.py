class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Clue(object):
    def __init__(self):
        point = Point()
        color = (255, 255, 255)
    
    def __init__(self, point, color = (255, 255, 255)):
        self.point = point
        self.color = color


class ContextScreen(object):
    def __init__(self):
        self.name = ""
        self.clues = []