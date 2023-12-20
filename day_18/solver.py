import copy
import sys


FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(FILE) as f:
    PUZZLE_INPUT = f.read()

lines = [line.strip() for line in PUZZLE_INPUT.split("\n") if line]


def solve(is_part_2=False):
    HMIN = 0
    HMAX = 0
    CORNERS = {}
    VERT_START = []
    VERT_END = []
    corner_rows = set()

    prev = None
    pos = (0, 0)

    for i, l in enumerate(lines):
        if is_part_2:
            _, _, h = l.replace("(", "").replace(")", "").replace("#", "").split(" ")
            n = h[:-1]
            d = int(h[~0])
            d = ["R", "D", "L", "U"][d]
            n = int(n, 16)
        else:
            d, n, _ = l.split(" ")
            n = int(n)

        if d == "R":
            if prev == "U":
                CORNERS[pos] = "F"
            elif prev == "D":
                CORNERS[pos] = "L"
            elif prev:
                assert False
            prev = "R"
            pos = (pos[0], pos[1] + n)
        elif d == "L":
            if prev == "U":
                CORNERS[pos] = "7"
            elif prev == "D":
                CORNERS[pos] = "J"
            elif prev:
                assert False
            prev = "L"
            pos = (pos[0], pos[1] - n)
        elif d == "U":
            if prev == "L":
                CORNERS[pos] = "L"
            elif prev == "R":
                CORNERS[pos] = "J"
            elif prev:
                assert False
            VERT_START.append((pos[0] - n, pos[1]))
            VERT_END.append(pos)
            prev = "U"
            pos = (pos[0] - n, pos[1])
        elif d == "D":
            if prev == "L":
                CORNERS[pos] = "F"
            elif prev == "R":
                CORNERS[pos] = "7"
            elif prev:
                assert False
            VERT_START.append(pos)
            VERT_END.append((pos[0] + n, pos[1]))
            prev = "D"
            pos = (pos[0] + n, pos[1])
        else:
            assert False
        HMAX = max(HMAX, pos[0])
        HMIN = min(HMIN, pos[0])
        corner_rows.add(pos[0])

    CORNERS[(0, 0)] = "F"  # From looking at the input
    corner_rows = list(sorted(corner_rows))

    result = 0
    r = HMIN

    while r < HMAX + 1:
        if r in corner_rows:
            walls = []
            for (st_r, st_c), (end_r, end_c) in zip(VERT_START, VERT_END):
                if st_r <= r <= end_r:
                    walls.append((r, st_c))

            walls.sort()
            inside = False
            prev_wall = None
            i = 0
            while i < len(walls):
                if walls[i] not in CORNERS:
                    # regular wall
                    if not inside:
                        prev_wall = walls[i]
                        inside = True
                    else:
                        result += walls[i][1] - prev_wall[1] + 1
                        inside = False
                elif CORNERS[walls[i]] == "F":
                    if CORNERS.get(walls[i + 1]) == "7":
                        if not inside:
                            result += walls[i + 1][1] - walls[i][1] + 1
                        i += 2
                        continue
                    elif CORNERS.get(walls[i + 1]) == "J":
                        if not inside:
                            inside = True
                            prev_wall = walls[i]
                            i += 2
                            continue
                        else:
                            inside = False
                            result += walls[i + 1][1] - prev_wall[1] + 1
                            i += 2
                            continue
                    else:
                        assert False
                elif CORNERS[walls[i]] == "L":
                    if CORNERS.get(walls[i + 1]) == "7":
                        if inside:
                            inside = False
                            result += walls[i + 1][1] - prev_wall[1] + 1
                            i += 2
                            continue
                        else:
                            inside = True
                            prev_wall = walls[i]
                            i += 2
                            continue
                    elif CORNERS.get(walls[i + 1]) == "J":
                        if not inside:
                            result += walls[i + 1][1] - walls[i][1] + 1
                        i += 2
                        continue

                i += 1
            corner_rows.pop(0)
            r += 1
        else:
            walls = []
            for (st_r, st_c), (end_r, end_c) in zip(VERT_START, VERT_END):
                if st_r <= r <= end_r:
                    walls.append((r, st_c))

            walls.sort()
            inside = False
            prev_wall = None
            i = 0
            row_count = 0
            while i < len(walls):
                if inside:
                    row_count += walls[i][1] - prev_wall[1] + 1
                    inside = False
                else:
                    inside = True
                    prev_wall = walls[i]
                i += 1

            # Until we reach a row with a corner in it, the number of inside
            # squares for the rows will be the same, so we can jump ahead.
            num_rows = corner_rows[0] - r
            result += row_count * num_rows
            r = corner_rows[0]
    return result


# Part 1 = 36679
print(f"answer = {solve()}")

# Part 2 = 88007104020978
print(f"answer = {solve(True)}")

# Internet solution - shoelace formula plus Pick's theorem
CORNERS = [(0, 0)]
pos = (0, 0)
LENGTH = 0

for i, l in enumerate(lines):
    _, _, h = l.replace("(", "").replace(")", "").replace("#", "").split(" ")
    n = h[:-1]
    d = int(h[~0])
    d = ["R", "D", "L", "U"][d]
    n = int(n, 16)

    LENGTH += n

    if d == "R":
        pos = (pos[0], pos[1] + n)
    elif d == "L":
        pos = (pos[0], pos[1] - n)
    elif d == "U":
        pos = (pos[0] - n, pos[1])
    elif d == "D":
        pos = (pos[0] + n, pos[1])
    else:
        assert False
    CORNERS.append(pos)


def shoelace(corners):
    result = 0
    for i in range(len(corners) - 1):
        pos1, pos2 = corners[i], corners[i + 1]
        result += (pos1[0] * pos2[1]) - (pos1[1] * pos2[0])

    # Can be negative depending on which way round the points we go
    return abs(result / 2)


# Note: shoelace works in non-integer space
# Doesn't matter in this case as everything is integers anyway...
result = int(shoelace(CORNERS))

# Pick's theorem (when all angles are 90 degrees:
#    Area = (number of internal points) - (number of points on the perimeter)/2 + 1
# The shoelace gives the number of internal points.
# The number of points on the perimeter is the LENGTH
# NOTE: Pick's theorem only works for integer space.
#
# For this puzzle, because the bounding line is a "thick" line, those squares need to be added too.
# => Total area = number of exterior points (Perimeter) + Pick's
# => Total area = LENGTH + shoelace - LENGTH/2 + 1
# => Total area = shoelace + LENGTH/2 + 1

# Pick's uses half the perimeter because half the line is already included in the
# shoelace calculation.
result += LENGTH // 2

# At each exterior corner, a 0.5x0.5 chunk is missing
# and at each interior corner, a 0.5x0.5 is an overlap
# So the exterior and interior cancel out, except there
# are four more exterior corners
# 4 x 0.5 x 0.5 = 1
result += 1

print(f"Internet answer = {result}")
