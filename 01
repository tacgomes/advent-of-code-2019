#!/usr/bin/env python3

import sys


def parse_input(filename):
    return list(map(int, open(filename).readlines()))


def calculate_mass_fuel(mass):
    return mass // 3 - 2


def calculate_total_fuel(mass):
    fuel = total = calculate_mass_fuel(mass)
    while (fuel := calculate_mass_fuel(fuel)) > 0:
        total += fuel
    return total


def part1(masses):
    return sum(map(calculate_mass_fuel, masses))


def part2(masses):
    return sum(map(calculate_total_fuel, masses))


masses = parse_input(sys.argv[1])
print("Part 1:", part1(masses))
print("Part 2:", part2(masses))
