#!/usr/bin/env python3

import sys

from enum import IntEnum
from itertools import permutations


class Op(IntEnum):
    ADD = 1
    MUL = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_TRUE = 5
    JUMP_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE = 9
    HALT = 99


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def decode(instr):
    return (
        instr % 100,
        instr // 100 % 10,
        instr // 1000 % 10,
        instr // 10000 % 10,
    )


class IntCodeProgram:
    def __init__(self, prog, inputs=[]):
        self.prog = dict(enumerate(prog))
        self.ip = 0
        self.base = 0
        self.inputs = inputs
        self.output = None

    def run(self, extra_inputs=[]):
        self.inputs.extend(extra_inputs)

        while True:
            ip = self.ip
            op, m1, m2, m3 = decode(self[ip])
            p1 = self._param(ip + 1, m1)
            p2 = self._param(ip + 2, m2)
            p3 = self._param(ip + 3, m3)

            if op == Op.ADD:
                self[p3] = self[p1] + self[p2]
                ip += 4
            elif op == Op.MUL:
                self[p3] = self[p1] * self[p2]
                ip += 4
            elif op == Op.INPUT:
                self[p1] = self.inputs.pop(0)
                ip += 2
            elif op == Op.OUTPUT:
                self.output = self[p1]
                self.ip += 2
                return self.output
            elif op == Op.JUMP_TRUE:
                ip = self[p2] if self[p1] != 0 else ip + 3
            elif op == Op.JUMP_FALSE:
                ip = self[p2] if self[p1] == 0 else ip + 3
            elif op == Op.LESS_THAN:
                self[p3] = 1 if self[p1] < self[p2] else 0
                ip += 4
            elif op == Op.EQUALS:
                self[p3] = 1 if self[p1] == self[p2] else 0
                ip += 4
            elif op == Op.RELATIVE_BASE:
                self.base += self[p1]
                ip += 2
            elif op == Op.HALT:
                break

            self.ip = ip

        return self.output

    def __getitem__(self, key):
        return self.prog.get(key, 0)

    def __setitem__(self, key, val):
        self.prog[key] = val

    def run_until_halt(self):
        while not self.halted():
            self.run()
        return self.output

    def halted(self):
        op = decode(self[self.ip])[0]
        return op == Op.HALT

    def _param(self, addr, mode):
        if mode == Mode.POSITION:
            return self[addr]
        elif mode == Mode.IMMEDIATE:
            return addr
        elif mode == Mode.RELATIVE:
            return self.base + self[addr]
