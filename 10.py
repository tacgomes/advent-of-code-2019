#!/usr/bin/env python3

import sys

from itertools import product


def parse_intput(filename):
    return open(filename).read().splitlines()


def slope(y, x):
    return y / x if x != 0 else float('inf')


def unique(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]


def get_asteroids(m):
    yield from [
        (r, c)
        for (r, row) in enumerate(m)
        for (c, col) in enumerate(row)
        if col == '#'
    ]


def get_moves(nrows, ncols):
    # TODO: instead of deriving all possible moves, for each asteroid
    # calculate the moves necessary to reach the other asteroids.
    #
    # TODO: sort the moves using some trigonometric function such as
    # atan2.
    moves = list(product(range(1, nrows), range(1, ncols)))
    moves.extend([(1, 0), (0, 1)])
    moves = {slope(y, x): (y, x) for y, x in moves[::-1]}
    moves = moves.values()
    moves = sorted(moves, key=lambda p: slope(p[0], p[1]))[::-1]
    moves = (
        [(-y, x) for y, x in moves]
        + moves[::-1]
        + [(y, -x) for y, x in moves]
        + [(-y, -x) for y, x in moves][::-1]
    )
    return unique(moves)


def count_blocked(m, r, c, move):
    r, c = r + move[0], c + move[1]
    if r < 0 or c < 0 or r >= len(m) or c >= len(m[0]):
        return 0
    count = 1 if m[r][c] == '#' else 0
    return count + count_blocked(m, r, c, move)


def vaporize(m, r, c, move, vaporized):
    r, c = r + move[0], c + move[1]
    if r < 0 or c < 0 or r >= len(m) or c >= len(m[0]):
        return None
    if m[r][c] == '#' and (r, c) not in vaporized:
        return (r, c)
    return vaporize(m, r, c, move, vaporized)


def part1(m):
    asteroids = list(get_asteroids(m))
    station, min_blocked = None, sys.maxsize
    moves = get_moves(len(m), len(m[0]))
    for r, c in asteroids:
        counts = [count_blocked(m, r, c, move) - 1 for move in moves]
        num_blocked = sum(filter(lambda x: x > 0, counts))
        if num_blocked < min_blocked:
            station = r, c
            min_blocked = num_blocked
    return station, len(asteroids) - min_blocked - 1


def part2(m, station):
    vaporized = []
    moves = get_moves(len(m), len(m[0]))
    while len(vaporized) < 200:
        for move in moves:
            if vap := vaporize(m, station[0], station[1], move, vaporized):
                vaporized.append(vap)
    return vaporized[199][1] * 100 + vaporized[199][0]


m = parse_intput(sys.argv[1])
station, num_detected = part1(m)
print("Part 1:", num_detected)
print("Part 2:", part2(m, station))
