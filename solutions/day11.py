with open('input/day11.txt', 'r') as f:
    input = f.readlines()

def parse(data):
    # creates a directed graph from the input data
    graph = {}
    for line in data:
        node, edges = line.strip().split(': ')
        graph[node] = edges.split(' ')
    return graph

def part1(data = input):
    graph = parse(data)

    # finds all paths from node 'you' to node 'out'
    def dfs(node, visited):
        if node == 'out':
            return 1
        if node in visited:
            return 0
        visited.add(node)
        total_paths = 0
        for neighbor in graph.get(node, []):
            total_paths += dfs(neighbor, visited)
        visited.remove(node)
        return total_paths
    
    return dfs('you', set())

example = [
    "aaa: you hhh",
    "you: bbb ccc",
    "bbb: ddd eee",
    "ccc: ddd eee fff",
    "ddd: ggg",
    "eee: out",
    "fff: out",
    "ggg: out",
    "hhh: ccc fff iii",
    "iii: out",
]

print(part1(example))
print(part1())