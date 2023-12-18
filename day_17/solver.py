import copy
import heapq
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


def print_layout(seen):
    for r in range(H):
        line = ""
        for c in range(W):
            if (r, c) in seen:
                line += "#"
            else:
                line += "."
        print(line)
    print("=======================")


def solve():
    SEEN = {}
    best = 1000000000

    Q = [(0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 0)]

    while Q:
        r, c, dr, dc, f, score = heapq.heappop(Q)
        if SEEN.get((r, c, dr, dc, f), 1000000000) <= score:
            continue
        SEEN[(r, c, dr, dc, f)] = score
        if r == H - 1 and c == W - 1:
            best = min(best, score)
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
            heapq.heappush(Q, (r, c, dr, dc, f, score + lines[r][c]))
    return best


result = solve()

# Part 1 = 1246
print(f"answer = {result}")


def solve():
    SEEN = {}
    best = 1000000000

    Q = [(0, 0, 0, 1, 0, 0), (0, 0, 1, 0, 0, 0)]

    while Q:
        r, c, dr, dc, f, score = heapq.heappop(Q)
        if SEEN.get((r, c, dr, dc, f), 1000000000) <= score:
            continue
        SEEN[(r, c, dr, dc, f)] = score
        if r == H - 1 and c == W - 1 and f >= 4:
            best = min(best, score)
            continue
        options = []
        options.append((r + dr, c + dc, dr, dc, f + 1))
        if f >= 4:
            options.append(turn_right(r, c, dr, dc, f))
            options.append(turn_left(r, c, dr, dc, f))
        for r, c, dr, dc, f in options:
            if f > 10:
                # must turn
                continue
            if r < 0 or r >= H or c < 0 or c >= W:
                # out of bounds
                continue
            if score + lines[r][c] >= best:
                continue
            heapq.heappush(Q, (r, c, dr, dc, f, score + lines[r][c]))
    return best


# Part 2 = 1389
print(f"answer = {solve()}")
