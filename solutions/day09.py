import os
import re


def puzzle_input(f):
    global puzzle_input
    puzzle_input = [int(line) for line in f.readlines()]


def find_number(lst, num):
    lst.sort()
    for index_i, i in enumerate(lst[:-1]):
        for j in lst[index_i + 1 :]:
            if i + j == num:
                return True

    return False


def part1():
    preamble_size = 25

    for index, value in enumerate(puzzle_input[preamble_size:], preamble_size):
        start = index - preamble_size
        end = start + preamble_size
        if not find_number(puzzle_input[start:end], value):
            return value


def part2():
    num = part1()
    last_removed_index = -1
    current_sum = 0

    for index, value in enumerate(puzzle_input):
        current_sum += value
        while current_sum > num:
            last_removed_index += 1
            current_sum -= puzzle_input[last_removed_index]
        if current_sum == num:
            sublist = sorted(puzzle_input[last_removed_index + 1 : index + 1])

            return sublist[0] + sublist[-1]
