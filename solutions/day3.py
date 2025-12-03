with open(r'input/day3.txt') as f:
    input = f.read().splitlines()

def part1(data = input):
    joltageSum = 0
    for line in data:
        currentMaxValue = 11
        for startIndex in range(len(line)):
            startValue = line[startIndex]
            for nextIndex in range(startIndex + 1, len(line)):
                nextValue = line[nextIndex]
                potentialJoltage = (int(startValue) * 10) + int(nextValue)
                if potentialJoltage > currentMaxValue:
                    currentMaxValue = potentialJoltage
        joltageSum += currentMaxValue
    return joltageSum

def part2(data = input):
    joltageSum = 0
    for line in data:
        # print(line)
        currentMaxJoltage = 0
        startSearchIndex = 0
        endSearchIndex = len(line) - 11
        # print(line[startSearchIndex:endSearchIndex])
        for _ in range(12):
            # Find Max in smaller window
            currentMaxValue = 0
            # print(f"Searching indexes {startSearchIndex} to {endSearchIndex}: {line[startSearchIndex:endSearchIndex]}")
            for curSearchIndex in range(startSearchIndex, endSearchIndex):
                startValue = line[curSearchIndex]
                if int(startValue) > currentMaxValue:
                    currentMaxValue = int(startValue)
                    startSearchIndex = curSearchIndex + 1
            currentMaxJoltage = (currentMaxJoltage * 10) + currentMaxValue
            endSearchIndex += 1
        # print(f"Line: {line} - MaxJoltage: {currentMaxJoltage}")
        joltageSum += currentMaxJoltage
    return joltageSum
    

# example = [
#     "987654321111111",
#     "811111111111119",
#     "234234234234278",
#     "818181911112111",
# ]
# print(part1(example))
# print(part2(example))
print(part1())
print(part2())