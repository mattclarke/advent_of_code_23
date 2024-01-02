import copy
import sys
from collections import deque


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

low_sent = 0
high_sent = 0


class Broadcaster:
    def __init__(self):
        self.dest = []
        self.name = "broadcaster"

    def send(self, pulse, sender):
        global low_sent
        result = []
        for d in self.dest:
            low_sent += 1
            result.append((d, pulse, self.name))
        return result


class Flipflop:
    def __init__(self):
        self.on = False
        self.dest = []
        self.name = None

    def send(self, pulse, sender):
        global low_sent, high_sent
        result = []
        if pulse == False:
            if self.on:
                self.on = False
                for d in self.dest:
                    low_sent += 1
                    result.append((d, False, self.name))
            else:
                self.on = True
                for d in self.dest:
                    high_sent += 1
                    result.append((d, True, self.name))
        return result

    def __repr__(self):
        return f"FF {self.name}, {self.on}, {self.dest}"


class Conjunction:
    def __init__(self):
        self.dest = []
        self.senders = {}
        self.name = None

    def all_high(self):
        return all(self.senders.values())

    def send(self, pulse, sender):
        global low_sent, high_sent
        result = []
        self.senders[sender] = pulse

        if self.all_high():
            for d in self.dest:
                low_sent += 1
                result.append((d, False, self.name))
        else:
            for d in self.dest:
                high_sent += 1
                result.append((d, True, self.name))
        return result

    def __repr__(self):
        return f"CJ {self.name}, {self.senders} {self.dest}"


modules = {}

for l in lines:
    if l.startswith("broadcaster"):
        l = l.replace("broadcaster -> ", "").replace(" ", "")
        dests = l.split(",")
        modules["broadcaster"] = Broadcaster()
        modules["broadcaster"].dest = dests
    elif l.startswith("%"):
        l = l[1:].replace("->", "|").replace(" ", "")
        n, dests = l.split("|")
        dests = dests.split(",")
        flip = Flipflop()
        flip.dest = dests
        flip.name = n
        modules[n] = flip
    elif l.startswith("&"):
        l = l[1:].replace("->", "|").replace(" ", "")
        n, dests = l.split("|")
        dests = dests.split(",")
        conj = Conjunction()
        conj.dest = dests
        conj.name = n
        modules[n] = conj
    else:
        assert False

modules_copy = copy.deepcopy(modules)

# Run a few times to setup the Conjunctions correctly
# This is where I had the bug that meant I thought it was
# a CRT problem and not an LCM problem.
# 1000 was too low
for i in range(5000):
    Q = [("broadcaster", False, "")]

    while Q:
        d, pulse, n = Q.pop(0)
        if d in modules_copy:
            temp = modules_copy[d].send(pulse, n)
            for t in temp:
                Q.append(t)

for k, v in modules_copy.items():
    if isinstance(v, Conjunction):
        inputs = {}
        for n in v.senders:
            modules[k].senders[n] = False

low_sent = 0
high_sent = 0

outputs = {}
modules_pt2 = copy.deepcopy(modules)

for _ in range(1000):
    Q = [("broadcaster", False, "")]
    low_sent += 1

    while Q:
        d, pulse, n = Q.pop(0)
        if d in modules:
            temp = modules[d].send(pulse, n)
            for t in temp:
                Q.append(t)
        else:
            v = outputs.get(d, 0)
            outputs[d] = v + 1

# Part 1 = 825896364
print(f"answer = {low_sent * high_sent}")

collect = {}
for i in range(1, 20_000):
    Q = deque([("broadcaster", False, "")])

    while Q:
        d, pulse, n = Q.popleft()
        if d in modules_pt2:
            temp = modules_pt2[d].send(pulse, n)
            for t in temp:
                Q.append(t)
        if d == "zg" and pulse:
            if n not in collect:
                collect[n] = i

steps = [x for x in collect.values()]

# LCM
step1 = steps.pop(0)
s1 = step1

step2 = steps.pop(0)
s2 = step2

while True:
    while s1 != s2:
        if s1 < s2:
            s1 += step1
        else:
            if (s1 - s2) > step2:
                nsteps = (s1 - s2) // step2
                s2 += step2 * nsteps
            else:
                s2 += step2
    step1 = step1 * step2
    if not steps:
        break
    step2 = steps.pop(0)
    s2 = step2

# Part 2 = 243566897206981
print(f"answer = {step1}")
