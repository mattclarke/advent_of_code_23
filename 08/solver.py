import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

route = lines.pop(0)

M = {}

for l in lines:
    l = l.replace(" = ", " ").replace("(", "").replace(")", "").replace(",", "")
    pos, left, right = l.split(" ")
    M[pos] = (left, right)

result = 0
loc = "AAA"
index = 0

while loc != "ZZZ":
    choice = route[index % len(route)]
    if choice == "L":
        loc = M[loc][0]
    else:
        loc = M[loc][1]
    index += 1
    result += 1

# Part 1 = 19783
print(f"answer = {result}")

starting = [x for x in M if x.endswith("A")]
loc = "AAA"
index = 0

results = [None for _ in starting]

while True:
    choice = route[index % len(route)]
    for i, l in enumerate(starting):
        if choice == "L":
            l = M[l][0]
        else:
            l = M[l][1]
        starting[i] = l
        if l.endswith("Z") and results[i] is None:
            results[i] = index + 1

    index += 1
    if all(results):
        break


# Crude lcm
base = results.pop(0)
result = base
target = results.pop(0)

while True:
    if result % target == 0:
        base = result
        if results:
            target = results.pop(0)
        else:
            break
    result += base

# Part 2 = 9177460370549
print(f"answer = {result}")
