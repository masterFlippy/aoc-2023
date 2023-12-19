from functools import reduce
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')

gameDict = {}
for line in lines:
    gameId, values = line.split(':')
    values = [element.strip() for element in values.replace(';', ',').split(',')]
    gameDict[gameId.strip()] = values


def solveOne(lines):
    maxValues = {
        'blue': 14,
        'green': 13,
        'red': 12,
    }

    approvedGames = []
    for gameId, values in gameDict.items():
        gameNumber = int(gameId.split(' ')[1])
        isApproved = True;
        for value in values:
            count, color = value.split(' ')
            if int(count) > maxValues[color]:
                isApproved = False
        if isApproved:
            approvedGames.append(gameNumber)
    return reduce(lambda x, y: x + y, approvedGames)


def solveTwo(lines):
    minimumSets = []
    for _, values in gameDict.items():
        maxValueDict = {}
        for value in values:
            count, color = value.split(' ')
            count = int(count)
            if color not in maxValueDict or count > maxValueDict[color]:
                maxValueDict[color] = count
        minimumSets.append(
            reduce(lambda x, y: x * y, maxValueDict.values())
        )
    return reduce(lambda x, y: x + y, minimumSets)

            

print(solveOne(lines))
print(solveTwo(lines))