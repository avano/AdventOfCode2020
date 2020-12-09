import os
import re

from solutions.util.aoc_util import Bag


def solve(f):
    bags = parse_bags(f.readlines())

    return part1(bags), part2(bags)


BAG_PATTERN = re.compile(r"^(\w+ \w+).*contain (.*)\.$")
INSIDE_BAGS_PATTERN = re.compile(r"^(\d+) (\w+ \w+).*$")


def parse_bags(data):
    bags = []
    for line in data:
        regex_search = re.search(BAG_PATTERN, line)
        color, inside_bags = regex_search.group(1), regex_search.group(2)

        bag = get_or_create_bag(bags, color)

        if inside_bags != "no other bags":
            current_bags = {}

            for inside_bag in inside_bags.split(", "):
                regex_search = re.search(INSIDE_BAGS_PATTERN, inside_bag)
                quantity, color = int(regex_search.group(1)), regex_search.group(2)

                current_bags[get_or_create_bag(bags, color)] = quantity

            bag.bags = current_bags

    return bags


def get_or_create_bag(bags, color):
    bag = next((bag for bag in bags if bag.color == color), None)

    if not bag:
        bag = Bag(color)
        bags.append(bag)

    return bag


def search_bag(where, what):
    if where.bags is None:
        return False
    if what in where.bags:
        return True
    else:
        for bag in where.bags:
            if search_bag(bag, what):
                return True

    return False


def count_bags(where):
    count = 0
    if where.bags is None:
        return count
    else:
        for bag, quantity in where.bags.items():
            bag_size = 1 + count_bags(bag)
            count += quantity * bag_size

        return count


def part1(bags):
    finds = 0
    shiny_gold = get_or_create_bag(bags, "shiny gold")
    for bag in bags:
        if search_bag(bag, shiny_gold):
            finds += 1

    return finds


def part2(bags):
    return count_bags(get_or_create_bag(bags, "shiny gold"))
