import os

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    numbers = list(map(int, f.readlines()))


def part1():
    for num in numbers:
        result = 2020 - num
        if result in numbers:
            return num * result


def part2():
    for i in numbers[:-1]:
        for j in numbers[1:]:
            result = 2020 - i - j
            if result in numbers:
                return i * j * result
