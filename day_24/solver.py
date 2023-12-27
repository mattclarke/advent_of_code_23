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
        print("=========")
        print(COORDS[i], COORDS[j])
        g1 = grads[i]
        g2 = grads[j]
        o1 = offsets[i]
        o2 = offsets[j]
        if g1 == g2:
            print("    ", "parallel")
            continue

        x_int = (o1 - o2) / (g2 - g1)
        y_int = g1 * x_int + o1
        print("    ", x_int, y_int)
        okay = True
        if x_int > COORDS[i][0] and SPEEDS[i][0] < 0:
            okay = False
            print("    occured in the past for A")
        elif x_int < COORDS[i][0] and SPEEDS[i][0] > 0:
            okay = False
            print("    occured in the past for A")
        if y_int > COORDS[j][1] and SPEEDS[j][1] < 0:
            okay = False
            print("    occured in the past for B")
        elif y_int < COORDS[j][1] and SPEEDS[j][1] > 0:
            okay = False
            print("    occured in the past for B")
        if x_int < MIN or x_int > MAX:
            okay = False
            print("    out of bounds x")
        if y_int < MIN or y_int > MAX:
            okay = False
            print("    out of bounds y")

        if okay:
            print("    OKAY")
            result += 1

# Part 1 = 20847
print(f"answer = {result}")

result = 0

# Part 2 =
print(f"answer = {result}")
