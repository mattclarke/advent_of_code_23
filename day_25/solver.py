import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]

layout = {}

for l in lines:
    node, nodes = l.split(": ")
    nodes = nodes.split(" ")
    temp = layout.get(node, set())
    for n in nodes:
        temp.add(n)
        nt = layout.get(n, set())
        nt.add(node)
        layout[n] = nt
    layout[node] = temp


def walk(start, ignore=set()):
    Q = [(start, 0, [])]
    SEEN = {start: (0, [])}
    MAX = 0

    while Q:
        curr, steps, path = Q.pop(0)
        for lnk in layout[curr]:
            if lnk in SEEN and SEEN[lnk][0] <= steps + 1:
                continue
            curr_lnk = tuple(sorted([lnk, curr]))
            if curr_lnk in ignore:
                continue
            else:
                cpath = path[:]
                cpath.append(curr_lnk)
                MAX = max(MAX, steps + 1)
                SEEN[lnk] = (steps + 1, cpath[:])
                Q.append((lnk, steps + 1, cpath[:]))
    return [y for x, y in SEEN.values() if x == MAX], len(SEEN)


def find_most_popular_edge(ignore=set()):
    HOT_SPOT = {}
    result = 0
    for start in layout:
        ans, size = walk(start, ignore)
        result = max(result, size)
        for x in ans:
            for y in x:
                if y in HOT_SPOT:
                    HOT_SPOT[y] += 1
                else:
                    HOT_SPOT[y] = 1
    a = list(HOT_SPOT.items())
    a.sort(key=lambda x: x[1])
    return a[~0][0], result


to_ignore = set()
edge, _ = find_most_popular_edge(to_ignore)
to_ignore.add(edge)
edge, _ = find_most_popular_edge(to_ignore)
to_ignore.add(edge)
edge, _ = find_most_popular_edge(to_ignore)
to_ignore.add(edge)

_, result = find_most_popular_edge(to_ignore)

# Part 1 = 527790
print(f"answer = {result * (len(layout) - result)}")
