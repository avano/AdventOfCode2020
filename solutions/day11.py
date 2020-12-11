from solutions.util.aoc_util import Map


def solve(f):
    data = f.readlines()

    return part1(data), part2(data)


ADJACENT_VECTORS = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def process_seat(map_object, coordinate, processed, part):
    current = map_object.map[coordinate[1]][coordinate[0]]

    if current == ".":
        return current

    if part == 1:
        if current != "#":
            processed = None
        seats, max_count = (
            get_adjacent_occupied_seats_count(map_object, coordinate, processed),
            4,
        )
    else:
        seats, max_count = get_visible_occupied_seat_count(map_object, coordinate), 5

    if current == "L":
        return "#" if seats == 0 else current
    elif current == "#":
        return "L" if seats >= max_count else current
    else:
        return current


def get_adjacent_occupied_seats_count(map_object, coordinate, processed=None):
    occupied = 0
    for vector in ADJACENT_VECTORS:
        adjacent = tuple(map(lambda x, y: x + y, coordinate, vector))
        if map_object.in_range(adjacent):
            value = map_object.map[adjacent[1]][adjacent[0]]
            if value == "#":
                occupied += 1
            elif value == "L":
                if processed is not None:
                    processed.add(adjacent)
    return occupied


def get_visible_occupied_seat_count(map_object, coordinate):
    occupied = 0
    for vector in ADJACENT_VECTORS:
        i = 1
        c = (coordinate[0] + (vector[0] * i), coordinate[1] + (vector[1] * i))
        while map_object.in_range(c):
            val = map_object.map[c[1]][c[0]]
            if val == "#":
                occupied += 1
                break
            elif val == "L":
                break
            i += 1
            c = (coordinate[0] + (vector[0] * i), coordinate[1] + (vector[1] * i))
    return occupied


def _solve(data, part):
    occupied_seats = 0
    previous_state = Map(data)
    state_changed = True
    already_processed = set()

    while state_changed:
        new_state = []
        for c in previous_state.coordinates():
            if c in already_processed:
                processed_seat = previous_state.map[c[1]][c[0]]
            else:
                processed_seat = process_seat(
                    previous_state, c, already_processed, part
                )
                if processed_seat == "#":
                    occupied_seats += 1
            if c[0] == 0:
                new_state.append([])
            new_state[-1].append(processed_seat)
        state_changed = previous_state.map != new_state
        if not state_changed:
            return occupied_seats
        previous_state.map = new_state
        occupied_seats = 0


def part1(data):
    return _solve(data, 1)


def part2(data):
    return _solve(data, 2)
