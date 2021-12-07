from statistics import median

with open('input.txt') as f:
    crabs = [int(i) for i in f.read().split(',')]

boom_point = int(median(crabs))

fuel = 0
for c in crabs:
    fuel += abs(c - boom_point)

print(fuel)

# part 2, brute force
fuels = {}
for i in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for c in crabs:
        # calculate distances
        n = abs(c - i)
        fuel += int((n * (n + 1)) / 2)
    fuels[i] = fuel

print(min(fuels.values()))

# part 3: mean girls edition
from statistics import mean
from math import floor

central_point = floor(mean(crabs) - 1/2)

fuel = 0
for c in crabs:
    n = abs(c - central_point)
    fuel += int((n * (n + 1)) / 2)
print(fuel)
