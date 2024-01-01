import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

MIN = 200000000000000
MAX = 400000000000000
# MIN = 7
# MAX = 27

COORDS = []
SPEEDS = []

for l in lines:
    coords, speeds = l.split(" @ ")
    coords = eval(f"({coords})")
    speeds = eval(f"({speeds})")
    COORDS.append(coords)
    SPEEDS.append(speeds)

grads = []
offsets = []

for (x, y, _), (dx, dy, _) in zip(COORDS, SPEEDS):
    grad = dy / dx
    offset = y - (grad * x)
    grads.append(grad)
    offsets.append(offset)

result = 0

for i in range(len(grads)):
    for j in range(i + 1, len(grads)):
        g1 = grads[i]
        g2 = grads[j]
        o1 = offsets[i]
        o2 = offsets[j]
        if g1 == g2:
            continue

        x_int = (o1 - o2) / (g2 - g1)
        y_int = g1 * x_int + o1
        okay = True
        if x_int > COORDS[i][0] and SPEEDS[i][0] < 0:
            okay = False
        elif x_int < COORDS[i][0] and SPEEDS[i][0] > 0:
            okay = False
        if y_int > COORDS[j][1] and SPEEDS[j][1] < 0:
            okay = False
        elif y_int < COORDS[j][1] and SPEEDS[j][1] > 0:
            okay = False
        if x_int < MIN or x_int > MAX:
            okay = False
        if y_int < MIN or y_int > MAX:
            okay = False

        if okay:
            result += 1

# Part 1 = 20847
print(f"answer = {result}")
result = 0


def find_velocity_for_axis(same_v, axis):
    result = set()
    for i, j in same_v:
        diff = abs(COORDS[i][axis] - COORDS[j][axis])
        poss = set()
        # Find all the possible velocities that could be possible for this pair.
        # Brute force FTW!
        for v in range(-1000, 1000):
            if v == SPEEDS[i][axis]:
                # cannot mod zero, so skip this v
                continue
            # See if a rock moving at v can hit both.
            if diff % (v - SPEEDS[i][axis]) == 0:
                poss.add(v)
        if not result:
            result = poss
        else:
            result = result.intersection(poss)
    # Only one v value will work for all pairs of the same velocity
    assert len(result) == 1, f"{result}"
    return result.pop()


# Finding the velocities.
# By considering pairs of hailstones with the same velocity along one axis
# we can work out vRock along that axis. One pair might have multiple solutions
# but only one value for vRock will work for all.
#
# Worked example:
#     Consider two hailstones with vHailstone = 2 (along x), and x positions 10 and 20
#     respectively:
#     At t = t0, x1 = 10 and x2 = 20
#     At t = t0 + 1, x1 = 12 and x2 = 22
#     At t = t0 + 2, x1 = 14 and x2 = 24
#     At t = t0 + 3, x1 = 16 and x2 = 26 and so on.
#
#     Consider a rock with vRock = 7 that hits the first hailstone at t0 + 1:
#     At t = t0 + 1, rx = 12
#     At t = t0 + 2, rx = 19
#     At t = t0 + 3, rx = 26 <- hits the second hailstone, so 7 is a possible speed
#
#     Unfortunately, we don't know t0, so need a general solution.
#
#     The distance between the two hailstones is fixed (as the velocities are the same).
#     If we change the frame of reference so the hailstones aren't moving then the rock's
#     velocity becomes vRock - vHailstone (for this example: 7 - 2 = 5).
#     The rock hits both if: 
#         diff_in_position % (vRock - vHailstone) == 0
#     
#     For the example: (20 - 10) % (7 - 2) = 10 % 5 = 0    <- 7 is a valid solution
#
#     Another possible solution:
#         (20 - 10) % (12 - 2) = 10 % 10 = 0

# Find pairs of hailstones with the same speed in x
same = []
for i in range(len(SPEEDS)):
    for j in range(i + 1, len(SPEEDS)):
        if SPEEDS[i][0] == SPEEDS[j][0]:
            same.append((i, j))
v_x = find_velocity_for_axis(same, 0)

# Find pairs of hailstones with the same speed in y
same = []
for i in range(len(SPEEDS)):
    for j in range(i + 1, len(SPEEDS)):
        if SPEEDS[i][1] == SPEEDS[j][1]:
            same.append((i, j))
v_y = find_velocity_for_axis(same, 1)

# Find pairs of hailstones with the same speed in z
same = []
for i in range(len(SPEEDS)):
    for j in range(i + 1, len(SPEEDS)):
        if SPEEDS[i][2] == SPEEDS[j][2]:
            same.append((i, j))
v_z = find_velocity_for_axis(same, 2)

# Pick two hailstones
# Calculate the lines for both
grads = []
offsets = []

for (x, y, _), (dx, dy, _) in zip(COORDS[0:2], SPEEDS[0:2]):
    # Substract the rock speed from both, so effectively the rock is stationary
    grad = (dy - v_y) / (dx - v_x)
    offset = y - (grad * x)
    grads.append(grad)
    offsets.append(offset)

# The two lines will intersect at the rocks location
# First find x
x = (offsets[0] - offsets[1]) / (grads[1] - grads[0])

# Using x we can calculate the number of turns it takes the rock to hit the
# first hailstone
# And that can be used to calculate y and z (without any floating point issues)
t = abs((COORDS[0][0] - x) / (SPEEDS[0][0] - v_x))
y = COORDS[0][1] + t * (SPEEDS[0][1] - v_y)
z = COORDS[0][2] + t * (SPEEDS[0][2] - v_z)

# Part 2 = 908621716620524
print(f"answer = {int(x + y + z)}")
