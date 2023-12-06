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
        diff = ans[0] - ans[1]
        h = ans[1] + ans[2] - 1
        rules[index].append([ans[1], h, diff])


def solve(current, rule):
    result = []
    for s in current:
        ans = s
        for r in rule:
            start, end, diff = r
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

# sorted so we can assume any seeds to the left of a rule as not changing
rules = [sorted(r) for r in rules]


def solve2(current, rule):
    result = []
    queue = current
    while queue:
        changed = False
        l, h = queue.pop(0)
        for r in rule:
            start, end, diff = r
            if l < start and h < start:
                # below range
                break
            elif l > end and h > end:
                # above range
                continue
            elif start <= l <= end and start <= h <= end:
                # both in range
                changed = True
                result.append([l + diff, h + diff])
                break
            elif l < start and h > end:
                # whole range covered
                changed = True
                result.append([start + diff, end + diff])
                result.append([l, start - 1])
                queue.append([end + 1, h])
                break
            elif l < start and start <= h <= end:
                # straddling start
                changed = True
                result.append([start + diff, h + diff])
                result.append([l, start - 1])
                break
            elif start <= l <= end and h > end:
                # straddling end
                changed = True
                result.append([l + diff, end + diff])
                queue.append([end + 1, h])
                break
            else:
                assert False, "Oops!"
        if not changed:
            result.append([l, h])
    return result


current = []
for i in range(0, len(seeds), 2):
    current.append([seeds[i], seeds[i] + seeds[i + 1] - 1])

for rule in rules:
    current = solve2(current, rule)

# Part 2 = 78775051
print(f"answer = {min(current)[0]}")
