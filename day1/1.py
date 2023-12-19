import re
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')

def solveOne(lines):
    sum = 0
    numbers = [list(filter(lambda char: char.isdigit(), subArray)) for subArray in lines]
    for number in numbers:
        if len(number) > 0:
            if len(number) == 1:
                sum += int(number[0]+number[0])
            else:
                sum += int(number[0] + number[len(number)-1])
    return sum

def solveTwo(lines):
    wordNumDict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5':'5',
        '6':'6',
        '7':'7',
        '8':'8',
        '9':'9'

    };
    sum = 0
    for line in lines:
        reversedLine = line[::-1]
        first = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        firstNumber = wordNumDict[first[0]]
        last = re.findall(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', reversedLine)
        lastNumber = wordNumDict[last[0][::-1]]
        print(firstNumber, lastNumber)
        sum += int(firstNumber + lastNumber)
    return sum
        

print(solveTwo(lines))
print(solveOne(lines))
