import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [[int(x) for x in line.strip()] for line in PUZZLE_INPUT.split("\n") if line]

W = len(lines[0])
H = len(lines)


def turn_right(r, c, dr, dc, f):
    if dr == 0 and dc == 1:
        # Right
        return r + 1, c, 1, 0, 1
    elif dr == 0 and dc == -1:
        # Left
        return r - 1, c, -1, 0, 1
    elif dr == 1 and dc == 0:
        # Down
        return r, c - 1, 0, -1, 1
    elif dr == -1 and dc == 0:
        # Up
        return r, c + 1, 0, 1, 1
    assert False


def turn_left(r, c, dr, dc, f):
    if dr == 0 and dc == 1:
        # Right
        return r - 1, c, -1, 0, 1
    elif dr == 0 and dc == -1:
        # Left
        return r + 1, c, 1, 0, 1
    elif dr == 1 and dc == 0:
        # Down
        return r, c + 1, 0, 1, 1
    elif dr == -1 and dc == 0:
        # Up
        return r, c - 1, 0, -1, 1
    assert False


def solve():
    SEEN = {}
    best = 1000000000

    Q = [(0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 0)]
    while Q:
        r, c, dr, dc, f, score = Q.pop(0)
        if (r, c, dr, dc, f) in SEEN:
            if SEEN[(r, c, dr, dc, f)] <= score:
                continue
        SEEN[(r, c, dr, dc, f)] = score
        # print(r, c, dr, dc, f, score)
        if r == H - 1 and c == W - 1:
            best = min(best, score)
            print(best)
            continue
        options = []
        options.append((r + dr, c + dc, dr, dc, f + 1))
        options.append(turn_right(r, c, dr, dc, f))
        options.append(turn_left(r, c, dr, dc, f))
        for r, c, dr, dc, f in options:
            if f > 3:
                # must turn
                continue
            if r < 0 or r >= H or c < 0 or c >= W:
                # out of bounds
                continue
            if score + lines[r][c] >= best:
                continue
            Q.append((r, c, dr, dc, f, score + lines[r][c]))
    return best


result = solve()

# Part 1 =
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
