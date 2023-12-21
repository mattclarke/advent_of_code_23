import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

HIGH = 123
LOW = 42
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
        if pulse == LOW:
            if self.on:
                self.on = False
                for d in self.dest:
                    low_sent += 1
                    result.append((d, LOW, self.name))
            else:
                self.on = True
                for d in self.dest:
                    high_sent += 1
                    result.append((d, HIGH, self.name))
        return result

    def __repr__(self):
        return f"FF {self.name}, {self.on}, {self.dest}"


class Conjunction:
    def __init__(self):
        self.dest = []
        self.senders = {}
        self.name = None
        self.all_high = False
    

    def send(self, pulse, sender):
        global low_sent, high_sent
        result = []
        curr = self.senders.get(sender, LOW)
        self.senders[sender] = pulse
        # print("hello",self.name,  pulse, self.senders)
        all_high = True
        for v in self.senders.values():
            if v == LOW:
                all_high = False
        self.all_high = all_high

        if all_high:
            for d in self.dest:
                low_sent += 1
                result.append((d, LOW, self.name))
        else:
            for d in self.dest:
                high_sent += 1
                result.append((d, HIGH, self.name))
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
# TODO: do this in a better way!
for i in range(1000):
    Q = [("broadcaster", LOW, "")]

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
            modules[k].senders[n] = LOW

low_sent = 0
high_sent = 0

outputs = {}
modules_pt2 = copy.deepcopy(modules)

for _ in range(1000):
    Q = [("broadcaster", LOW, "")]
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
not_done = True
for i in range(1, 1000000):
    Q = [("broadcaster", LOW, "")]

    while Q:
        d, pulse, n = Q.pop(0)
        if d in modules_pt2:
            temp = modules_pt2[d].send(pulse, n)
            for t in temp:
                Q.append(t)
        for m in ["hl", "hq", "bc", "ql"]:
            if modules_pt2[m].all_high:
                temp = collect.get(m, (0, 0))
                if temp[1] != i:
                    collect[m] = (temp[1], i)
starts = []
steps = []
for m in ["hl", "hq", "bc", "ql"]:
    prev, last = collect[m]
    print(m, last, last-prev, collect[m])
    starts.append(last)
    steps.append(last - prev)

s1 = starts.pop(0)
step1 = steps.pop(0)

s2 = starts.pop(0)
step2 = steps.pop(0)

while True:
    while s1 != s2:
        if s1 < s2:
            s1 += step1
        else:
            if (s1 - s2) > step2:
                nsteps = (s1 - s2) // step2
                s2 += step2 *nsteps
            else:
                s2 += step2
    print("done", s1, s2, step1)
    input()
    step1 = step1 * step2
    s2 = starts.pop(0)
    step2 = steps.pop(0)

# Part 2 =
print(f"answer = {result}")
