#!/usr/bin/env python3

import sys
import re

from collections import Counter


def parse_intput(filename):
    lines = open(filename).read().splitlines()
    reactions = {}
    for line in lines:
        match = re.finditer(r'(\d+) (\w+)', line)
        reaction = [(int(m.group(1)), m.group(2)) for m in match]
        output = reaction[-1]
        reactions[output[1]] = (int(output[0]), reaction[:-1])

    return reactions


def round_to_nearest(n, m):
    return n if n % m == 0 else n + m - (n % m)


def part1(reactions, fuel_amount=1):
    dependencies = {'FUEL': []}
    for chemical, data in reactions.items():
        for _, input_ in data[1]:
            dependencies.setdefault(input_, []).append(chemical)
    del dependencies['ORE']

    counter = Counter()
    while dependencies:
        candidate = next(
            c for c, deps in dependencies.items() if len(deps) == 0
        )
        required = counter[candidate] if candidate != 'FUEL' else fuel_amount
        created, inputs = reactions[candidate]
        multiplier = (
            1
            if required < created
            else round_to_nearest(required, created) // created
        )

        for amount, input_ in inputs:
            counter[input_] += amount * multiplier

        for k, v in dependencies.items():
            dependencies[k] = list(filter(lambda x: x != candidate, v))
        del dependencies[candidate]

    return counter['ORE']


def part2(reactions):
    max_ore = 10**12

    upper_bound = 2
    while part1(reactions, upper_bound) < max_ore:
        upper_bound *= 2

    lower_bound = upper_bound // 2

    while lower_bound + 1 < upper_bound:
        middle = (lower_bound + upper_bound) // 2
        ore = part1(reactions, middle)
        if ore > max_ore:
            upper_bound = middle
        else:
            lower_bound = middle

    return lower_bound


reactions = parse_intput(sys.argv[1])
print("Part 1:", part1(reactions))
print("Part 2:", part2(reactions))
