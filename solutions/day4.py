with open('input/day4.txt') as f:
    lines = [l.strip() for l in f.readlines()]

directions = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
def isInGrid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

def isRollAccessible(row, col, grid):
    if grid[row][col] != '@':
        return False
    adjacent_rolls = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if isInGrid(r, c, grid) and grid[r][c] == '@':
            adjacent_rolls += 1
            if adjacent_rolls >= 4:
                break
    return adjacent_rolls < 4

def part1(grid = lines):
    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not isRollAccessible(row, col, grid):
                continue
            else:
                accessible_rolls += 1
    return accessible_rolls

def part2(grid = lines):
    rolls_removed = 0
    roll_positions = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                roll_positions.append((row, col))
    
    moreRollsCanBeRemoved = True
    while moreRollsCanBeRemoved:
        moreRollsCanBeRemoved = False
        for row, col in roll_positions:
            if isRollAccessible(row, col, grid):
                grid[row] = grid[row][:col] + '.' + grid[row][col+1:]
                rolls_removed += 1
                moreRollsCanBeRemoved = True
    return rolls_removed

# example = [
#     "..@@.@@@@.",
#     "@@@.@.@.@@",
#     "@@@@@.@.@@",
#     "@.@@@@..@.",
#     "@@.@@@@.@@",
#     ".@@@@@@@.@",
#     ".@.@.@.@@@",
#     "@.@@@.@@@@",
#     ".@@@@@@@@.",
#     "@.@.@@@.@.",
# ]
# print(part1(example))
# print(part2(example))
print(part1())
print(part2())