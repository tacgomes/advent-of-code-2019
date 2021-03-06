#!/usr/bin/env python3

import sys

from collections import deque
from pyaoc.intcode import IntCodeProgram


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def input_func_wrapper(rcvq):
    return lambda: rcvq.popleft() if rcvq else -1


def solve(intcode):
    progs, rcvqs = [], []
    last_nat_y, first_nat_y = None, None

    for addr in range(50):
        rcvq = deque([addr])
        prog = IntCodeProgram(
            intcode,
            input_func=input_func_wrapper(rcvq)
        )
        rcvqs.append(rcvq)
        progs.append(prog)

    while True:
        idle = all(len(rcvq) == 0 for rcvq in rcvqs)

        for prog in progs:
            dst_addr = prog.run(pause_on_input=True)
            if dst_addr is None:
                continue

            x, y = prog.run(), prog.run()
            assert x is not None
            assert y is not None

            if dst_addr == 255:
                first_nat_y = y if first_nat_y is None else first_nat_y
                still_idle = all(len(rcvq) == 0 for rcvq in rcvqs)
                if idle and still_idle:
                    if last_nat_y == y:
                        return first_nat_y, y
                    rcvqs[0].extend([x, y])
                    last_nat_y = y
            else:
                rcvqs[dst_addr].extend([x, y])


intcode = parse_intput(sys.argv[1])
part1, part2 = solve(intcode)
print("Part 1:", part1)
print("Part 2:", part2)
