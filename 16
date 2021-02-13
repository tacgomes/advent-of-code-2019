#!/usr/bin/env python3

import sys


PATTERN = [0, 1, 0, -1]


def parse_intput(filename):
    return list(map(int, open(filename).read().strip()))


def flatten(lst):
    return [item for subl in lst for item in subl]


def part1(signal, num_phases=100):
    for _ in range(num_phases):
        new_signal = []
        for i, n in enumerate(signal):
            pattern = flatten(map(lambda x: [x] * (i + 1), PATTERN))
            total = sum(
                m * pattern[(j + 1) % len(pattern)]
                for j, m in enumerate(signal)
            )
            new_signal.append(abs(total) % 10)
        signal = new_signal

    return ''.join(map(str, signal[:8]))


def part2(signal):
    skip = int(''.join(map(str, signal[:7])))
    assert(skip >= len(signal) * 10_000 // 2)

    signal = signal * 10_000
    signal = signal[skip:]

    for _ in range(100):
        cumsum = 0
        for i in reversed(range(len(signal))):
            cumsum += signal[i]
            signal[i] = abs(cumsum) % 10

    return ''.join(map(str, signal[:8]))


signal = parse_intput(sys.argv[1])
print("Part 1:", part1(signal[:]))
print("Part 2:", part2(signal[:]))
