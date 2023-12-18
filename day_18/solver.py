import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]


def print_layout(layout):
    for r in range(HMIN, HMAX + 1):
        line = ""
        for c in range(WMIN, WMAX + 1):
            if (r, c) in dug:
                line += "#"
            else:
                line += "."
        print(line)
    print()


HMIN = 0
WMIN = 0
HMAX = 0
WMAX = 0
pos = (0, 0)
dug = {(0, 0)}

for l in lines:
    d, n, _ = l.split(" ")
    n = int(n)
    if d == "R":
        for _ in range(n):
            pos = (pos[0], pos[1] + 1)
            dug.add(pos)
    elif d == "L":
        for _ in range(n):
            pos = (pos[0], pos[1] - 1)
            dug.add(pos)
    elif d == "U":
        for _ in range(n):
            pos = (pos[0] - 1, pos[1])
            dug.add(pos)
    elif d == "D":
        for _ in range(n):
            pos = (pos[0] + 1, pos[1])
            dug.add(pos)
    else:
        assert False
    HMAX = max(HMAX, pos[0])
    WMAX = max(WMAX, pos[1])
    HMIN = min(HMIN, pos[0])
    WMIN = min(WMIN, pos[1])


result = 0

for r in range(HMIN, HMAX + 1):
    c = WMIN
    inside = False
    while c <= WMAX + 1:
        if (r, c) in dug and (r - 1, c) in dug and (r + 1, c) in dug:
            # simple wall
            inside = not inside
        elif (r, c) in dug and (r - 1, c) in dug and (r, c + 1) in dug:
            # L
            while (r, c + 1) in dug:
                c += 1
            if (r + 1, c) in dug:
                #  L7 is a wall
                inside = not inside
        elif (r, c) in dug and (r + 1, c) in dug and (r, c + 1) in dug:
            # F
            while (r, c + 1) in dug:
                c += 1
            if (r - 1, c) in dug:
                # FJ is a wall
                inside = not inside
        else:
            if inside:
                dug.add((r, c))
        c += 1
    assert inside == False


# Part 1 = 36679
print(f"answer = {len(dug)}")

result = 0

for l in lines:
    _, _, h = l.replace("(", "").replace(")", "").replace("#", "").split(" ")
    dist = h[:-1]
    d = int(h[~0])
    d = ["R", "D", "L", "U"][d]
    dist = int(dist, 16)
    print(d, dist)


# Part 2 =
print(f"answer = {result}")
