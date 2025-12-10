from collections import deque

with open('input/day10.txt') as f:
    input = f.readlines()

def parseInputLines(data):
    machines = []
    for line in data:
        lights = line.split(' ')[0][1:-1]
        buttons = tuple(map(lambda l: tuple(map(int, l.strip("()\n").split(','))), line.split(' ')[1:-1]))
        unknown = tuple(line.split(' ')[-1].strip("{}\n").split(','))
        machines.append((lights, buttons, unknown))
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

example = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
]

print(part1(example))
print(part1())