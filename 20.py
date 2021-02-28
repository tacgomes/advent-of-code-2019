#!/usr/bin/env python3

import sys

from collections import deque


MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))


def parse_intput(filename):
    return list(map(list, open(filename).read().splitlines()))


def is_outer_portal(maze, r, c):
    return (
        r == 1 or r == len(maze) - 2 or
        c == 1 or c == len(maze[0]) - 2
    )


def find_portals(maze):
    portals = {}
    name2pos = {}

    for r, row in enumerate(maze):
        for c in range(len(row) - 1):
            if maze[r][c].isupper() and maze[r][c + 1].isupper():
                portal = maze[r][c] + maze[r][c + 1]
                # Exit on the left of the portal
                if c - 1 >= 0 and maze[r][c - 1] == '.':
                    entrance1 = r, c
                    exit1 = r, c - 1
                # Exit on the right of the portal
                else:
                    entrance1 = r, c + 1
                    exit1 = r, c + 2

                entrance2, exit2 = name2pos.get(portal, (None, None))
                if entrance2 is not None:
                    portals[entrance1] = exit2
                    portals[entrance2] = exit1
                else:
                    name2pos[portal] = entrance1, exit1

    for c in range(len(maze[0])):
        for r in range(len(maze) - 1):
            if maze[r][c].isupper() and maze[r + 1][c].isupper():
                portal = maze[r][c] + maze[r + 1][c]
                # Exit at the top of the portal
                if r - 1 >= 0 and maze[r - 1][c] == '.':
                    entrance1 = r, c
                    exit1 = r - 1, c
                # Exit at the bottom of the portal
                else:
                    entrance1 = r + 1, c
                    exit1 = r + 2, c

                entrance2, exit2 = name2pos.get(portal, (None, None))
                if entrance2 is not None:
                    portals[entrance1] = exit2
                    portals[entrance2] = exit1
                else:
                    name2pos[portal] = entrance1, exit1

    return name2pos['AA'][1], name2pos['ZZ'][1], portals


def explore_nonrecursive(maze, start, end, portals):
    visited, queue = set(), deque([(0, start)])

    while queue:
        steps, pos = queue.popleft()

        if pos == end:
            return steps

        visited.add(pos)

        for my, mx in MOVES:
            new_r, new_c = pos[0] + my, pos[1] + mx
            if (new_r, new_c) not in visited:
                cell = maze[new_r][new_c]
                if cell.isupper() and (new_r, new_c) in portals:
                    queue.append((steps + 1, portals[(new_r, new_c)]))
                elif cell == '.':
                    queue.append((steps + 1, (new_r, new_c)))


def explore_recursive(maze, start, end, portals):
    visited, queue = set(), deque([(0, 0, start)])

    while queue:
        steps, level, pos = queue.popleft()

        if pos == end and level == 0:
            return steps

        visited.add((level, pos))

        for (my, mx) in MOVES:
            new_r, new_c = new_pos = pos[0] + my, pos[1] + mx
            if (level, new_pos) not in visited:
                cell = maze[new_r][new_c]
                if cell.isupper():
                    outer_portal = is_outer_portal(maze, new_r, new_c)
                    valid_outer_portal = (
                        outer_portal and
                        level > 0 and
                        new_pos not in (start, end)
                    )
                    if (not outer_portal or valid_outer_portal) and (
                            new_pos in portals):
                        new_pos = portals[new_pos]
                        new_l = level - 1 if outer_portal else level + 1
                        queue.append((steps + 1, new_l, new_pos))
                elif cell == '.':
                    queue.append((steps + 1, level, new_pos))


def part1(maze):
    start, end, portals = find_portals(maze)
    return explore_nonrecursive(maze, start, end, portals)


def part2(maze):
    start, end, portals = find_portals(maze)
    return explore_recursive(maze, start, end, portals)


maze = parse_intput(sys.argv[1])
print("Part 1:", part1(maze))
print("Part 2:", part2(maze))
