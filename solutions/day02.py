import os
import re

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    rules = list(f.readlines())

pattern = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$")


def solve(part):
    valid_passwords = 0
    for rule in rules:
        search = re.search(pattern, rule)
        low, high, char, password = (
            int(search.group(1)),
            int(search.group(2)),
            search.group(3),
            search.group(4),
        )
        if part == "part1":
            valid_passwords += 1 if password.count(char) in range(low, high + 1) else 0
        else:
            password = password[low - 1] + password[high - 1]
            valid_passwords += 1 if password.count(char) == 1 else 0
    return valid_passwords


def part1():
    return solve("part1")


def part2():
    return solve("part2")
