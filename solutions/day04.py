import os
import re

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}", "r") as f:
    input_list = list(f.readlines())

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
rules = {
    fields[0]: lambda year: int(year) in range(1920, 2003),
    fields[1]: lambda year: int(year) in range(2010, 2021),
    fields[2]: lambda year: int(year) in range(2020, 2031),
    fields[3]: lambda height: int(height[: height.index("cm")]) in range(150, 194)
    if "cm" in height
    else int(height[: height.index("in")]) in range(59, 77)
    if "in" in height
    else False,
    fields[4]: lambda color: bool(re.match(r"#[0-9a-f]{6}", color)),
    fields[5]: lambda color: color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    fields[6]: lambda password_id: len(password_id) == 9 and password_id.isnumeric(),
    fields[7]: lambda x: False,
}


def passport_ok(p, part):
    p = p.strip().replace("\n", " ")

    missing_fields = fields.copy()
    for kv in p.split(" "):
        if part == "part1":
            missing_fields.remove(kv.split(":")[0])
        else:
            key, value = kv.split(":")
            if rules[key](value):
                missing_fields.remove(key)

    return len(missing_fields) == 0 or (
        len(missing_fields) == 1 and missing_fields[0] == "cid"
    )


def solve(part):
    passport = ""
    ok_passports = 0
    for line in input_list:
        passport += line
        if line.strip() == "" or line == input_list[-1]:
            ok_passports += 1 if passport_ok(passport, part) else 0
            passport = ""
    return ok_passports


def part1():
    return solve("part1")


def part2():
    return solve("part2")
