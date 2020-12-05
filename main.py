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
                "{}/{}".format(
                    os.path.dirname(os.path.realpath(__file__)), "solutions"
                ),
                "*.py",
            )
        )
        days = []
        for i in range(file_count):
            days.append(str(i + 1).zfill(2))
    for day in days:
        solution = importlib.import_module("solutions.day{}".format(day))
        print(f"Day {day}: Part 1: {solution.part1()}")
        print(f"Day {day}: Part 2: {solution.part2()}")
