def solve(f):
    data = f.readlines()

    return part1(data), part2(data)


def find_in_range(min_range, max_range, code):
    for c in code:
        half_elements = ((max_range - min_range) // 2) + 1
        if c in ["F", "L"]:
            max_range -= half_elements
        else:
            min_range += half_elements

    return min_range


def part1(data):
    max_seat_id = 0
    for code in data:
        row = find_in_range(0, 127, code.strip()[:7])
        column = find_in_range(0, 7, code.strip()[-3:])
        seat_id = row * 8 + column
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id


def part2(data):
    ids = []
    for code in data:
        row = find_in_range(0, 127, code.strip()[:7])
        column = find_in_range(0, 7, code.strip()[-3:])
        ids.append(row * 8 + column)
    ids.sort()

    for i in range(len(ids) - 1):
        if ids[i + 1] - ids[i] == 2:
            return ids[i] + 1
