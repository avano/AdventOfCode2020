import math
import sys


def solve(f):
    data = f.read().strip().split("\n")
    timestamp = int(data[0])
    buses = [int(bus) if bus.isnumeric() else bus for bus in data[1].split(",")]

    return part1(timestamp, buses), part2(buses)


def part1(timestamp, buses):
    shortest_wait_time = sys.maxsize
    bus_id = -1
    for bus in filter(lambda b: isinstance(b, int), buses):
        wait_time = bus * (timestamp // bus) + bus - timestamp
        if wait_time < shortest_wait_time:
            shortest_wait_time = wait_time
            bus_id = bus
    return bus_id * shortest_wait_time


def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclid(b % a, a)

    x = int(y1 - (b // a) * x1)
    y = int(x1)

    return gcd, x, y


def part2(buses):
    lcm = math.lcm(*filter(lambda x: isinstance(x, int), buses))

    result = 0
    for index, bus in enumerate(buses):
        if isinstance(bus, int):
            result += (-index % bus) * int(lcm / bus) * extended_euclid(lcm / bus, bus)[1]
    return result % lcm
