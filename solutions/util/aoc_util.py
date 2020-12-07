import os


class Map:
    def __init__(self, file):
        self.map = []

        with open(file, "r") as f:
            for l in f.readlines():
                self.map.append(list(l.strip()))

    def get_map(self):
        return self.map

    def get_row(self, index):
        return self.map[index]

    def is_tree(self, position):
        return self.map[position.y][position.x] == "#"

    def resize_map(self):
        for row in self.map:
            row.extend(row)

    class Coordinate:
        def __init__(self, x, y):
            self.x = x
            self.y = y


class Bag:
    color = None
    bags = None

    def __init__(self, color):
        self.color = color
