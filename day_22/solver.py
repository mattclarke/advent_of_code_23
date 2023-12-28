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


def compare_heights(a,b):
    alow = min(a[0][2],a[1][2])
    blow = min(b[0][2],b[1][2])
    if alow < blow:
        return -1
    elif alow > blow:
        return 1
    else:
        return 0

import functools
freefall.sort(key=functools.cmp_to_key(compare_heights))


def resting_on(current, previous):
    (cx1, cy1, cz1), (cx2, cy2, cz2) = current
    (px1, py1, pz1), (px2, py2, pz2) = previous
    px1, px2 = sorted([px1, px2])
    cx1, cx2 = sorted([cx1, cx2])
    py1, py2 = sorted([py1, py2])
    cy1, cy2 = sorted([cy1, cy2])
    px = set(range(px1, px2+1))
    cx = set(range(cx1, cx2+1))
    xokay = len(cx.intersection(px)) > 0
    py = set(range(py1, py2+1))
    cy = set(range(cy1, cy2+1))
    yokay = len(cy.intersection(py)) > 0
    # TODO: check heights: if they are the same then it cannot rest on it
    if xokay and yokay:
        pz = set(range(pz1, pz2+1))
        cz = set(range(cz1, cz2+1))
        zokay = len(cz.intersection(pz)) > 0
        if zokay:
            assert False
    return xokay and yokay


assert resting_on(((0,0,2),(2,0,2)), ((1,0,1),(1,2,1)))


resting = []
is_resting_on = {}

for i, (first, second) in enumerate(freefall):
    on = []
    heights = []
    for j, f, s in resting:
        if resting_on((first, second), (f,s)):
            on.append(j)
            heights.append(max(f[2], s[2]))
    if on:
        mh = max(heights)
        for o, h in zip(on, heights):
            if h == mh:
                temp = is_resting_on.get(i, set())
                temp.add(o)
                is_resting_on[i] = temp
        new_heights = (mh+1, mh+1)
        if first[2] > second[2]:
            new_heights = (new_heights[0] + first[2] - second[2], new_heights[0])
        elif second[2] > first[2]:
            new_heights = (new_heights[0], new_heights[1]+ second[2] - first[2])

        resting.append((i, (first[0], first[1], new_heights[0]), (second[0], second[1], new_heights[1])))
    else:
        resting.append((i, (first[0], first[1], first[2]), (second[0], second[1], second[2])))

print(is_resting_on)

cannot = set()
for k,v in is_resting_on.items():
    if len(v) == 1:
        for x in v:
            cannot.add(x)

# Part 1 = 
print(f"answer = {len(resting) - len(cannot)}")

result = 0

# Part 2 = 
print(f"answer = {result}")
