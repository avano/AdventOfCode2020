import re

RULE_PATTERN = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$")


def solve(f):
    data = f.readlines()

    return part1(data), part2(data)


def _solve(part, rules):
    valid_passwords = 0

    for rule in rules:
        search = re.search(RULE_PATTERN, rule)
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


def part1(data):
    return _solve("part1", data)


def part2(data):
    return _solve("part2", data)
