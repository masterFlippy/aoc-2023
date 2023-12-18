f = open('input.txt', 'r')
input = f.read().replace(" ", "").split('\n')
lines =  [
    {
        'direction': line.split('(', 1)[0],
        'color': line.split('(', 1)[1][:-1]
    }
    for line in input
]
dir = {"R":(0,1), "D":(1,0), "L":(0,-1), "U":(-1,0)}
instructions = []
horizontal, vertical, around, inside = 0, 0, 0, 0

for lineIndex,line in enumerate(lines):
    instructions.append((line['direction'][0], int(line['direction'][1:])))

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

print(inside+around/2 + 1)


