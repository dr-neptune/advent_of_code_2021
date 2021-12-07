from statistics import median

with open('input.txt') as f:
    crabs = [int(i) for i in f.read().split(',')]

excrabs = [16,1,2,0,4,2,7,1,2,14]

boom_point = int(median(crabs))

fuel = 0
for c in crabs:
    fuel += abs(c - boom_point)

print(fuel)

# part 2
