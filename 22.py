#!/usr/bin/env python3

import sys

OP_NS = 'deal into new stack'
OP_CUT = 'cut '
OP_INC = 'deal with increment '


def parse_intput(filename):
    return open(filename).read().splitlines()


def part1(operations):
    pos, dlen = 2019, 10007

    for op in operations:
        if op == OP_NS:
            pos = dlen - pos - 1
        elif op.startswith(OP_CUT):
            n = int(op[len(OP_CUT):])
            if n < 0:
                n += dlen
            if pos < n:
                pos += dlen - n
            else:
                pos -= n
        elif op.startswith(OP_INC):
            n = int(op[len(OP_INC):])
            pos = (pos * n) % dlen

    return pos


operations = parse_intput(sys.argv[1])
print("Part 1:", part1(operations))
