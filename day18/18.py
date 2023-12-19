f = open('input.txt', 'r')
input = f.read().replace(" ", "").split('\n')
lines =  [
    {
        'direction': line.split('(', 1)[0],
        'color': line.split('(', 1)[1][:-1]
    }
    for line in input
]


def calculateInstructions(instructions):
    dir = {"R":(0,1), "D":(1,0), "L":(0,-1), "U":(-1,0)}
    horizontal, vertical, around, inside = 0, 0, 0, 0

    for instruction in instructions:
        direction = instruction[0]
        steps = instruction[1]
        directionVer = dir[direction][0]
        directionHor = dir[direction][1]
        directionVer *= steps
        directionHor *= steps
        vertical += directionVer
        horizontal += directionHor
        around += steps
        inside += horizontal * directionVer

    return inside+around/2 + 1


def getColorInstructions(lines):
    directionDict = {
        0:'R',
        1:'D',
        2:'L',
        3:'U'
    }
    instructions = []
    for line in lines:
        hex = line["color"][1:]
        direction = directionDict[int(hex[5:])]
        steps = int(hex[:5], 16)
        instructions.append((direction, steps))
    return instructions

def solveOne(lines):
    instructions = []
    for line in lines:
        instructions.append((line['direction'][0], int(line['direction'][1:])))
    return calculateInstructions(instructions)

def solveTwo(lines):
    colorInstructions = getColorInstructions(lines)
    return calculateInstructions(colorInstructions)

print(solveOne(lines))
print(solveTwo(lines))





