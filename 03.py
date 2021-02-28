#!/usr/bin/env python3

import sys


deltas = {
    "U": (0, 1),
    "R": (1, 0),
    "D": (0, -1),
    "L": (-1, 0),
}


def parse_move(s):
    return s[0], int(s[1:])


def parse_input(filename):
    lines = open(filename).readlines()
    wire1 = tuple(map(parse_move, lines[0].strip().split(",")))
    wire2 = tuple(map(parse_move, lines[1].strip().split(",")))
    return wire1, wire2


def get_points(wire):
    (x, y) = (0, 0)
    points = set()

    for direction, value in wire:
        d = deltas[direction]
        for _ in range(value):
            (x, y) = (x + d[0], y + d[1])
            points.add((x, y))

    return points


def get_intersections(wire1, wire2):
    points1 = get_points(wire1)
    points2 = get_points(wire2)
    return points1 & points2


def get_steps(wire):
    (x, y) = (0, 0)
    step = 0
    steps = {}

    for direction, value in wire:
        d = deltas[direction]
        for _ in range(value):
            (x, y, step) = (x + d[0], y + d[1], step + 1)
            if (x, y) not in steps:
                steps[(x, y)] = step

    return steps


def part1(intersects):
    return min(abs(x) + abs(y) for (x, y) in intersects)


def part2(wire1, wire2, intersections):
    steps1 = get_steps(wire1)
    steps2 = get_steps(wire2)
    return min(steps1[k] + steps2[k] for k in intersections)


wire1, wire2 = parse_input(sys.argv[1])
intersects = get_intersections(wire1, wire2)
print("Part 1:", part1(intersects))
print("Part 2:", part2(wire1, wire2, intersects))
