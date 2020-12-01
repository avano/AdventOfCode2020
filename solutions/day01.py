import os

with open(os.path.dirname(os.path.realpath(__file__)) + "/input/day01.txt", "r") as f:
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
