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

def part2(data = input):
    graph = parse(data)
    # build nodes from keys and neighbors
    nodes = set(graph.keys())
    for neighs in graph.values():
        for n in neighs:
            nodes.add(n)

    if 'svr' not in nodes or 'out' not in nodes:
        return 0

    node_list = list(nodes)
    idx = {n: i for i, n in enumerate(node_list)}
    n_nodes = len(node_list)
    adj = [[] for _ in range(n_nodes)]
    for u, neighs in graph.items():
        ui = idx[u]
        for v in neighs:
            vi = idx[v]
            adj[ui].append(vi)

    # topological sort (assume DAG)
    indeg = [0] * n_nodes
    for u in range(n_nodes):
        for v in adj[u]:
            indeg[v] += 1
    q = [i for i, d in enumerate(indeg) if d == 0]
    topo = []
    qi = 0
    while qi < len(q):
        u = q[qi]; qi += 1
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    start = idx['svr']
    out_i = idx['out']

    dp_from = [0] * n_nodes
    dp_from[start] = 1
    for u in topo:
        cu = dp_from[u]
        if not cu:
            continue
        for v in adj[u]:
            dp_from[v] += cu

    dp_to = [0] * n_nodes
    dp_to[out_i] = 1
    for u in reversed(topo):
        for v in adj[u]:
            dp_to[u] += dp_to[v]

    pos = {node: i for i, node in enumerate(topo)}
    def paths_between(src, dst):
        dp = [0] * n_nodes
        dp[src] = 1
        for u in topo[pos[src]:]:
            if dp[u] == 0:
                continue
            for v in adj[u]:
                dp[v] += dp[u]
        return dp[dst]

    required = ['dac', 'fft']
    if any(r not in idx for r in required):
        return 0
    a = idx[required[0]]
    b = idx[required[1]]
    pab = paths_between(a, b)
    pba = paths_between(b, a)
    return dp_from[a] * pab * dp_to[b] + dp_from[b] * pba * dp_to[a]

# example = [
#     "aaa: you hhh",
#     "you: bbb ccc",
#     "bbb: ddd eee",
#     "ccc: ddd eee fff",
#     "ddd: ggg",
#     "eee: out",
#     "fff: out",
#     "ggg: out",
#     "hhh: ccc fff iii",
#     "iii: out",
# ]
# example2 = [
#     "svr: aaa bbb",
#     "aaa: fft",
#     "fft: ccc",
#     "bbb: tty",
#     "tty: ccc",
#     "ccc: ddd eee",
#     "ddd: hub",
#     "hub: fff",
#     "eee: dac",
#     "dac: fff",
#     "fff: ggg hhh",
#     "ggg: out",
#     "hhh: out",
# ]
# print(part1(example))
# print(part2(example2))
print(part1())
print(part2())