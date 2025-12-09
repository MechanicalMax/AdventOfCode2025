from shapely.geometry import Polygon, box
from shapely.prepared import prep
from itertools import combinations

with open('input/day9.txt') as f:
    input = f.read().splitlines()
    
getPoints = lambda data: [tuple([int(x) for x in line.strip().split(',')]) for line in data]
areaBetweenPoints = lambda p1, p2: (abs(p1[0] - p2[0])+1) * (abs(p1[1] - p2[1])+1)

def part1(data = input):
    allPoints = getPoints(data)
    n = len(allPoints)

    maxArea = 0
    for i in range(n):
        for j in range(i + 1, n):
            maxArea = max(maxArea, areaBetweenPoints(allPoints[i], allPoints[j]))

    return maxArea

def part2(data=input):
    pts = getPoints(data)
    poly = Polygon(pts)
    poly_prep = prep(poly)   # speed for O(n^2) tests

    max_area = 0

    for (x1,y1),(x2,y2) in combinations(pts,2):
        xmin,xmax = sorted([x1,x2])
        ymin,ymax = sorted([y1,y2])

        rect = box(xmin,ymin,xmax,ymax)

        if poly_prep.covers(rect):  # inclusive boundary test
            area = (xmax-xmin+1)*(ymax-ymin+1)
            max_area = max(max_area, area)

    return max_area

# example = [
#     "7,1",
#     "11,1",
#     "11,7",
#     "9,7",
#     "9,5",
#     "2,5",
#     "2,3",
#     "7,3",
# ]
# print(part1(example))
# print(part2(example))
print(part1())
print(part2())