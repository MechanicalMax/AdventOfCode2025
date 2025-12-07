with open("input/day7.txt", 'r') as file:
    input = file.readlines()

def part1(data = input):
    splits = 0
    pointsToCheck = set()
    curRow = 0
    curCol = data[0].index('S')
    pointsToCheck.add((curRow, curCol))
    while pointsToCheck:
        newPoints = set()
        for point in pointsToCheck:
            row, col = point
            if row + 1 >= len(data):
                continue

            if data[row + 1][col] == '^':
                splits += 1
                if row + 1 < len(data):
                    newPoints.add((row + 1, col - 1))
                    newPoints.add((row + 1, col + 1))
            else:
                newPoints.add((row + 1, col))
        pointsToCheck = newPoints
    return splits

example = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]
print(part1(example))
print(part1())