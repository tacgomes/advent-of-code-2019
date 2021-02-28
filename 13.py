#!/usr/bin/env python3

import sys

from enum import IntEnum
from pyaoc.intcode import IntCodeProgram


class Tile(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def part1(intcode):
    blocks = set()
    prog = IntCodeProgram(intcode)
    while not prog.halted():
        x, y, t = prog.run(), prog.run(), prog.run()
        if t == Tile.BLOCK:
            blocks.add((x, y))
    return len(blocks)


def part2(intcode):
    intcode[0] = 2
    prog = IntCodeProgram(intcode)
    input_, paddle = [], None
    while not prog.halted():
        x, y, t = prog.run(input_), prog.run(), prog.run()
        input_ = []
        if (x, y) == (-1, 0):
            score = t
        elif t == Tile.PADDLE:
            paddle = x
        elif t == Tile.BALL:
            input_ = [0]
            if paddle is not None and paddle < x:
                input_ = [1]
            elif paddle is not None and paddle > x:
                input_ = [-1]
    return score


intcode = parse_intput(sys.argv[1])
print("Part 1:", part1(intcode[:]))
print("Part 2:", part2(intcode[:]))
