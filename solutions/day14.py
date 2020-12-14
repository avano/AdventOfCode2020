import re


def solve(f):
    data = f.readlines()
    return part1(data), part2(data)


MEMORY_REGEX = re.compile(r"^mem\[(\d+)] = (\d+)$")


def create_masks(mask):
    mask_ones = ""
    mask_zeroes = ""
    for char in mask:
        mask_ones += "0" if char == "X" else char
        mask_zeroes += "1" if char == "X" else char
    return int(mask_ones, 2), int(mask_zeroes, 2)


def permute_floating_bit(address):
    suffix_permutations = []
    suffix = ""
    for index in range(len(address) - 1, -1, -1):
        if address[index] != "X":
            suffix += address[index]
        else:
            if suffix_permutations:
                new_suffixes = []
                for permutation in suffix_permutations:
                    new_suffixes.append(permutation + suffix + "0")
                    new_suffixes.append(permutation + suffix + "1")
                suffix_permutations = new_suffixes
            else:
                suffix_permutations.append(suffix + "0")
                suffix_permutations.append(suffix + "1")
            suffix = ""
    for s in suffix_permutations:
        yield int(suffix[::-1] + s[::-1], 2)


def get_addresses(address, mask):
    binary_padded_string = format(address, "036b")
    result = ""
    for i in range(len(binary_padded_string)):
        if mask[i] == "0":
            result += binary_padded_string[i]
        else:
            result += mask[i]
    return permute_floating_bit(result)


def part1(data):
    mask_ones = 0
    mask_zeroes = 0
    memory = {}
    for line in data:
        if line.startswith("mask"):
            mask_ones, mask_zeroes = create_masks(line.split(" = ")[1].strip())
        else:
            search = re.search(MEMORY_REGEX, line)
            memory[search.group(1)] = (int(search.group(2)) | mask_ones) & mask_zeroes
    return sum(memory.values())


def part2(data):
    mask = ""
    memory = {}
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1].strip()
        else:
            search = re.search(MEMORY_REGEX, line)
            address, value = int(search.group(1)), int(search.group(2))
            for addr in get_addresses(address, mask):
                memory[addr] = value
    return sum(memory.values())
