#!/usr/bin/env python3

import sys
import re


def part1(n):
    return sorted(str(n)) == list(str(n)) and any(
        x == y for x, y in zip(str(n), str(n)[1:])
    )


def part2(n):
    return sorted(str(n)) == list(str(n)) and any(
        len(match.group()) == 2 for match in re.finditer(r'(\d)\1+', str(n))
    )


start = int(sys.argv[1])
end = int(sys.argv[2])
numlist = list(str(start))

print("Part1: ", len(tuple(filter(part1, range(start, end)))))
print("Part2: ", len(tuple(filter(part2, range(start, end)))))
