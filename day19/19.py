f = open('input.txt', 'r')
input = f.read()
workflows, ratings = input.split('\n\n')
workflows = workflows.split('\n')
ratings = ratings.split('\n')

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




