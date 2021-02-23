#!/usr/bin/env python3

import sys
from collections import deque
from copy import deepcopy


MOVES = ((1, 0), (0, 1), (-1, 0), (0, -1))

BORDERS = (
    tuple((0, x) for x in range(5)),
    tuple((x, 0) for x in range(5)),
    tuple((4, x) for x in range(5)),
    tuple((x, 4) for x in range(5)),
)

EMPTY = [['.' for _ in range(5)] for _ in range(5)]
EMPTY[2][2] = '?'


def parse_intput(filename):
    return list(map(list, open(filename).read().splitlines()))


def count_adjacent_bugs(m, r, c):
    count = 0
    for mr, mc in MOVES:
        rr, cc = r + mr, c + mc
        if 0 <= rr < len(m) and (
            0 <= cc < len(m[0]) and
            m[rr][cc] == '#'
        ):
            count += 1
    return count


def count_adjacent_bugs_3d(levels, i, r, c):
    level = levels[i]
    upper = levels[i - 1] if i - 1 >= 0 else None
    lower = levels[i + 1] if i + 1 < len(levels) else None
    count = 0
    for mi, (mr, mc) in enumerate(MOVES):
        rr, cc = r + mr, c + mc
        if 0 <= rr < len(level) and (
            0 <= cc < len(level[0]) and
            level[rr][cc] == '#'
        ):
            count += 1
        elif rr < 0 and upper is not None and upper[1][2] == '#':
            count += 1
        elif rr > 4 and upper is not None and upper[3][2] == '#':
            count += 1
        elif cc < 0 and upper is not None and upper[2][1] == '#':
            count += 1
        elif cc > 4 and upper is not None and upper[2][3] == '#':
            count += 1
        elif rr == 2 and cc == 2 and lower is not None:
            count += sum(
                1 for lr, lc in BORDERS[mi] if lower[lr][lc] == '#'
            )
    return count


def part1(eris):
    layouts = []

    while True:
        copy = deepcopy(eris)
        for r, row in enumerate(copy):
            for c, cell in enumerate(row):
                n = count_adjacent_bugs(copy, r, c)
                if cell == '#' and n != 1:
                    eris[r][c] = '.'
                elif cell == '.' and n in (1, 2):
                    eris[r][c] = '#'

        if eris in layouts:
            return sum(
                2 ** i
                for i, cell in enumerate(
                    [cell for row in eris for cell in row]
                )
                if cell == '#'
            )

        layouts.append(deepcopy(eris))


def part2(eris):
    eris[2][2] = '?'
    levels = deque([eris])

    for i in range(200):
        if i % 2 == 0:
            levels.appendleft(deepcopy(EMPTY))
            levels.append(deepcopy(EMPTY))

        copy = deepcopy(levels)

        for li, level in enumerate(levels):
            for r, row in enumerate(level):
                for c, cell in enumerate(row):
                    n = count_adjacent_bugs_3d(copy, li, r, c)
                    if cell == '#' and n != 1:
                        level[r][c] = '.'
                    elif cell == '.' and n in (1, 2):
                        level[r][c] = '#'

    return sum(
        1 for level in levels for r in level for x in r if x == '#'
    )


eris = parse_intput(sys.argv[1])
print("Part 1:", part1(eris))
print("Part 2:", part2(eris))
