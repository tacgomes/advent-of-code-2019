def draw(points):
    min_x = min(points.keys(), key=lambda p: p[0])[0]
    max_x = max(points.keys(), key=lambda p: p[0])[0]
    min_y = min(points.keys(), key=lambda p: p[1])[1]
    max_y = max(points.keys(), key=lambda p: p[1])[1]

    m = []
    for _ in range(min_y, max_y + 1):
        m.append([' ' for _ in range(min_x, max_x + 1)])

    for p, c in points.items():
        x, y = p[0] + min_x * -1, p[1] + min_y * -1
        m[y][x] = c

    return '\n'.join(''.join(r) for r in m)
