from numpy import sign
from toolz import sliding_window
from typing import List, Callable
from operator import gt

# IO
with open('input.txt') as f:
    depths = [int(i) for i in f.read().splitlines()]

def chunked_operation(op_fn: Callable, support: List[int], chunk_size: int) -> List[int]:
    """
    Given a list, break it into chunk_size chunks and apply the op_fn to each chunk
    """
    chunks = sliding_window(chunk_size, support)
    return map(op_fn, chunks)

sgn_tuple_fn = lambda tup: sign(tup[1] - tup[0])  # return the sign of the difference of a 2-tuple [-1, 0, 1]
get_sgn_list = lambda support: chunked_operation(sgn_tuple_fn, support, 2)
triple_sums = chunked_operation(sum, depths, 3)

if __name__ == '__main__':
    # solution for part 1
    sum([x for x in get_sgn_list(depths) if gt(x, 0)])
    # solution for part 2
    sum([x for x in get_sgn_list(triple_sums) if gt(x, 0)])
