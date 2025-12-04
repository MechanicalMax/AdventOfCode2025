with open('input/day4.txt') as f:
    lines = [l.strip() for l in f.readlines()]

directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
def isInGrid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def part1(grid = lines):
    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '@':
                continue
            adjacent_rolls = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if isInGrid(r, c, grid) and grid[r][c] == '@':
                    adjacent_rolls += 1
                    if adjacent_rolls >= 4:
                        break
            if adjacent_rolls >= 4:
                continue
            else:
                accessible_rolls += 1
    return accessible_rolls

example = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]
print(part1(example))
print(part1())