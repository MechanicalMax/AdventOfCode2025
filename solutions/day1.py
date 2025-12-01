with open(r"input\day1.txt", 'r') as f:
    inputLines = f.readlines()

def part1(lines=inputLines):
    start = 50
    atZeroCount = 0
    for line in lines:
        direction = 1 if line[0] == "R" else -1
        change = int(line[1:]) * direction
        start += change
        start %= 100
        if start == 0:
            atZeroCount += 1
    return atZeroCount

def part2(lines=inputLines):
    curPos = 50
    zeroCount = 0
    for line in lines:
        if line[0] == "R":
            for _ in range(int(line[1:])):
                curPos += 1
                curPos %= 100
                if curPos == 0:
                    zeroCount += 1
        else:
            for _ in range(int(line[1:])):
                curPos -= 1
                curPos %= 100
                if curPos == 0:
                    zeroCount += 1
    return zeroCount

# example=["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
# print(part1(example))
# print(part2(example))
print(part1())
print(part2())