#!/usr/bin/env python3

import sys

from pyaoc.intcode import IntCodeProgram


DIR = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3,
}

MOVES = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}

CANCEL = {
    0: 2,
    1: 3,
    2: 0,
    3: 1,
}

TURN = {
    (0, 1): 'R',
    (1, 2): 'R',
    (2, 3): 'R',
    (3, 0): 'R',
    (0, 3): 'L',
    (3, 2): 'L',
    (2, 1): 'L',
    (1, 0): 'L',
}


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def prepare_function(f):
    return list(','.join(map(str, f)) + '\n')


def create_map(intcode):
    map_drawing = []
    prog = IntCodeProgram(intcode)
    while not prog.halted():
        char = chr(prog.run())
        map_drawing.append(char)
    map_drawing = ''.join(map_drawing).strip()
    m = [list(r) for r in map_drawing.splitlines()]
    return m, map_drawing


def advance(pos, d, m):
    for i in range(4):
        if (d + i) % 4 == CANCEL[d]:
            continue

        move = MOVES[(d + i) % 4]
        next_pos = pos[0] + move[0], pos[1] + move[1]

        if next_pos[0] < 0 or next_pos[0] >= len(m[0]) or (
                next_pos[1] < 0 or next_pos[1] >= len(m)):
            continue

        if m[next_pos[1]][next_pos[0]] == '#':
            return next_pos, (d + i) % 4

    return None, None


def walk(m):
    pos = next(
        (x, y)
        for y in range(len(m))
        for x in range(len(m[0]))
        if m[y][x] in '^>v<'
    )

    d = m[pos[1]][pos[0]]
    d = DIR[d]

    path = []
    advanced = 0
    intersections = []
    visited = set()
    turn = None

    while pos is not None:
        pos, next_d = advance(pos, d, m)
        if pos in visited:
            intersections.append((pos))
        visited.add(pos)

        advanced += 1
        if d != next_d:
            if turn is not None:
                path.extend([turn, advanced])
            if next_d is not None:
                turn = TURN[(d, next_d)]
            advanced = 0

        d = next_d

    return intersections, path


def find_main_routine(fa, fb, fc, path):
    main = []
    while path:
        if path[:len(fa)] == fa:
            main.append('A')
            path = path[len(fa):]
        elif path[:len(fb)] == fb:
            main.append('B')
            path = path[len(fb):]
        elif path[:len(fc)] == fc:
            main.append('C')
            path = path[len(fc):]
        else:
            return None

    return main


def find_functions(path):
    for la in range(2, 11):
        fa = path[:la]

        sb = la
        while path[sb:sb + la] == fa:
            sb += la

        for lb in range(2, 11):
            fb = path[sb:sb + lb]

            sc = sb + lb
            while True:
                if path[sc:sc + la] == fa:
                    sc += la
                elif path[sc:sc + lb] == fb:
                    sc += lb
                else:
                    break

            for lc in range(2, 11):
                fc = path[sc:sc + lc]

                main = find_main_routine(fa, fb, fc, path)
                if main is not None and len(main) < 11:
                    return main, fa, fb, fc


def part1(intersections):
    return sum(map(lambda p: p[0] * p[1], intersections))


def part2(intcode, path):
    main, fa, fb, fc = find_functions(path)
    main = prepare_function(main)
    fa = prepare_function(fa)
    fb = prepare_function(fb)
    fc = prepare_function(fc)

    input_ = main + fa + fb + fc + ['n', '\n']
    input_ = list(map(ord, input_))

    intcode[0] = 2
    prog = IntCodeProgram(intcode, input_)
    return prog.run_until_halt()


intcode = parse_intput(sys.argv[1])
m, map_drawing = create_map(intcode)
intersections, path = walk(m)
print(map_drawing)
print("Path:", path)
print("Part 1:", part1(intersections))
print("Part 2:", part2(intcode, path))
