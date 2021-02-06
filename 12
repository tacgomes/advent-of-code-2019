#!/usr/bin/env python3

import sys
import re
import copy
import math

from itertools import combinations, count


def parse_intput(filename):
    lines = open(filename).read().splitlines()
    positions = []
    for line in lines:
        m = re.match(r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)', line)
        x, y, z = m.groups()
        positions.append([int(x), int(y), int(z)])
    return positions


def apply_gravity(positions, velocities):
    for a, b in combinations(range(len(positions)), 2):
        for c in (0, 1, 2):
            if positions[a][c] > positions[b][c]:
                velocities[a][c] -= 1
                velocities[b][c] += 1
            elif positions[a][c] < positions[b][c]:
                velocities[a][c] += 1
                velocities[b][c] -= 1


def apply_velocity(positions, velocities):
    for i in range(len(positions)):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]
        positions[i][2] += velocities[i][2]


def calculate_energy(position, velocity):
    pot = sum(map(abs, position))
    kin = sum(map(abs, velocity))
    return pot * kin


def part1(positions):
    velocities = [[0, 0, 0] for i in range(4)]
    for _ in range(1000):
        apply_gravity(positions, velocities)
        apply_velocity(positions, velocities)
    return sum(
        calculate_energy(p, v)
        for p, v in zip(positions, velocities)
    )


def part2(positions):
    periods = []
    for d in (0, 1, 2):
        initials = tuple(positions[i][d] for i in range(4))
        p = copy.deepcopy(positions)
        v = [[0, 0, 0] for i in range(4)]
        for period in count(1):
            apply_gravity(p, v)
            apply_velocity(p, v)
            if (all(p[i][d] == initials[i] for i in range(4)) and
                    all(v[i][d] == 0 for i in range(4))):
                periods.append(period)
                break
    return math.lcm(*periods)


positions = parse_intput(sys.argv[1])
print("Part 1:", part1(copy.deepcopy(positions)))
print("Part 2:", part2(copy.deepcopy(positions)))
