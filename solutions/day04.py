import os
import re

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    input_list = f.read()

rules = {
    "byr": lambda year: int(year) in range(1920, 2003),
    "iyr": lambda year: int(year) in range(2010, 2021),
    "eyr": lambda year: int(year) in range(2020, 2031),
    "hgt": lambda height: int(height[: height.index("cm")]) in range(150, 194)
    if "cm" in height
    else int(height[: height.index("in")]) in range(59, 77)
    if "in" in height
    else False,
    "hcl": lambda color: bool(re.match(r"#[0-9a-f]{6}", color)),
    "ecl": lambda color: color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda password_id: len(password_id) == 9 and password_id.isnumeric(),
    "cid": lambda x: False,
}


def passport_ok(p, part):
    p = p.strip().replace("\n", " ")

    missing_fields = list(rules.keys()).copy()
    for kv in p.split(" "):
        if part == "part1":
            missing_fields.remove(kv.split(":")[0])
        else:
            key, value = kv.split(":")
            if rules[key](value):
                missing_fields.remove(key)

    return not missing_fields or (
        len(missing_fields) == 1 and missing_fields[0] == "cid"
    )


def solve(part):
    ok_passports = 0

    for passport in input_list.split("\n\n"):
        if passport_ok(passport, part):
            ok_passports += 1

    return ok_passports


def part1():
    return solve("part1")


def part2():
    return solve("part2")
