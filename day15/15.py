import functools


f = open('input.txt', 'r')
input = f.read().replace("\n", "").split(',')
boxes = [[] for i in range(256)]

def calculateItem(item):
    value = 0
    for char in item:
        value += ord(char)
        value = value * 17 
        value = value % 256
    return value


def solveOne(input):
    items = []
    for item in input:
        items.append(calculateItem(item))
    return functools.reduce(lambda a, b: a+b, items)

def solveTwo(input):
    lengths = {}
    for entry in input:
        if('-' in entry):
            label = entry[:-1]
            hashIndex = calculateItem(label)
            if label in boxes[hashIndex]:
                boxes[hashIndex].remove(label)
        else:
            label = entry[:-2]
            focalLength = int(entry[-1])
            hashIndex = calculateItem(label)
            if label not in boxes[hashIndex]:
                boxes[hashIndex].append(label)
            lengths[label] = focalLength

    sum = 0
    for index, entry in enumerate(boxes,1):
        for slotIndex, label in enumerate(entry,1):
            if len(label) > 0:
                print('box:', index, 'slot:', slotIndex, 'length:', lengths[label], 'label:', label)
                sum += index * slotIndex * lengths[label]
    return sum
     

print(solveOne(input))  
print(solveTwo(input))
    