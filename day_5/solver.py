import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n")]

_, s = lines[0].split(": ")
seeds = [int(x.strip()) for x in s.split(" ")]

lines.pop(0)
lines.pop(0)

rules = [[] for _ in range(7)]

index = 0
for line in lines:
    if not line:
        index += 1
    elif line[0].isdigit():
        ans = [int(x.strip()) for x in line.split(" ")]
        # TODO: store the diff and the end points
        diff = ans[0] - ans[1]
        h = ans[1] + ans[2] - 1
        rules[index].append([ans[1], h, diff])


def solve(current, convert):
    result = []
    for s in current:
        ans = s
        for c in convert:
            start, end, diff = c
            if start <= s <= end:
                ans = s + diff
                break
        result.append(ans)
    return result


current = list(seeds)
for rule in rules:
    current = solve(current, rule)


# Part 1 = 227653707
print(f"answer = {min(current)}")

current = []
for i in range(0, len(seeds), 2):
    current.append([seeds[i], seeds[i] + seeds[i + 1] - 1])


def solve(current, convert):
    result = []
    queue = current
    while queue:
        changed = False
        l, h = queue.pop(0)
        print("1", l, h)
        for c in convert:
            dest, src, r = c
            print(c)
            if src + r <= l or h < src:
                print("out")
                # out of range
                continue
            elif src <= l < src + r and h < src + r:
                # both in range
                print("both")
                changed = True
                l_diff = l - src
                h_diff = h - src
                result.append([dest + l_diff, dest + h_diff])
            elif src <= l < src + r:
                # only l is in range
                print("l")
                changed = True
                l_diff = l - src
                result.append([dest + l_diff, dest + r - 1])
                queue.append([src + r, h])
            elif h >= src and h < src + r:
                # only h in range
                print("h")
                changed = True
                h_diff = h - src
                result.append([dest, dest + h_diff])
                queue.append([l, src - 1])
            else:
                assert False, "oops"
            print("res", result)
            print("q", queue)
        if not changed:
            result.append([l, h])
    return result


print("======")
print(current)
current = solve(current, seed_to_soil)
print(current)
print("======")
current = solve(current, soil_to_fert)
print(current)
print("======")
current = solve(current, fert_to_water)
print(current)
print("======")
current = solve(current, water_to_light)
print(current)
print("======")
current = solve(current, light_to_temp)
print(current)
print("======")
# current = solve(current, temp_to_humid)
# current = solve(current, humid_to_loc)

# Part 2 = 78775051
print(f"answer = {min(current)}")
