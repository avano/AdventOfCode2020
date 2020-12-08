import os
import re

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    inputText = f.read().strip()


def run_instructions(instructions_list):
    acc = 0
    seen_ids = []
    i = 0
    while True:
        if i in seen_ids:
            return acc, False
        if i == len(instructions_list):
            return acc, True
        seen_ids.append(i)
        op, value = instructions_list[i].split(" ")
        if op == "acc":
            acc += int(value)
        i += int(value) if op == "jmp" else 1


def part1():
    return run_instructions(inputText.split("\n"))[0]


def part2():
    for instruction_list in create_instructions_lists():
        acc, ok = run_instructions(instruction_list.split("\n"))
        if ok:
            return acc


def create_instructions_lists():
    instructions_lists = []
    for instr in ["jmp", "nop"]:
        for match in re.finditer(instr, inputText):
            index = match.start()
            replaced = (
                inputText[:index]
                + ("nop" if instr == "jmp" else "jmp")
                + inputText[index + 3 :]
            )
            instructions_lists.append(replaced)
    return instructions_lists
