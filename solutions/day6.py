from functools import reduce

with open('input/day6.txt') as f:
    input = f.readlines()

def parse_data(data):
    numbers = data[:-1]
    parsed_numbers = [list(map(int, line.split())) for line in numbers]
    operations = data[-1].strip().split()
    return parsed_numbers, operations

def part1(data = input):
    parsed_numbers, operations = parse_data(data)
    total_sum = 0
    for i in range(len(operations)):
        if operations[i] == '*':
            total_sum += reduce(lambda x, y: x * y, [parsed_numbers[j][i] for j in range(len(parsed_numbers))])
        elif operations[i] == '+':
            total_sum += sum([parsed_numbers[j][i] for j in range(len(parsed_numbers))])
    return total_sum

def part2(data = input):
    colIndex = len(data[0]) - 1
    totalSum = 0
    currentColNumbers = []
    while colIndex >= 0:
        colNumber = 0
        rowIndex = 0
        while rowIndex < len(data) - 1:
            try:
                cellNumber = int(data[rowIndex][colIndex])
                colNumber = colNumber * 10 + cellNumber
            except ValueError:
                pass
            rowIndex += 1
        currentColNumbers.append(colNumber)
        if data[rowIndex][colIndex] == '*':
            totalSum += reduce(lambda x, y: x * y, currentColNumbers)
            currentColNumbers = []
            colIndex -= 2
        elif data[rowIndex][colIndex] == '+':
            totalSum += sum(currentColNumbers)
            currentColNumbers = []
            colIndex -= 2
        else:
            colIndex -= 1
    return totalSum

# example = [
#     "123 328  51 64 ",
#     " 45 64  387 23 ",
#     "  6 98  215 314",
#     "*   +   *   +  ",
# ]
# print(part1(example))
# print(part2(example))
print(part1())
print(part2())