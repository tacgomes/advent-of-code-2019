#!/usr/bin/env python3

import sys

from itertools import product
from pyaoc.intcode import IntCodeProgram


def parse_input(filename):
    return list(map(int, open(filename).read().split(",")))


def part1(intcode):
    intcode[1] = 12
    intcode[2] = 2
    prog = IntCodeProgram(intcode)
    prog.run()
    return prog[0]


def part2(intcode):
    for (noun, verb) in product(range(100), range(100)):
        prog = IntCodeProgram(intcode)
        prog[1], prog[2] = noun, verb
        prog.run()
        if prog[0] == 19690720:
            return 100 * noun + verb

    return None


intcode = parse_input(sys.argv[1])
print("Part 1:", part1(intcode))
print("Part 2:", part2(intcode))
