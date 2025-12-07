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

# Attempted DFS approach
# def part2(data = input):
#     pathsToEnd = 0
#     # visited = set()
#     stack = [(0, data[0].index('S'))]

#     while stack:
#         row, col = stack.pop()
#         # if (row, col) in visited:
#             # continue
#         # visited.add((row, col))

#         if row == len(data) - 1:
#             pathsToEnd += 1
#             continue

#         if data[row + 1][col] == '^':
#             stack.append((row + 1, col - 1))
#             stack.append((row + 1, col + 1))
#         else:
#             stack.append((row + 1, col))
#     return pathsToEnd

def part2(data = input):
    pointsToCheck = set()
    startRow = 0
    startCol = data[startRow].index('S')
    pathsToPoint = {(startRow, startCol): 1}
    pointsToCheck.add((startRow + 1, startCol))
    while pointsToCheck:
        newPoints = set()
        for point in pointsToCheck:
            row, col = point
            if row >= len(data):
                continue

            if data[row][col] == '^':
                newPoints.add((row, col - 1))
                newPoints.add((row, col + 1))
                continue

            paths = 0
            if col-1>0 and data[row][col-1] == '^':
                paths += pathsToPoint.get((row - 1, col - 1), 0)
            if col+1<len(data[row]) and data[row][col+1] == '^':
                paths += pathsToPoint.get((row - 1, col + 1), 0)
            paths += pathsToPoint.get((row - 1, col), 0)
            pathsToPoint[(row, col)] = paths

            newPoints.add((row + 1, col))
        pointsToCheck = newPoints
    return sum(pathsToPoint.get((len(data) - 1, col), 0) for col in range(len(data[0])))

# example = [
#     ".......S.......",
#     "...............",
#     ".......^.......",
#     "...............",
#     "......^.^......",
#     "...............",
#     ".....^.^.^.....",
#     "...............",
#     "....^.^...^....",
#     "...............",
#     "...^.^...^.^...",
#     "...............",
#     "..^...^.....^..",
#     "...............",
#     ".^.^.^.^.^...^.",
#     "...............",
# ]
# print(part1(example))
# print(part2(example[:2]))
# print(part2(example[:4]))
# print(part2(example[:6]))
# print(part2(example[:8]))
# print(part2(example[:10]))
# print(part2(example[:12]))
# print(part2(example[:14]))
# print(part2(example))
print(part1())
print(part2())