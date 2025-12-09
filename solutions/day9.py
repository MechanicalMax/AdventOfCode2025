import heapq
from collections import Counter

with open('input/day9.txt') as f:
    input = f.read().splitlines()
    
getPoints = lambda data: [tuple([int(x) for x in line.strip().split(',')]) for line in data]
areaBetweenPoints = lambda p1, p2: (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)

def part1(data = input):
    allPoints = getPoints(data)
    n = len(allPoints)

    maxArea = 0
    maxPoints = (None, None)
    for i in range(n):
        for j in range(i + 1, n):
            maxArea = max(maxArea, areaBetweenPoints(allPoints[i], allPoints[j]))

    return maxArea

example = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3",
]
print(part1(example))
print(part1())