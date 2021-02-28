#!/usr/bin/env python3

import sys

from collections import deque
from pyaoc.intcode import IntCodeProgram
from pyaoc.map_drawer import draw


MOVES = {
    1: (0, -1),
    2: (0, 1),
    3: (-1, 0),
    4: (1, 0),
}

CANCEL = {
    1: 2,
    2: 1,
    3: 4,
    4: 3,
}


def parse_intput(filename):
    return list(map(int, open(filename).read().split(',')))


def part1(maze):
    visited = set()
    queue = deque([(0, (0, 0))])

    while queue:
        dist, pos = queue.popleft()
        visited.add(pos)

        if maze[pos] == 'O':
            return dist

        for m in MOVES.values():
            newpos = pos[0] + m[0], pos[1] + m[1]
            if newpos not in visited and maze.get(newpos) != '#':
                queue.append((dist + 1, newpos))

    return None


def part2(maze):
    oxygen = next(filter(lambda x: x[1] == 'O', maze.items()))[0]
    visited = set()
    queue = deque([(0, oxygen)])

    while queue:
        dist, pos = queue.popleft()
        visited.add(pos)
        for m in MOVES.values():
            newpos = pos[0] + m[0], pos[1] + m[1]
            if newpos not in visited and maze.get(newpos) != '#':
                queue.append((dist + 1, newpos))

    return dist


def explore(pos, prog, maze):
    if pos in maze:
        return

    maze[pos] = ' '

    for d, m in MOVES.items():
        status = prog.run([d])
        nextpos = pos[0] + m[0], pos[1] + m[1]
        if status == 0:
            maze[nextpos] = '#'
        elif status == 1:
            explore(nextpos, prog, maze)
            prog.run([CANCEL[d]])
            maze[nextpos] = '.'
        elif status == 2:
            explore(nextpos, prog, maze)
            prog.run([CANCEL[d]])
            maze[nextpos] = 'O'


def create_maze(intcode):
    prog = IntCodeProgram(intcode)
    maze = {}
    explore((0, 0), prog, maze)
    maze[(0, 0)] = 'S'
    return maze


intcode = parse_intput(sys.argv[1])
maze = create_maze(intcode)

print(draw(maze))
print("Part 1:", part1(maze))
print("Part 2:", part2(maze))
