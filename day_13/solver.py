import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n")]

patterns = []
current = []
for l in lines:
    if l:
        current.append([x for x in l])
    else:
        patterns.append(current)
        current = []


def print_layout(layout):
    for r in layout:
        print("".join(r))
    print()


def find_reflection(rows, skip=-1):
    prev = None
    for ri, row in enumerate(rows):
        if prev and prev == row:
            # Potential reflection
            if ri == skip:
                # In part 2 we need to skip the original reflection
                # Even if it is still valid!
                continue
            ia = ri - 1
            ib = ri
            is_reflection = True
            while ia >= 0 and ib < len(rows):
                if rows[ia] != rows[ib]:
                    is_reflection = False
                    break
                ia -= 1
                ib += 1
            if is_reflection:
                return ri
        prev = row
    return 0


def find_reflection_v(p, skip=-1):
    cols = [[] for _ in p[0]]
    for row in p:
        for c, v in enumerate(row):
            cols[c].append(v)

    return find_reflection(cols, skip)


# Needed for part 2
original_horizontals = []
original_verticals = []

result = 0

for p in patterns:
    horiz = find_reflection(p)
    original_horizontals.append(horiz)
    result += 100 * horiz

    vert = find_reflection_v(p)
    original_verticals.append(vert)
    result += vert


# Part 1 = 34993
print(f"answer = {result}")

result = 0

for n, p in enumerate(patterns):
    done = False
    for r, row in enumerate(p):
        for c, v in enumerate(row):
            old = v
            new = "#" if v == "." else "."
            p[r][c] = new
            # print_layout(p)
            horiz = find_reflection(p, original_horizontals[n])
            if horiz:
                result += 100 * horiz
                done = True
                break
            vert = find_reflection_v(p, original_verticals[n])
            if vert:
                result += vert
                done = True
                break
            p[r][c] = old
        if done:
            break

# Part 2 = 29341
print(f"answer = {result}")
