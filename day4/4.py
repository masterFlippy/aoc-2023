from functools import reduce
f = open('input.txt', 'r')

input = f.read().split('\n')


def solveOne():
    valueDict = {}
    for line in input:
        index = line.index(':')
        cardId = line[0:index]
        rawValues = line[index+1:len(line)]
        pipeIndex = rawValues.index('|')
        winningValues = [x for x in rawValues[0:pipeIndex].strip().split(' ')if x != '']
        myValues = [x for x in rawValues[pipeIndex+1:len(rawValues)].strip().split(' ')if x != '']
        valueDict[cardId] = (winningValues, myValues)

    winningValues = []
    for cardId, value in valueDict.items():
        values = []
        for myValue in valueDict[cardId][1]:
            if myValue in valueDict[cardId][0]:
                values.append(myValue)
        winningValues.append(
        [int(value) for value in values],
        )

    totals = []
    for values in winningValues:
        sum = 0
        for index in range(len(values)):
            if sum == 0:
                sum += 1
            else:
                sum = sum * 2
        totals.append(sum)

    return reduce(lambda x, y: x + y, totals)

print(solveOne())

    