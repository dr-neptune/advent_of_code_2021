import numpy as np
from typing import Tuple, List

# make a step
def step(state: np.ndarray) -> np.ndarray:
    # keep track of flashes
    total_flashes = 0
    flashes = []
    def flash(r: int, c: int):
        nonlocal total_flashes
        state[r, c] = 0
        adjacents = get_adjacent_cell_indices(r, c, state.shape)
        total_flashes += 1
        for a in adjacents:
            value = state[a[0], a[1]]
            if value < 9:
                state[a[0], a[1]] += 1
            else:
                flashes.append((a[0], a[1]))
                flash(a[0], a[1])
    # increment state
    state += 1
    # check for flash points
    row, col = np.where(state > 9)
    # turn row, col into flash points (i, j)
    flash_points = [(i, j) for i, j in zip(row, col)]
    # for each flash point, ignite it
    for point in flash_points:
        r, c = point[0], point[1]
        if state[r, c] <= 9:
            continue
        else:
            flashes.append((r, c))
            flash(r, c)
        for f in flashes:
            state[f[0], f[1]] = 0
    return state, total_flashes


# get neighbors in a 2D array
def get_adjacent_cell_indices(row: int, col: int, shape: Tuple[int]) -> List[Tuple[int, int]]:
    def neighbors(value, val_max):
        output = []
        # handle values on the edge of the board
        if value == 0:
            output.append(0)
            output.append(1)
        elif value == val_max - 1:
            output.append(val_max - 2)
            output.append(val_max - 1)
        # handle values with at least a 1 cell buffer
        else:
            output.append(value)
            output.append(value - 1)
            output.append(value + 1)
        return output
    # get
    result = []
    rowvals = neighbors(row, shape[0])
    colvals = neighbors(col, shape[1])
    for i in rowvals:
        for j in colvals:
            result.append((i, j))
    return result

if __name__ == '__main__':

    # IO
    with open('input.txt') as f:
        board = f.read().strip()

    board = np.array([int(c) for c in board if c != '\n']).reshape(10,10)

    all_flashes = 0
    iters = 100
    for i in range(100):
        board, total = step(board)

        # check for all flashing at once (part 2 solution)
        if sum(sum(board)) == 0:
            print(f'The iteration is: {i + 1}')
            break

        all_flashes += total

    # part 1 solution
    print(f"The total number of flashes for {iters} iterations is {all_flashes}")
