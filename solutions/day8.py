import heapq
from collections import Counter

with open('input/day8.txt') as f:
    input = f.read().splitlines()

# Disjoint Set Union (Union-Find) data structure
class DSU:
    def __init__(self, elements):
        self.parent = {e: e for e in elements}
        self.size = {e: 1 for e in elements}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False  # they were already connected

        # union by size
        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA

        # attach smaller tree under larger
        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]
        return True

getPoints = lambda data: [tuple([int(x) for x in line.strip().split(',')]) for line in data]
distanceBetweenPoints = lambda p1, p2: sum([(p1[i] - p2[i])**2 for i in range(3)])

def part1(data = input, K = 1000):
    allPoints = getPoints(data)
    n = len(allPoints)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((distanceBetweenPoints(allPoints[i], allPoints[j]), allPoints[i], allPoints[j]))

    heapq.heapify(edges)

    dsu = DSU(allPoints)

    edges_considered = 0
    while edges_considered < K and edges:
        _, point, otherPoint = heapq.heappop(edges)
        edges_considered += 1
        dsu.union(point, otherPoint)

    comp = Counter(dsu.find(p) for p in allPoints)
    sizes = sorted(comp.values(), reverse=True)

    return sizes[0] * sizes[1] * sizes[2]

example = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]
print(part1(example, 10))
print(part1())