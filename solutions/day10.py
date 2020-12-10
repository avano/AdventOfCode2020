def solve(f):
    data = sorted([int(line) for line in f.readlines()])

    return part1(data), part2(data)


def part1(data):
    differences = {1: 0, 3: 0}
    current_jolts = 0
    data.append(data[-1] + 3)

    for adapter in data:
        differences[adapter - current_jolts] += 1
        current_jolts = adapter
    return differences[1] * differences[3]


def part2(data):
    ways = {0: 1}

    for adapter in data:
        count = 0
        for previous in range(1, 4):
            if adapter - previous in ways:
                count += ways[adapter - previous]
        ways[adapter] = count
    return ways[data[-1]]
