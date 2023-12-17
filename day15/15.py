import functools


f = open('input.txt', 'r')
input = f.read().replace("\n", "").split(',')

items = []

for item in input:
    value = 0
    for char in item:
        value += ord(char)
        value = value * 17 
        value = value % 256
    items.append(value)



print(functools.reduce(lambda a, b: a+b, items))
    