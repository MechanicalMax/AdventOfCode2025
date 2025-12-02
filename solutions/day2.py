from math import log10
import re

with open('input/day2.txt') as f:
    lines = f.read().strip()

def createInvalidId(repeatedDigit):
    if repeatedDigit < 1:
        return 11
    return repeatedDigit + (repeatedDigit * 10**int(log10(repeatedDigit)+1))

def part1(rangeString = lines):
    ranges = rangeString.split(',')
    invalidIds = set()
    for r in ranges:
        start, end = map(int, r.split('-'))
        startRepeatedDigit = start // 10**int(log10(start) // 2 + 1)
        currentInvalidId = createInvalidId(startRepeatedDigit)
        while currentInvalidId <= end:
            if currentInvalidId >= start:
                invalidIds.add(currentInvalidId)
            startRepeatedDigit += 1
            currentInvalidId = createInvalidId(startRepeatedDigit)
    return sum(invalidIds)

def part2(rangeString = lines):
    repeatingNumbers = re.compile(r'^(\d+)\1+$')
    ranges = rangeString.split(',')
    fullInvalidIds = set()
    for r in ranges:
        start, end = map(int, r.split('-'))
        for i in range(start, end + 1):
            re.match(repeatingNumbers, str(i)) and fullInvalidIds.add(i) and print(i)
    return sum(fullInvalidIds)

exampleInput = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
# print(part1(exampleInput))
# print(part2(exampleInput))
print(part1())
print(part2())