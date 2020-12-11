from solutions.util.aoc_util import Map


def solve(f):
    data = f.readlines()

    return part1(data), part2(data)


def is_tree(map_object, coordinate):
    return map_object.map[coordinate[1]][coordinate[0]] == "#"


def part1(data, slope=None):
    map_object = Map(data)
    pos = (0, 0)
    slope = slope or (3, 1)
    trees = 0

    while pos[1] < len(map_object.get_map()):
        if is_tree(map_object, pos):
            trees += 1
        pos = ((pos[0] + slope[0]) % len(map_object.get_row(pos[1])), pos[1] + slope[1])

    return trees


def part2(data):
    slopes = [
        (1, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees = part1(data)

    for slope in slopes:
        trees *= part1(data, slope)

    return trees
