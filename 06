#!/usr/bin/env python3

import sys


def parse_input(filename):
    lines = open(filename).read().splitlines()
    return {y: x for x, y in map(lambda x: x.split(")"), lines)}


def depth(orbits, obj):
    count = 0
    parent = obj
    while parent != "COM":
        parent = orbits[parent]
        count += 1
    return count


def part1(orbits):
    return sum(map(lambda x: depth(orbits, x), orbits.keys()))


def part2(orbits):
    # Assume that the graph is acyclic and therefore we only need to
    # calculate the distance until YOU and SAN intersect. Otherwise, we
    # would have to use a shortest path algorithm such as the Dijkstra's
    # algorithm.
    obj = orbits["YOU"]
    count = 0
    distances = {}
    while obj != "COM":
        distances[obj] = count
        obj = orbits[obj]
        count += 1

    obj = orbits["SAN"]
    count = 0
    while obj != "COM":
        if obj in distances:
            return distances[obj] + count
        obj = orbits[obj]
        count += 1

    return None


orbits = parse_input(sys.argv[1])
print("Part 1:", part1(orbits))
print("Part 1:", part2(orbits))
