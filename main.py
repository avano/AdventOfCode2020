import glob
import importlib

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        days = sys.argv[1:]
    else:
        for f in sorted(
            glob.glob1(
                f"{os.path.dirname(os.path.realpath(__file__))}/solutions", "*.py"
            )
        ):
            day = f.split(".")[0]
            solution = importlib.import_module(f"solutions.{day}")

            with open(
                f"{os.path.dirname(os.path.realpath(__file__))}/input/{day}.txt",
                "r",
            ) as f:
                part1, part2 = solution.solve(f)

            print(f"{day}: part 1: {part1}")
            print(f"{day}: part 2: {part2}")
            print("~-~-~-~-~-~-~-~-~-")
