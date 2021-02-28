#!/usr/bin/env python3

import sys

from itertools import product
from pyaoc.intcode import IntCodeProgram


SQUARE_SIZE = 100


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def find_beam_start(intcode):
    return next(
        filter(
            lambda p: IntCodeProgram(intcode[:]).run([p[0], p[1]]) == 1,
            ((x, y) for (x, y) in product(range(1, 10), range(10)))
        )
    )


def part1(intcode):
    return sum(
        map(
            lambda p: IntCodeProgram(intcode[:]).run([p[0], p[1]]),
            ((x, y) for (x, y) in product(range(50), range(50)))
        )
    )


def part2(intcode):
    start = find_beam_start(intcode)
    beam, (pos_x, pos_y) = set(), start

    # TODO: use a binary search algorithm to find where square fits.
    while True:
        x, pos_x = pos_x - 1, None
        while True:
            if IntCodeProgram(intcode).run([x, pos_y]) == 1:
                beam.add((x, pos_y))
                if pos_x is None:
                    pos_x = x
            elif pos_x is not None:
                break
            x += 1

        if pos_y >= SQUARE_SIZE:
            for (x, y) in filter(
                lambda p: p[1] == pos_y - SQUARE_SIZE + 1, beam
            ):
                tr = (x + SQUARE_SIZE - 1, y)
                bl = (x, pos_y)
                br = (x + SQUARE_SIZE - 1, pos_y)
                if tr in beam and bl in beam and br in beam:
                    return x * 10000 + y

        pos_y += 1


intcode = parse_intput(sys.argv[1])
print("Part 1:", part1(intcode))
print("Part 2:", part2(intcode))
