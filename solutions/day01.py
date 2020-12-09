import os


def puzzle_input(f):
    global puzzle_input
    puzzle_input = [int(line) for line in f.readlines()]


def part1():
    for num in puzzle_input:
        result = 2020 - num
        if result in puzzle_input:
            return num * result


def part2():
    for i in puzzle_input[:-1]:
        for j in puzzle_input[1:]:
            result = 2020 - i - j
            if result in puzzle_input:
                return i * j * result
