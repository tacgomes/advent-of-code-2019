#!/usr/bin/env python3

import sys

from pyaoc.intcode import IntCodeProgram


def parse_input(filename):
    return list(map(int, open(filename).read().split(",")))


intcode = parse_input(sys.argv[1])
print("Part 1:", IntCodeProgram(intcode, [1]).run_until_halt())
print("Part 2:", IntCodeProgram(intcode, [5]).run_until_halt())
