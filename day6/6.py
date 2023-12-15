f = open('input.txt', 'r')
import re
from functools import reduce

lines = f.read().split('\n')
valueArray = []

for line in lines:
    index = line.index(':')
    type = line[0:index]
    strValues = re.sub(' +', ' ',line[index+1:len(line)].lstrip().strip()).split(' ')
    numValues = [int(num) for num in strValues]

    valueArray.append({
        type:
        numValues
        })

winningValues = []
for key,value in valueArray[0].items():
    for index, item in enumerate(value):
        waysToWin = 0
        distanceToBeat = valueArray[1]['Distance'][index]
        maxTime = item
        for milliseconds in range(1, maxTime):
            distance = milliseconds * (maxTime - milliseconds)
            if distance > distanceToBeat:
                waysToWin += 1
        winningValues.append(waysToWin)

totalSum = reduce(lambda x, y: x * y, winningValues)
print(totalSum)


