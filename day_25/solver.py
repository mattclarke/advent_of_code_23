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


def solve():
    to_ignore = set()
    edge, _ = find_most_popular_edge(to_ignore)
    to_ignore.add(edge)
    edge, _ = find_most_popular_edge(to_ignore)
    to_ignore.add(edge)
    edge, _ = find_most_popular_edge(to_ignore)
    to_ignore.add(edge)

    _, result = find_most_popular_edge(to_ignore)
    return result * (len(layout) - result)


# Part 1 = 527790
print(f"answer = {solve()}")


# Internet solution using Karger's algorithm to find the minimum cut
def kargers(layout):
    import random

    # Need the links from a vertex to be a list as it
    # MUST keep duplicates
    new_layout = {}
    for n, v in layout.items():
        new_layout[n] = list(v)

    # Purely for information
    num_times_tried = 0

    # The algorithm is non-deterministic, so we have to repeat
    # The key insight is that the non-min-cut edges significantly outnumber
    # the min-cut edges, so we should find the answer reasonably quickly
    #
    # The puzzle tells us the min-cut is 3, so we know when we have found it.
    while True:
        num_times_tried += 1

        layout = copy.deepcopy(new_layout)

        # Run until only two vertices remain
        while len(layout) > 2:
            # Pick a vertex at random
            v1 = random.choice(list(layout.keys()))

            # Pick one of the vertices it joins to randomly
            v2 = random.choice(layout[v1])

            # Merge them together
            links = [x for x in layout[v1] + layout[v2] if x not in {v1, v2}]

            # Delete the two vertices
            del layout[v1]
            del layout[v2]

            # Nothing to do with the algorithm as such, but for the puzzle
            # we change the node name to contain all the nodes that have been
            # merged together separated by |
            # Afterwards we can then work out how many nodes in each partition.
            new_name = f"{v1}|{v2}"

            # Go through all the other vertices and replace references to the
            # old nodes with the new node name
            for n, v in layout.items():
                temp = [x if x not in {v1, v2} else new_name for x in v]
                layout[n] = temp

            # Add the new combined vertex
            layout[new_name] = links

        # See how many edges remain and if it what we want break
        # else try again
        num_edges = len(layout[list(layout.keys())[0]])
        if num_edges == 3:
            break

    print("number of tries =", num_times_tried)

    # Get size of partitions
    partition_sizes = [len(n.split("|")) for n in layout]
    print(f"answer = {partition_sizes[0] * partition_sizes[1]}")


kargers(layout)
