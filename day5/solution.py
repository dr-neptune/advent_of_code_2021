import numpy as np
import pandas as pd
from toolz import pluck, concat
from typing import List


# IO
with open('input.txt') as f:
    lines = f.read().splitlines()


# form into lists like ([491, 392], [34, 392]) where ([x1, y1], [x2, y2])
lines_in = []
for line in lines:
    a, b = list(map(lambda s: list(map(int, s.strip().split(','))), line.split('->')))
    lines_in.append((a, b))


# we want the dimensions of the table
max_x = max(concat([pluck(0, i) for i in lines_in]))
max_y = max(concat([pluck(1, i) for i in lines_in]))


# make a blank grid
grid = np.zeros((max_x + 1, max_y + 1))


# consider only horizontal and vertical lines, x1 = x2 or y1 = y2
df = pd.DataFrame([a + b for a, b in lines_in], columns=['x1', 'y1', 'x2', 'y2'])
vertical = df.query('x1 == x2')
horizontal = df.query('y1 == y2')


# add the vertical, horizontal lines to the grid
for row in vertical.iterrows():
    xrange = row[1]['x1']
    a, b = sorted([row[1]['y1'], row[1]['y2']])
    yrange = range(a, b + 1)
    for i in yrange:
        grid[xrange, i] += 1


for row in horizontal.iterrows():
    yrange = row[1]['y1']
    a, b = sorted([row[1]['x1'], row[1]['x2']])
    xrange = range(a, b + 1)
    for i in xrange:
        grid[i, yrange] += 1


# now get all the points which are > 1
len(np.argwhere(grid > 1))


# part 2
def equiv_distances(row: pd.Series) -> bool:
    """
    2 lines fall on a 45 degree diagonal iff abs(dist(x)) == abs(dist(y))
    """
    return abs(row['x1'] - row['x2']) == abs(row['y1'] - row['y2'])


def inc_dec(row: pd.Series) -> List[str]:
    """Returns whether x, y incremented or decremented between x1,x2 and y1,y2"""
    delta = []
    if row['x1'] < row['x2']:
        delta.append('inc')
    else:
        delta.append('dec')
    if row['y1'] < row['y2']:
        delta.append('inc')
    else:
        delta.append('dec')
    return delta


diagonal = df[df.apply(equiv_distances, axis=1)]
diagonal['delta'] = diagonal.apply(inc_dec, axis=1)


# now iterate over the grid
# if increasing x, increasing y then a -> +1, +1 -> b  | 1,1 -> 2,2 -> 3,3
# if decreasing x, increasing y, then a -> -1, +1 -> b | 9,7 -> 8,8 -> 7,9
# if increasing x, decreasing y, then a -> +1, -1 -> b | 5,5 -> 6,4 -> 7,3
# if decreasing x, decreasing y, then a -> -1, -1 -> b | 5,5 -> 4,4 -> 3,3
for row in diagonal.iterrows():
    x, y, endx, endy, _ = row[1]
    match row[1]['delta']:
        case ['inc', 'inc']:
            while x < endx + 1 and y < endy + 1:
                grid[x, y] += 1
                x += 1
                y += 1
        case ['dec', 'inc']:
            while x > endx - 1 and y < endy + 1:
                grid[x, y] += 1
                x -= 1
                y += 1
        case ['inc', 'dec']:
            while x < endx + 1 and y > endy - 1:
                grid[x, y] += 1
                x += 1
                y -= 1
        case ['dec', 'dec']:
            while x > endx - 1 and y > endy - 1:
                grid[x, y] += 1
                x -= 1
                y -= 1


# result
len(np.argwhere(grid > 1))
