import pulp
from collections import deque

with open('input/day10.txt') as f:
    input = f.readlines()

def parseInputLines(data):
    machines = []
    for line in data:
        lights = line.split(' ')[0][1:-1]
        buttons = tuple(map(lambda l: tuple(map(int, l.strip("()\n").split(','))), line.split(' ')[1:-1]))
        joltages = list(map(int, line.split(' ')[-1].strip("{}\n").split(',')))
        machines.append((lights, buttons, joltages))
    return machines

def part1(data = input):
    machines = parseInputLines(data)
    fewestPresses = []

    for machine in machines:
        lights, buttons, _ = machine
        # Simulate button presses with BFS
        queue = deque([("."*len(lights), 0)])
        foundShortest = False
        while not foundShortest and queue:
            current_lights, presses = queue.popleft()
            for button in buttons:
                new_lights = list(current_lights)
                for index in button:
                    new_lights[index] = '#' if new_lights[index] == '.' else '.'
                new_lights_str = ''.join(new_lights)
                if new_lights_str == lights:
                    fewestPresses.append(presses + 1)
                    foundShortest = True
                    break
                queue.append((new_lights_str, presses + 1))

    return sum(fewestPresses)

def min_integer_sum(A, b):
    """
    Minimize sum(x_i) subject to A x = b and x_i >= 0 integers.

    Parameters
    ----------
    A : list[list[int]]
        Coefficient matrix (m x n)
    b : list[int]
        Right-hand side values (length m)

    Returns
    -------
    int
        Minimum achievable sum of all variables
    """
    m = len(A)
    n = len(A[0])

    prob = pulp.LpProblem("Minimize_Sum", pulp.LpMinimize)

    # Decision variables: nonnegative integers
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(n)]

    # Objective: minimize sum of variables
    prob += pulp.lpSum(x)

    # Constraints: A x = b
    for i in range(m):
        prob += pulp.lpSum(A[i][j] * x[j] for j in range(n)) == b[i]

    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if prob.status != pulp.LpStatusOptimal:
        raise ValueError("No feasible integer solution exists")

    return sum(int(pulp.value(v)) for v in x)

def part2(data = input):
    machines = parseInputLines(data)
    fewestPresses = 0

    for machine in machines:
        _, buttons, joltages = machine
        A = []
        for i in range(len(joltages)):
            row = []
            for button in buttons:
                row.append(1 if i in button else 0)
            A.append(row)
        b = joltages
        fewestPresses += min_integer_sum(A, b)

    return fewestPresses

example = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]

# print(part1(example))
# print(part2(example))
print(part1())
print(part2())