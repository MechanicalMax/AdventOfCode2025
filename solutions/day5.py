with open('input/day5.txt') as f:
    data = f.read().splitlines()

def parse_input(input):
    split_index = input.index("")
    ranges = []
    for line in input[:split_index]:
        start, end = map(int, line.split("-"))
        ranges.append((start, end))
    numbers = list(map(int, input[split_index + 1:]))
    return ranges, numbers

def part1(input = data):
    ranges, numbers = parse_input(input)
    count = 0
    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                count += 1
                break
    return count

example = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]
print(part1(example))
print(part1())