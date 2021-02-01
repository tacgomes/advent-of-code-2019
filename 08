#!/usr/bin/env python3

import sys

from collections import Counter

HEIGHT = 6
WIDTH = 25
LAYER_SIZE = HEIGHT * WIDTH


def parse_input(filename):
    return list(open(filename).read().rstrip())


def decode(image):
    decoded = [None] * LAYER_SIZE
    for i in range(LAYER_SIZE):
        offset = 0
        while image[offset + i] == '2':
            offset += LAYER_SIZE
        decoded[i] = image[offset + i]
    return decoded


def image2string(image):
    res = [''.join(image[i:i + WIDTH]) for i in range(0, LAYER_SIZE, WIDTH)]
    res = '\n'.join(res)
    res = res.replace('0', ' ')
    res = res.replace('1', '#')
    return res


def part1(image):
    counters = [
        Counter(image[i:i + LAYER_SIZE])
        for i in range(0, len(image), LAYER_SIZE)
    ]
    counter0 = min(counters, key=lambda c: c['0'])
    return counter0['1'] * counter0['2']


def part2(image):
    return image2string(decode(image))


image = parse_input(sys.argv[1])
print("Part 1:", part1(image))
print("Part 2:", part2(image), sep='\n')
