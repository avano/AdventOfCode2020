class Map:
    def __init__(self, puzzle_input):
        self.map = [list(line.strip()) for line in puzzle_input]

    def get_map(self):
        return self.map

    def get_row(self, index):
        return self.map[index]

    def in_range(self, coordinate):
        return 0 <= coordinate[1] < len(self.map) and 0 <= coordinate[0] < len(
            self.map[0]
        )

    def coordinates(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                yield x, y


class Bag:
    def __init__(self, color):
        self.color = color
        self.bags = None
