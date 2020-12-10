import re


def solve(f):
    data = f.read().strip()

    return part1(data), part2(data)


def run_instructions(instructions_list):
    acc = 0
    seen_ids = set()
    i = 0

    while True:
        if i in seen_ids:
            return acc, False
        if i == len(instructions_list):
            return acc, True

        seen_ids.add(i)
        op, value = instructions_list[i].split(" ")
        if op == "acc":
            acc += int(value)
        i += int(value) if op == "jmp" else 1


def part1(data):
    return run_instructions(data.split("\n"))[0]


def part2(data):
    for instruction_list in generate_instructions_lists(data):
        acc, ok = run_instructions(instruction_list.split("\n"))
        if ok:
            return acc


def generate_instructions_lists(data):
    for match in re.finditer("jmp|nop", data):
        index = match.start()
        replaced = (
            data[:index]
            + ("nop" if match.group(0) == "jmp" else "jmp")
            + data[index + 3 :]
        )

        yield replaced
