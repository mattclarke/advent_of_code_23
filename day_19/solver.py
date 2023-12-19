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
    n, r = rule.replace("}","").split("{")
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
            if l(i[v]):
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

result = 0

# Part 2 = 
print(f"answer = {result}")
