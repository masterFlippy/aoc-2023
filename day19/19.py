from itertools import product


f = open('test.txt', 'r')
input = f.read()
workflows, ratings = input.split('\n\n')
workflows = workflows.split('\n')
ratings = ratings.split('\n')
xmasDict = {
    'x':(1,4000),
    'm':(1,4000),
    'a':(1,4000),
    's':(1,4000)
}


def parseWorkflows(workflows):
    workflowDict = {}
    for workflow in workflows:
        name = workflow.split('{')[0]
        rules = workflow.split('{')[1].split(',')
        lastRule = rules.pop()
        workflowDict[name] = ([], lastRule.replace('}', ''))
        for rule in rules:
            comparison = rule.split(':')[0]
            targetFlow = rule.split(':')[1]
            key = comparison[0]
            operator = comparison[1]
            value = int(comparison[2:])
            workflowDict[name][0].append((key, operator, value, targetFlow))
    return workflowDict

def isAccepted(rating, name = 'in' ):
   if name == 'A':
        return True
   if name == 'R':
        return False
   rules = workflowDict[name][0]
   lastRule = workflowDict[name][1]
   for key, operator, value, targetFlow in rules:
       if eval(str(rating[key]) + operator + str(value)):
           return isAccepted(rating, targetFlow)
   return isAccepted(rating, lastRule)

workflowDict = parseWorkflows(workflows)

def solveOne(ratings):
    total = 0
    for rating in ratings:
        strippedRatingArr = rating[1:-1].split(',')
        ratingDict = {}
        for rating in strippedRatingArr:
            key = rating.split('=')[0]
            value = int(rating.split('=')[1])
            ratingDict[key] = value
        if(isAccepted(ratingDict)):
            total += sum(ratingDict.values())
    return total

print(solveOne(ratings))

def solveTwo(xmasDict, name='in', memo={}):
    if name == 'R':
        return 0
    
    elif name == 'A':
        prod = 1
        for minVal, maxVal in xmasDict.values():
            prod *= maxVal - minVal + 1
        return prod

    if (name, tuple(xmasDict.items())) in memo:
        return memo[(name, tuple(xmasDict.items()))]

    rules = workflowDict[name][0]
    lastRule = workflowDict[name][1]
    sum = 0
    for key, operator, value, targetFlow in rules:
        minVal, maxVal = xmasDict[key]
        trueValues = (minVal, value - 1) if operator == '<' else (value + 1, maxVal)
        falseValues = (value, maxVal) if operator == '<' else (minVal, value)

        rangeDict = xmasDict.copy() if trueValues[0] <= trueValues[1] else xmasDict
        rangeDict[key] = trueValues if trueValues[0] <= trueValues[1] else rangeDict[key]
        sum += solveTwo(rangeDict, targetFlow, memo)

        xmasDict[key] = falseValues if falseValues[0] <= falseValues[1] else xmasDict[key]
        if not (falseValues[0] <= falseValues[1]):
            break
    else:
        sum += solveTwo(xmasDict, lastRule, memo)

    memo[(name, tuple(xmasDict.items()))] = sum
    return sum

print(solveTwo(xmasDict))











