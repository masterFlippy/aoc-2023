f = open('input.txt', 'r')
input = f.read().split('\n')
lines = [[char for char in line] for line in input]

def rotateGrid(grid):
    return [list(row)[::-1] for row in zip(*grid)]


def rollRox(lines):
    for columnIndex in range(len(lines[0])):
        for extra in range(len(lines)):
            for lineIndex in range(len(lines)):
                if lines[lineIndex][columnIndex] == 'O' and lineIndex > 0 and lines[lineIndex - 1][columnIndex] == '.':
                    lines[lineIndex - 1][columnIndex] = 'O'
                    lines[lineIndex][columnIndex] = '.'
    return lines

def solveOne(lines):
    partOneAnswer = 0
    newLines = rollRox(lines)
    for line in range(len(newLines)):
        for index in range(len(newLines[0])):
            if newLines[line][index] == 'O':
                partOneAnswer += len(newLines) - line

    return partOneAnswer

def getSum(lines):
    sum = 0
    for line in range(len(lines)):
        for index in range(len(lines[0])):
            if lines[line][index] == 'O':
                sum += len(lines) - line
    return sum


def solveTwo(lines):
    target = 1000
    iteration = 0
    sum = 0
    while iteration < target:
        iteration += 1
        for i in range(4):
            lines = rollRox(lines)
            lines = rotateGrid(lines)
        sum = getSum(lines)
    return sum



print(solveOne(lines)) 
print(solveTwo(lines))






    