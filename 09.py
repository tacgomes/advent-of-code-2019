#!/usr/bin/env python3

import sys

from itertools import product
from pyaoc.intcode import IntCodeProgram

def parse_intput(filename):
    return list(map(int, open(filename).read().split(",")))


def part1(intcode):
    prog = IntCodeProgram(intcode, [1])
    return prog.run()


def part2(intcode):
    prog = IntCodeProgram(intcode, [2])
    return prog.run()


intcode = parse_intput(sys.argv[1])
print("Part 1:", part1(intcode))
print("Part 2:", part2(intcode))
