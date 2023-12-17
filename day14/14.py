f = open('input.txt', 'r')

input = f.read().split('\n')

lines = [[char for char in line] for line in input]

for columnIndex in range(len(lines[0])):
    for extra in range(len(lines)):
        for lineIndex in range(len(lines)):
            if lines[lineIndex][columnIndex] == 'O' and lineIndex > 0 and lines[lineIndex - 1][columnIndex] == '.':
                lines[lineIndex - 1][columnIndex] = 'O'
                lines[lineIndex][columnIndex] = '.'

answer = 0

for line in range(len(lines)):
    for index in range(len(lines[0])):
        if lines[line][index] == 'O':
            answer += len(lines) - line

print(answer)

    