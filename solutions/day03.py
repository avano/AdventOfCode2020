import os

from solutions.util.aoc_util import Map

input_file = os.path.dirname(os.path.realpath(__file__)) + "/input/day03.txt"


def resize_map(map):
    for row in map.get():
        row.extend(row)


def is_tree(map, pos):
    return map.get(pos) == "#"


def part1(*args):
    map = Map(input_file)
    pos = Map.Coordinate(0, 0)
    slope = Map.Coordinate(3, 1) if len(args) == 0 else args[0]
    trees = 0

    while pos.y < len(map.get()):
        trees += 1 if is_tree(map, pos) else 0
        if pos.x + slope.x > len(map.get(pos.y)) - 1:
            resize_map(map)
        pos.x, pos.y = pos.x + slope.x, pos.y + slope.y

    return trees


def part2():
    slopes = [
        Map.Coordinate(1, 1),
        Map.Coordinate(5, 1),
        Map.Coordinate(7, 1),
        Map.Coordinate(1, 2),
    ]
    trees = part1()

    for slope in slopes:
        trees *= part1(slope)
    return trees
