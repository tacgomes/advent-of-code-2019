#!/usr/bin/env python3

import sys

from itertools import combinations
from pyaoc.intcode import IntCodeProgram


#                                                   HALLWAY ———— WARP DRIVE
#                                                      |
#                                                      |
#                                                 HULL BREACH
#                 OBSERVATORY ——— STABLES              |
#                                    |                 |
#                                    |                 |
#  SECURITY CHECKPOINT —————————— KITCHEN ——————— SCIENCE LAB ————— SICK BAY
#                                                      |
#                                                      |
#                  ARCADE                              |
#                    |                                 |
#                    |                                 |
# NAVIGATION ——— ENGINEERING                           |
#                    |                                 |
#                    |                                 |
# HOT CHOC —————— STORAGE ———————————————————————— GIFT WRAPPING
#                                                      |
#                                                      |
#              HOLODECK —————————————————————————— PASSAGES
#                                                      |
#                                                      |
#                                                CREW QUARTERS

INSTRUCTIONS = '''\
south
take space law space brochure
south
take mouse
south
take astrolabe
south
take mug
north
north
west
north
north
take wreath
south
south
east
north
west
take sand
north
take manifold
south
west
take monolith
west
'''

ITEMS = (
    'space law space brochure',
    'mouse',
    'astrolabe',
    'mug',
    'wreath',
    'sand',
    'manifold',
    'monolith',
)


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def solve(intcode):
    instructions = list(INSTRUCTIONS)

    for i in range(len(ITEMS) + 1):
        for combination in combinations(ITEMS, i):
            for item in ITEMS:
                instructions += f'drop {item}\n'
            for item in combination:
                instructions += f'take {item}\n'
            instructions += 'west\n'

    instructions = list(map(ord, instructions))
    prog = IntCodeProgram(intcode, instructions)

    while not prog.halted():
        out = prog.run()
        print(chr(out), end='')


intcode = parse_intput(sys.argv[1])
solve(intcode)
