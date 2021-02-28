#!/usr/bin/env python3

import sys

from itertools import permutations
from pyaoc.intcode import IntCodeProgram


def parse_input(filename):
    return list(map(int, open(filename).read().split(",")))


def part1(intcode):
    highest = 0
    for phases in permutations(range(0, 5)):
        signal = 0
        for amp in range(0, 5):
            program = IntCodeProgram(intcode)
            signal = program.run([phases[amp], signal])
        highest = max(highest, signal)
    return highest


def part2(intcode):
    highest = 0
    for phases in permutations(range(5, 10)):
        signal = 0
        programs = [IntCodeProgram(intcode, [p]) for p in phases]
        for amp in map(lambda x: x % 5, range(0, sys.maxsize)):
            signal = programs[amp].run([signal])
            if amp == 4 and programs[amp].halted():
                break
        highest = max(highest, signal)
    return highest


intcode = parse_input(sys.argv[1])
print("Part 1:", part1(intcode))
print("Part 2:", part2(intcode))
