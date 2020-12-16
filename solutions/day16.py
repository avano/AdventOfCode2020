import re


def solve(f):
    data = [line.strip() for line in f.readlines()]

    return part1(data), part2(data)


RULES_REGEX = re.compile(r".* (\d+-\d+) or (\d+-\d+)$")


def load_rules(data):
    rules = []
    for index, line in enumerate(data):
        if not line:
            break
        search = re.search(RULES_REGEX, line)
        low_min, low_max = search.group(1).split("-")
        high_min, high_max = search.group(2).split("-")
        rules.append((int(low_min), int(low_max), int(high_min), int(high_max)))
    return index, rules


def is_field_valid(f, rule):
    return f in range(rule[0], rule[1] + 1) or f in range(rule[2], rule[3] + 1)


def get_invalid_values(rules, ticket):
    result = 0
    for f in ticket:
        found = False
        for rule in rules:
            if is_field_valid(f, rule):
                found = True
                break
        if not found:
            result += f
    return result


def part1(data):
    index, rules = load_rules(data)
    result = 0
    for line in data[index + 5 :]:
        result += get_invalid_values(rules, [int(f) for f in line.split(",")])
    return result


def part2(data):
    index, rules = load_rules(data)
    ticket = [int(field) for field in data[index + 2].split(",")]
    valid_tickets = []

    for line in data[index + 5 :]:
        line = [int(f) for f in line.split(",")]
        if get_invalid_values(rules, line) == 0:
            valid_tickets.append(line)

    possible_rule_fields = []
    for rule in rules:
        possible_rule_fields.append(
            [
                field_index
                for field_index in range(len(ticket))
                if all(is_field_valid(valid_ticket[field_index], rule) for valid_ticket in valid_tickets)
            ]
        )

    resolved_fields = set()
    fields_lengths = {
        len(possible_fields): rule_index for rule_index, possible_fields in enumerate(possible_rule_fields)
    }

    rule_ticket_field = [-1] * (len(rules))
    for size in sorted(fields_lengths):
        remaining = [el for el in possible_rule_fields[fields_lengths[size]] if el not in resolved_fields]
        resolved_fields.add(remaining[0])
        rule_ticket_field[fields_lengths[size]] = remaining[0]

    result = 1
    for i in range(6):
        result *= int(ticket[rule_ticket_field[i]])
    return result
