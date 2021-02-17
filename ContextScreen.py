from PIL import Image

class Clue(object):
    def __init__(self):
        point = (0, 0)
        color = (255, 255, 255)
    
    def __init__(self, point, color = (255, 255, 255)):
        self.point = point
        self.color = color
    
    def appear_in(self, screenshot):
        # May be redundant
        screenshot = screenshot.convert("RGB")
        return screenshot.getpixel(self.point) == self.color


class ContextScreen(object):
    def __init__(self):
        self.name = ""
        self.clues = []

    def __init__(self, name, clues = []):
        self.name = name
        self.clues = clues

    def match(self, screen):
        for clue in self.clues:
            if not clue.appear_in(screen): return False
            print("pass")
        return True