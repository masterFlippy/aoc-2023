from functools import reduce
f = open('input.txt', 'r')
input = f.read().split('\n')

valueDict = {}
for line in input:
    index = line.index(':')
    cardId = line[0:index]
    rawValues = line[index+1:len(line)]
    pipeIndex = rawValues.index('|')
    winningValues = [x for x in rawValues[0:pipeIndex].strip().split(' ')if x != '']
    myValues = [x for x in rawValues[pipeIndex+1:len(rawValues)].strip().split(' ')if x != '']
    valueDict[cardId] = (winningValues, myValues)

def solveOne():
    winningValues = []
    for cardId, _ in valueDict.items():
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
        for _ in range(len(values)):
            if sum == 0:
                sum += 1
            else:
                sum = sum * 2
        totals.append(sum)

    return reduce(lambda x, y: x + y, totals)

def solveTwo():
    winningValues = []
    for index, value in enumerate(valueDict.values()):
        length = len([myValue for myValue in value[1] if myValue in value[0]])
        winningValues.append({
            'cardId': index,
            'winningValues': length,
            'processed': False,
        })


    idx = 0

    while idx < len(winningValues):
        cardIndex = winningValues[idx]['cardId']
        for i in range(winningValues[idx]['winningValues']):
            winningValues.append({
                'cardId': winningValues[cardIndex + i + 1]['cardId'],
                'winningValues': winningValues[cardIndex + i + 1]['winningValues'],
                'processed': False,
            })
        
        winningValues[idx]['processed'] = True
        idx += 1
    return len(winningValues)


print(solveOne())
print(solveTwo())

    