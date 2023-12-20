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

result = 0

# Part 2 =
print(f"answer = {result}")
