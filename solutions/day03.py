import os

from solutions.util.aoc_util import Map


def puzzle_input(f):
    global puzzle_input
    puzzle_input = f.readlines()


def part1(slope=None):
    map = Map(puzzle_input)
    pos = Map.Coordinate(0, 0)
    slope = slope or Map.Coordinate(3, 1)
    trees = 0

    while pos.y < len(map.get_map()):
        if map.is_tree(pos):
            trees += 1
        pos.x, pos.y = (pos.x + slope.x) % len(map.get_row(pos.y)), pos.y + slope.y

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
