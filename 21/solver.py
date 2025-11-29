import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]
lines = [[x for x in line] for line in lines]

S = None
for r, row in enumerate(lines):
    for c, ch in enumerate(row):
        if ch == "S":
            S = (r, c)
            break
    if S:
        break
lines[S[0]][S[1]] = "."


possible = {S}
for _ in range(64):
    new_possible = set()
    for p in possible:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = p[0] + dr
            c = p[1] + dc
            if dr == 0 and dc == 0:
                continue
            if r < 0 or r >= len(lines):
                continue
            if c < 0 or c >= len(lines[0]):
                continue
            if lines[r][c] != "#":
                new_possible.add((r, c))
    possible = new_possible


# Part 1 = 3858
print(f"answer = {len(possible)}")


def print_layout(layout, start=S):
    sor = sorted(layout)
    min_r = min(sor[0][0], 0)
    max_r = max(sor[~0][0], len(lines))
    for r in range(min_r - 1, max_r + 1):
        line = ""
        for c in range(min_r - 1, max_r + 1):
            if (r, c) == S:
                line += "S"
            elif (r, c) in layout:
                line += "O"
            else:
                line += lines[r % len(lines)][c % len(lines)]
        print(line)
    print("================")
    print("size", len(layout))
    print("================")


def solve(start, steps):
    answers = []
    possible = {start}
    for i in range(steps):
        new_possible = set()
        for p in possible:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = p[0] + dr
                c = p[1] + dc
                if dr == 0 and dc == 0:
                    continue
                rr = r % len(lines)
                cc = c % len(lines[0])
                if lines[rr][cc] != "#":
                    new_possible.add((r, c))
        possible = new_possible
        if i == 131 * (len(answers) + 1) + 64:
            answers.append(len(possible))
    return answers


REQUIRED = 26501365
NUM_SQUARES = REQUIRED // len(lines)

# Solve a few lower rounds
solutions = solve(S, 131 * 4 + 65)

# The diff between solutions increases by a set amount
# for each pair
differences = []
for a, b in zip(solutions, solutions[1:]):
    differences.append(b - a)

# The difference of the differences is constant
diff_diff = []
for a, b in zip(differences, differences[1:]):
    diff_diff.append(b - a)

result = solutions[0]
diff = differences[0]

for i in range(NUM_SQUARES - 1):
    result = result + diff
    diff += diff_diff[0]

# Part 2 = 636350496972143
print(f"answer = {result}")
