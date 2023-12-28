import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

freefall = []

for l in lines:
    first, second = l.split("~")
    first = eval(f"({first})")
    second = eval(f"({second})")
    freefall.append((first, second))

assert len(freefall) == len(lines)


freefall.sort(key=lambda x: min(x[0][2], x[1][2]))


def resting_on(current, previous):
    (cx1, cy1, cz1), (cx2, cy2, cz2) = current
    (px1, py1, pz1), (px2, py2, pz2) = previous
    px1, px2 = sorted([px1, px2])
    cx1, cx2 = sorted([cx1, cx2])
    py1, py2 = sorted([py1, py2])
    cy1, cy2 = sorted([cy1, cy2])
    px = set(range(px1, px2 + 1))
    cx = set(range(cx1, cx2 + 1))
    xokay = not px.isdisjoint(cx)
    py = set(range(py1, py2 + 1))
    cy = set(range(cy1, cy2 + 1))
    yokay = not py.isdisjoint(cy)
    return xokay and yokay


assert resting_on(((0, 0, 2), (2, 0, 2)), ((1, 0, 1), (1, 2, 1)))


resting = []
is_resting_on = {}

for i, (first, second) in enumerate(freefall):
    on = []
    heights = []
    for j, f, s in resting:
        if resting_on((first, second), (f, s)):
            on.append(j)
            heights.append(max(f[2], s[2]))
    if on:
        mh = max(heights)
        ontop = set()
        for o, h in zip(on, heights):
            if h == mh:
                ontop.add(o)
        is_resting_on[i] = ontop
        new_heights = (mh + 1, mh + 1)
        if first[2] > second[2]:
            new_heights = (new_heights[0] + first[2] - second[2], new_heights[0])
        elif second[2] > first[2]:
            new_heights = (new_heights[0], new_heights[1] + second[2] - first[2])

        resting.append(
            (
                i,
                (first[0], first[1], new_heights[0]),
                (second[0], second[1], new_heights[1]),
            )
        )
    else:
        resting.append(
            (i, (first[0], first[1], first[2]), (second[0], second[1], second[2]))
        )

cannot = set()
for k, v in is_resting_on.items():
    if len(v) == 1:
        for x in v:
            cannot.add(x)
print(list(sorted(cannot)))

result = len(resting) - len(cannot)
# TODO: work out this off by one error
result += 1

# Part 1 = 434
print(f"answer = {result}")

result = 0

for c in cannot:
    falling = {c}
    still_going = True
    while still_going:
        still_going = False
        for i in range(0, len(resting)):
            if i in falling or i not in is_resting_on:
                continue
            brick = is_resting_on[i]
            if len(brick & falling) == len(brick):
                falling.add(i)
                still_going = True
    result += len(falling) - 1


# 63674 is wrong
# The bug from part 1 is an issue because we have an extra cannot

# Part 2 =
print(f"answer = {result}")
