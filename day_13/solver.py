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
        current.append(l)
    else:
        patterns.append(current)
        current = []


def find_reflection(rows):
    prev = None
    for ri, row in enumerate(rows):
        if prev and prev == row:
            # Potential reflection
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


result = 0

for p in patterns:
    # horizontal
    horiz = find_reflection(p)
    result += 100 * horiz

    # vertical
    # rotate
    cols = [[] for _ in p[0]]
    for row in p:
        for c, v in enumerate(row):
            cols[c].append(v)
    vert = find_reflection(cols)
    result += vert

# Part 1 = 34993
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
