#!/usr/bin/env python3

import sys

from pyaoc.intcode import IntCodeProgram


springcode_part1 = '''\
NOT A J
NOT C T
AND D T
OR T J
WALK
'''

springcode_part2 = '''\
NOT A J
NOT C T
AND D T
AND H T
OR T J
NOT B T
AND D T
AND H T
OR T J
RUN
'''


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def solve(intcode, springcode):
    springcode = list(map(ord, springcode))
    springdroid_movement = []
    prog = IntCodeProgram(intcode, springcode)

    while not prog.halted():
        out = prog.run()
        if out < 128:
            springdroid_movement.append(out)
        else:
            return out

    print(''.join(map(chr, springdroid_movement)))

    return None


intcode = parse_intput(sys.argv[1])
print("Part 1:", solve(intcode, springcode_part1))
print("Part 2:", solve(intcode, springcode_part2))
