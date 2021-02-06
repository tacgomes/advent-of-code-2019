#!/usr/bin/env python3

import sys

from itertools import product
from pyaoc.intcode import IntCodeProgram


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def paint(intcode, start_color=0):
    pos = 0j
    direction = -1j
    paiting = {pos: start_color}
    prog = IntCodeProgram(intcode)
    while not prog.halted():
        current_color = paiting.get(pos, 0)
        next_color = prog.run([current_color])
        turn = prog.run()
        paiting[pos] = next_color
        direction *= -1j if turn == 0 else 1j
        pos += direction
    return paiting


def part1(intcode):
    return len(paint(intcode))


def part2(intcode):
    painting = paint(intcode, 1)
    min_y = int(min(painting.keys(), key=lambda c: c.imag).imag)
    max_y = int(max(painting.keys(), key=lambda c: c.imag).imag)
    min_x = int(min(painting.keys(), key=lambda c: c.real).real)
    max_x = int(max(painting.keys(), key=lambda c: c.real).real)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    lines = [[' '] * width for _ in range(height)]
    for p, c in painting.items():
        if c == 1:
            lines[int(p.imag) + abs(min_y)][int(p.real) + abs(min_x)] = '#'
    lines = [''.join(line) for line in lines]
    image = '\n'.join(lines)
    return image


intcode = parse_intput(sys.argv[1])
print("Part 1:", part1(intcode[:]))
print("Part 2:", part2(intcode[:]), sep='\n')
