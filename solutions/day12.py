with open("input/day12.txt") as f:
    input_lines = f.read().splitlines()

# ---------------- Parsing ----------------

def parse_input(lines):
    shapes = []
    for i in range(6):
        shape = set()
        for r in range(3):
            line = lines[i * 5 + 1 + r]
            for c, ch in enumerate(line):
                if ch == "#":
                    shape.add((r, c))
        shapes.append(shape)

    regions = []
    for line in lines[30:]:
        size, nums = line.split(":")
        w, h = map(int, size.split("x"))
        quantities = list(map(int, nums.split()))
        regions.append((w, h, quantities))

    return shapes, regions

# ---------------- Geometry ----------------

def normalize(shape):
    minx = min(x for x, y in shape)
    miny = min(y for x, y in shape)
    return {(x - minx, y - miny) for x, y in shape}

def orientations(shape):
    """All rotations + flips"""
    out = set()
    cur = normalize(shape)
    for _ in range(4):
        out.add(frozenset(cur))
        out.add(frozenset(normalize({(x, -y) for x, y in cur})))
        cur = normalize({(y, -x) for x, y in cur})
    return out

# ---------------- Solver ----------------

def solve_region(width, height, shapes, quantities):
    N = width * height

    # --- area pruning ---
    if sum(len(shapes[i]) * quantities[i] for i in range(len(shapes))) > N:
        return False

    # --- generate placements as bitmasks ---
    placements = []
    shape_areas = []

    for shape in shapes:
        ps = []
        for orient in orientations(shape):
            xs = [x for x, y in orient]
            ys = [y for x, y in orient]
            maxx, maxy = max(xs), max(ys)

            for r in range(height - maxx):
                for c in range(width - maxy):
                    mask = 0
                    for x, y in orient:
                        idx = (r + x) * width + (c + y)
                        mask |= 1 << idx
                    ps.append(mask)

        placements.append(ps)
        shape_areas.append(len(shape))

    # --- reorder shapes: large & constrained first ---
    order = sorted(
        range(len(shapes)),
        key=lambda i: (-shape_areas[i], len(placements[i]))
    )

    placements = [placements[i] for i in order]
    quantities = [quantities[i] for i in order]
    shape_areas = [shape_areas[i] for i in order]

    seen = set()

    def backtrack(mask, si):
        if si == len(placements):
            return True

        state = (mask, si)
        if state in seen:
            return False

        needed = quantities[si]

        def place_k(k, cur_mask):
            if k == needed:
                return backtrack(cur_mask, si + 1)

            for p in placements[si]:
                if p & cur_mask:
                    continue
                if place_k(k + 1, cur_mask | p):
                    return True
            return False

        ok = place_k(0, mask)
        if not ok:
            seen.add(state)
        return ok

    return backtrack(0, 0)

# ---------------- Part 1 ----------------

def part1(lines = input_lines):
    shapes, regions = parse_input(lines)
    return sum(
        solve_region(w, h, shapes, q)
        for w, h, q in regions
    )

# ---------------- Run ----------------

example = [
    "0:",
    "###",
    "##.",
    "##.",
    "",
    "1:",
    "###",
    "##.",
    ".##",
    "",
    "2:",
    ".##",
    "###",
    "##.",
    "",
    "3:",
    "##.",
    "###",
    "##.",
    "",
    "4:",
    "###",
    "#..",
    "###",
    "",
    "5:",
    "###",
    ".#.",
    "###",
    "",
    "4x4: 0 0 0 0 2 0",
    "12x5: 1 0 1 0 2 2",
    "12x5: 1 0 1 0 3 2",
]

print(part1(example))  # -> 2
print(part1())