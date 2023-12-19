import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n")]

rules = []
inputs = []
r = True

for l in lines:
    if l == "":
        r = False
        continue
    if r:
        rules.append(l)
    else:
        if l:
            inputs.append(eval(l.replace("{", "dict(").replace("}", ")")))
RULES = {}
for rule in rules:
    n, r = rule.replace("}", "").split("{")
    parts = r.split(",")
    subrules = []
    for p in parts[:-1]:
        p1, p2 = p.split(":")
        c = p1[0]
        l = f"lambda x: x{p1[1:]}"
        subrules.append((c, eval(l), p2))
    subrules.append(parts[~0])
    RULES[n] = subrules


def is_accepted(initial):
    rule = RULES["in"]
    while True:
        default = True
        for v, l, t in rule[:-1]:
            if l(initial[v]):
                nrule = t
                default = False
                break
        if default:
            nrule = rule[~0]
        if nrule == "R":
            return False
        if nrule == "A":
            return True
        rule = RULES[nrule]


accepted = []
for i in inputs:
    if is_accepted(i):
        accepted.append(i)

result = sum([sum(v.values()) for v in accepted])

# Part 1 = 391132
print(f"answer = {result}")

RULES = {}
for rule in rules:
    n, r = rule.replace("}", "").split("{")
    parts = r.split(",")
    subrules = []
    for p in parts[:-1]:
        p1, p2 = p.split(":")
        c = p1[0]
        if ">" in p1:
            _, amt = p1.split(">")
            subrules.append((c, ">", int(amt), p2))
        else:
            _, amt = p1.split("<")
            subrules.append((c, "<", int(amt), p2))
    subrules.append(parts[~0])
    RULES[n] = subrules

Q = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
result = 0

while Q:
    node, xmas = Q.pop(0)
    # print(node, xmas)
    if node == "A":
        # Accepted
        value = 1
        for vl, vh in xmas.values():
            value *= vh - vl + 1
        result += value
        continue
    if node == "R":
        # Rejected
        continue
    for ch, sign, amt, target in RULES[node][:-1]:
        if xmas[ch] is not None:
            if sign == "<":
                if xmas[ch][0] < amt and xmas[ch][1] >= amt:
                    temp = copy.copy(xmas)
                    temp[ch] = (xmas[ch][0], amt - 1)
                    Q.append((target, temp))
                    xmas[ch] = (amt, xmas[ch][1])
                elif xmas[ch][1] < amt:
                    temp = copy.copy(xmas)
                    Q.append((target, temp))
                    xmas[ch] = None
            else:
                if xmas[ch][0] <= amt and xmas[ch][1] > amt:
                    temp = copy.copy(xmas)
                    temp[ch] = (amt + 1, xmas[ch][1])
                    Q.append((target, temp))
                    xmas[ch] = (xmas[ch][0], amt)
                elif xmas[ch][0] > amt:
                    temp = copy.copy(xmas)
                    Q.append((target, temp))
                    xmas[ch] = None
    Q.append((RULES[node][~0], xmas))

# Part 2 = 128163929109524
print(f"answer = {result}")
