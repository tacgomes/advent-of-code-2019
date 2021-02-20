#!/usr/bin/env python3

import sys

from collections import deque


MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))


def parse_intput(filename):
    return list(map(list, open(filename).read().splitlines()))


def find_reachable_keys(maze, positions, keys_to_collect):
    reachable_keys = {}
    visited = set()

    for robot, position in enumerate(positions):
        queue = deque([(0, robot, position)])
        while queue:
            steps, robot, pos = queue.popleft()
            visited.add(pos)
            r, c = pos
            symb = maze[r][c]

            if symb.islower() and symb in keys_to_collect:
                reachable_keys[symb] = (steps, robot, pos)
                continue
            elif symb.isupper() and symb.lower() in keys_to_collect:
                continue

            for m in MOVES:
                new_r, new_c = r + m[0], c + m[1]
                if maze[new_r][new_c] != '#' and (new_r, new_c) not in visited:
                    queue.append((steps + 1, robot, (new_r, new_c)))

    return reachable_keys


def find_all_keys(maze, positions, total_steps, keys_to_collect, cache):
    if (positions, keys_to_collect) in cache:
        return total_steps + cache[(positions, keys_to_collect)]

    reachable_keys = find_reachable_keys(maze, positions, keys_to_collect)
    if not reachable_keys:
        return total_steps

    min_steps = sys.maxsize
    for key, val in reachable_keys.items():
        steps, robot, pos = val
        new_positions = (*positions[:robot], pos, *positions[robot + 1:])
        new_keys_to_collect = tuple(
            filter(lambda k: key != k, keys_to_collect)
        )
        steps = find_all_keys(
            maze, new_positions, steps, new_keys_to_collect, cache
        )
        min_steps = min(min_steps, steps)

    cache[(positions, keys_to_collect)] = min_steps

    return total_steps + min_steps


def get_start_position(maze):
    return next(
        (r, c)
        for r, row in enumerate(maze)
        for c, col in enumerate(row)
        if col == '@'
    )


def get_keys_to_collect(maze):
    return tuple(
        col
        for r, row in enumerate(maze)
        for c, col in enumerate(row)
        if col.islower()
    )


def part1(maze):
    start_pos = get_start_position(maze)
    positions = (start_pos,)
    keys_to_collect = get_keys_to_collect(maze)
    return find_all_keys(maze, positions, 0, keys_to_collect, {})


def part2(maze):
    start_r, start_c = get_start_position(maze)
    maze[start_r][start_c] = '#'
    maze[start_r - 1][start_c] = '#'
    maze[start_r][start_c + 1] = '#'
    maze[start_r + 1][start_c] = '#'
    maze[start_r][start_c - 1] = '#'
    positions = (
        (start_r - 1, start_c - 1),
        (start_r - 1, start_c + 1),
        (start_r + 1, start_c - 1),
        (start_r + 1, start_c + 1),
    )
    keys_to_collect = get_keys_to_collect(maze)
    return find_all_keys(maze, positions, 0, keys_to_collect, {})


maze = parse_intput(sys.argv[1])
print("Part 1:", part1(maze))
print("Part 2:", part2(maze))
