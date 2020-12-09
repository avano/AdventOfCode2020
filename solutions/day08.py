import os
import re


def puzzle_input(f):
    global puzzle_input
    puzzle_input = f.read().strip()


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


def part1():
    return run_instructions(puzzle_input.split("\n"))[0]


def part2():
    for instruction_list in generate_instructions_lists():
        acc, ok = run_instructions(instruction_list.split("\n"))
        if ok:
            return acc


def generate_instructions_lists():
    for match in re.finditer("jmp|nop", puzzle_input):
        index = match.start()
        replaced = (
            puzzle_input[:index]
            + ("nop" if match.group(0) == "jmp" else "jmp")
            + puzzle_input[index + 3 :]
        )

        yield replaced
