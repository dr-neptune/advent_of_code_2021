from typing import Tuple

# IO
with open('input.txt') as f:
    lava = f.read()

lv = """2199943210
3987894921
9856789892
8767896789
9899965678"""

cave = np.array([int(c) for c in lv if c != '\n']).reshape(10,5)


def get_adjacent_cell_indices(row: int, col:int, shape: Tuple[int]) -> List[Tuple[int, int]]:
    def neighbors(val, val_max):
        vals = []
        if val == 0:
            vals.append(0)
            vals.append(1)
        elif val == val_max - 1:
            vals.append(row)
            vals.append(row - 1)
        else:
            vals.append(row)
            vals.append(row - 1)
            vals.append(row + 1)
        return vals
    results = []
    rowvals = neighbors(row, shape[0])
    colvals = neighbors(col, shape[1])
    for i in rowvals:
        for j in colvals:
            results.append((i, j))
    return results


get_adjacent_cell_indices(0, 0, cave.shape)



print(get_adjacent_cell_indices(0, 0, cave.shape))

[manhattan_distance((0, 0), i) for i in get_adjacent_cell_indices(0, 1, cave.shape)]

def manhattan_distance(origin: Tuple[int], location: Tuple[int]) -> int:
    return abs(origin[0] - location[0]) + abs(origin[1] - location[1])




print(abs(0 - 1) + abs(0 - 1))
print(abs(0 - 1) + abs(0 - 0))
