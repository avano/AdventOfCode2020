import os


def solve(f):
    data = [int(line) for line in f.readlines()]

    return part1(data), part2(data)


def part1(data):
    for num in data:
        result = 2020 - num
        if result in data:
            return num * result


def part2(data):
    for i in data[:-1]:
        for j in data[1:]:
            result = 2020 - i - j
            if result in data:
                return i * j * result
