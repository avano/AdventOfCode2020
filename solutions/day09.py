import os
import re


def solve(f):
    data = [int(line) for line in f.readlines()]

    part1_result = part1(data)
    return part1_result, part2(data, part1_result)


def find_number(lst, num):
    lst.sort()
    for index_i, i in enumerate(lst[:-1]):
        for j in lst[index_i + 1 :]:
            if i + j == num:
                return True

    return False


def part1(data):
    preamble_size = 25

    for index, value in enumerate(data[preamble_size:], preamble_size):
        start = index - preamble_size
        end = start + preamble_size
        if not find_number(data[start:end], value):
            return value


def part2(data, num):
    last_removed_index = -1
    current_sum = 0

    for index, value in enumerate(data):
        current_sum += value
        while current_sum > num:
            last_removed_index += 1
            current_sum -= data[last_removed_index]
        if current_sum == num:
            sublist = sorted(data[last_removed_index + 1 : index + 1])

            return sublist[0] + sublist[-1]
