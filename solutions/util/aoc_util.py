import os


class Map:
    def __init__(self, puzzle_input):
        self.map = [list(line.strip()) for line in puzzle_input]

    def get_map(self):
        return self.map

    def get_row(self, index):
        return self.map[index]

    def is_tree(self, position):
        return self.map[position.y][position.x] == "#"

    class Coordinate:
        def __init__(self, x, y):
            self.x = x
            self.y = y


class Bag:
    def __init__(self, color):
        self.color = color
        self.bags = None
