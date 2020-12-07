import os
import re

from util.aoc_util import Bag

with open(
    f"{os.path.dirname(os.path.realpath(__file__))}/input/{os.path.basename(__file__).replace('.py', '.txt')}",
    "r",
) as f:
    input_list = f.readlines()

regex_bag = re.compile(r"^(\w+ \w+).*contain (.*)\.$")
regex_inside_bags = re.compile(r"^(\d+) (\w+ \w+).*$")


def parse_bags():
    bags = []
    for line in input_list:
        regex_search = re.search(regex_bag, line)
        color, inside_bags = regex_search.group(1), regex_search.group(2)
        bag = get_bag(bags, color)
        if inside_bags != "no other bags":
            current_bags = {}
            for inside_bag in inside_bags.split(", "):
                regex_search = re.search(regex_inside_bags, inside_bag)
                quantity, color = regex_search.group(1), regex_search.group(2)
                current_bags[get_bag(bags, color)] = quantity
            bag.bags = current_bags
    return bags


def get_bag(bags, color):
    for bag in bags:
        if bag.color == color:
            return bag
    new_bag = Bag(color)
    bags.append(new_bag)
    return new_bag


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
            count += int(quantity) * bag_size
        return count


def part1():
    bags = parse_bags()
    finds = 0
    shiny_gold = get_bag(bags, "shiny gold")
    for bag in bags:
        if search_bag(bag, shiny_gold):
            finds += 1

    return finds


def part2():
    return count_bags(get_bag(parse_bags(), "shiny gold"))
