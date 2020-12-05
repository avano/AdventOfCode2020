import os

from solutions.util.aoc_util import Map

input_file = f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}"


def part1(slope=None):
    map = Map(input_file)
    pos = Map.Coordinate(0, 0)
    slope = Map.Coordinate(3, 1) or slope
    trees = 0

    while pos.y < len(map.get_map()):
        if map.is_tree(pos):
            trees += 1
        if pos.x + slope.x > len(map.get_row(pos.y)) - 1:
            map.resize_map()
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
