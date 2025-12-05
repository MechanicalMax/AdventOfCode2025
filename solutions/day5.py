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

def part2(input = data):
    ranges, _ = parse_input(input)
    merged_ranges = []
    for start, end in sorted(ranges):
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
    count_covered = lambda ranges: sum(end - start + 1 for start, end in ranges)
    return count_covered(merged_ranges)

# example = [
#     "3-5",
#     "10-14",
#     "16-20",
#     "12-18",
#     "",
#     "1",
#     "5",
#     "8",
#     "11",
#     "17",
#     "32",
# ]
# print(part1(example))
# print(part2(example))
print(part1())
print(part2())