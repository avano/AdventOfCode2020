import os


class Map:
    map = []

    def __init__(self, file):
        m = []
        with open(file, "r") as f:
            for line in f.readlines():
                m.append(list(line.strip()))
        self.map = m

    def get(self, *args):
        if (len(args)) == 0:
            return self._get_map()
        if len(args) == 1:
            if isinstance(args[0], self.Coordinate):
                return self._get_position(args[0])
            else:
                return self._get_row(args[0])

    def _get_map(self):
        return self.map

    def _get_row(self, index):
        return self._get_map()[index]

    def _get_position(self, position):
        return self._get_map()[position.y][position.x]

    class Coordinate:
        x, y = 0, 0

        def __init__(self, x, y):
            self.x = x
            self.y = y
