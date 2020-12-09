import os
import re

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    input_list = [int(line) for line in f.readlines()]

preamble_size = 25


def find_number(lst, num):
    lst.sort()
    for index_i, i in enumerate(lst[:-1]):
        for j in lst[index_i + 1 :]:
            if i + j == num:
                return True
    return False


def part1():
    for index, value in enumerate(input_list[preamble_size:], preamble_size):
        start = index - preamble_size
        end = start + preamble_size
        if not find_number(input_list[start:end], value):
            return value


def part2():
    num = part1()
    last_removed_index = -1
    current_sum = 0
    for index, value in enumerate(input_list):
        current_sum += value
        if current_sum > num:
            while True:
                last_removed_index += 1
                current_sum -= input_list[last_removed_index]
                if current_sum <= num:
                    break
        if current_sum == num:
            sublist = sorted(input_list[last_removed_index + 1 : index + 1])
            return sublist[0] + sublist[-1]
