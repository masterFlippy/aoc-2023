f = open('input.txt', 'r')
import re
from functools import reduce

lines = f.read().split('\n')
part1Arr = []
part2Arr = []

for line in lines:
    index = line.index(':')
    type = line[0:index]
    part1StrValues = re.sub(' +', ' ',line[index+1:len(line)].lstrip().strip()).split(' ')
    part1NumValues = [int(num) for num in part1StrValues]
    part2StrValues = "".join(line[index+1:len(line)].split())
    part2NumValue = int(part2StrValues)

    part1Arr.append({
        type:
        part1NumValues
        })
    part2Arr.append({
        type:
        part2NumValue
        })

winningValues = []
for key,value in part1Arr[0].items():
    for index, item in enumerate(value):
        waysToWin = 0
        distanceToBeat = part1Arr[1]['Distance'][index]
        maxTime = item
        for milliseconds in range(1, maxTime):
            distance = milliseconds * (maxTime - milliseconds)
            if distance > distanceToBeat:
                waysToWin += 1
        winningValues.append(waysToWin)

part2TotalSum = 0
part2DistanceToBeat = part2Arr[1]['Distance']
part2MaxTime = part2Arr[0]['Time']
for milliseconds in range(1, part2MaxTime):
    distance = milliseconds * (part2MaxTime - milliseconds)
    if distance > part2DistanceToBeat:
        part2TotalSum += 1
        
part1TotalSum = reduce(lambda x, y: x * y, winningValues)


print('part1:', part1TotalSum)
print('part2:', part2TotalSum)



