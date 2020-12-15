def solve(f):
    data = [int(num) for num in f.read().strip().split(",")]

    return part1(data), part2(data)


def _solve(data, limit):
    numbers = [0] * limit
    turn = 0
    last_number = 0
    for num in data:
        turn += 1
        numbers[num] = turn

    while True:
        turn += 1
        previous = numbers[last_number]
        numbers[last_number] = turn
        if previous == 0:
            last_number = 0
        else:
            last_number = turn - previous

        if turn + 1 == limit:
            return last_number


def part1(data):
    return _solve(data, 2020)


def part2(data):
    return _solve(data, 30000000)
