def solve(f):
    data = [(line[0], int(line[1:])) for line in f.readlines()]

    return part1(data), part2(data)


DIRECTIONS = {"N": (0, -1), "E": (1, 0), "W": (-1, 0), "S": (0, 1)}

ROTATIONS = ["L", "R"]


def add(v1, v2):
    return tuple(map(lambda x, y: x + y, v1, v2))


def mult(vector, value):
    return vector[0] * value, vector[1] * value


def rotate(current_direction, direction, degrees):
    for _ in range(int(degrees / 90)):
        if direction == "R":
            current_direction = -current_direction[1], current_direction[0]
        else:
            current_direction = current_direction[1], -current_direction[0]
    return current_direction


def _solve(data, part):
    ship_position = (0, 0)
    ship_direction = DIRECTIONS["E"] if part == 1 else (10, -1)
    for action, value in data:
        if action in DIRECTIONS:
            if part == 1:
                ship_position = add(ship_position, mult(DIRECTIONS[action], value))
            else:
                ship_direction = add(ship_direction, mult(DIRECTIONS[action], value))
        elif action in ROTATIONS:
            ship_direction = rotate(ship_direction, action, value)
        else:
            ship_position = add(ship_position, mult(ship_direction, value))
    return abs(ship_position[0]) + abs(ship_position[1])


def part1(data):
    return _solve(data, 1)


def part2(data):
    return _solve(data, 2)
