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
    ROWS = set()

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
        ROWS.add(pos[0])

    CORNERS[(0, 0)] = "F"  # From looking at the input
    ROWS = list(sorted(ROWS))

    result = 0
    r = HMIN

    while r < HMAX + 1:
        if r in ROWS:
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
        else:
            walls = []
            for (st_r, st_c), (end_r, end_c) in zip(VERT_START, VERT_END):
                if st_r <= r <= end_r:
                    walls.append((r, st_c))

            walls.sort()
            inside = False
            prev_wall = None
            i = 0
            while i < len(walls):
                if inside:
                    result += walls[i][1] - prev_wall[1] + 1
                    inside = False
                else:
                    inside = True
                    prev_wall = walls[i]
                i += 1
        r += 1
    return result


# Part 1 = 36679
print(f"answer = {solve()}")

# Part 2 = 88007104020978
print(f"answer = {solve(True)}")
