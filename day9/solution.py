import numpy as np
from operator import lt
from typing import Tuple, List

# IO
with open('input.txt') as f:
    lava = f.read()

lava_shape = len(lava.split('\n')[0])

cave = np.array([int(c) for c in lava if c != '\n']).reshape(lava_shape, lava_shape)

def manhattan_distance(origin: Tuple[int], location: Tuple[int]) -> int:
    return abs(origin[0] - location[0]) + abs(origin[1] - location[1])

def get_adjacent_cell_indices(row: int, col:int, shape: Tuple[int], plus_only: bool = True) -> List[Tuple[int, int]]:
    def neighbors(val, val_max):
        vals = []
        if val == 0:
            vals.append(0)
            vals.append(1)
        elif val == val_max - 1:
            vals.append(val)
            vals.append(val - 1)
        else:
            vals.append(val)
            vals.append(val - 1)
            vals.append(val + 1)
        return vals
    results = []
    rowvals = neighbors(row, shape[0])
    colvals = neighbors(col, shape[1])
    for i in rowvals:
        for j in colvals:
            results.append((i, j))
    if plus_only:
        results = [i for i in results if manhattan_distance((row, col), i) < 2 and i != (row, col)]
    return results

# check if all the adjacents are higher than the current spot
low_points = []
for irow, icol in np.ndindex(cave.shape):
    results = get_adjacent_cell_indices(irow, icol, cave.shape)
    if all(map(lambda x: lt(cave[irow, icol], x), [cave[i[0], i[1]] for i in results])):
        low_points.append(cave[irow, icol])

sum([i + 1 for i in low_points])

# part 2
