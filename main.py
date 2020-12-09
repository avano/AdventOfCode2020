import glob
import importlib

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        days = sys.argv[1:]
    else:
        file_count = len(
            glob.glob1(
                f"{os.path.dirname(os.path.realpath(__file__))}/solutions", "*.py"
            )
        )
        days = []
        for i in range(file_count):
            days.append(str(i + 1).zfill(2))
    for day_num in days:
        solution = importlib.import_module(f"solutions.day{day_num}")

        with open(
            f"{os.path.dirname(os.path.realpath(__file__))}/input/day{day_num}.txt",
            "r",
        ) as f:
            solution.puzzle_input(f)

        print(f"Day {day_num}: Part 1: {solution.part1()}")
        print(f"Day {day_num}: Part 2: {solution.part2()}")
        print("~-~-~-~-~-~-~-~-~-")
