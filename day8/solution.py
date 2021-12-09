from typing import Callable, List
from toolz import concat, first, second, frequencies, keyfilter

digi = {0: 6,
        1: 2,  #
        2: 5,
        3: 5,
        4: 4,  #
        5: 5,
        6: 6,
        7: 3,  #
        8: 7,  #
        9: 6}

with open("input.txt") as f:
    digits = f.read()

# part 1
def input_format(input_str: str, num_part: Callable = second) -> List[str]:
    return list(map(lambda s: num_part(s).split(),
                         map(lambda s: s.split("|"), input_str.split("\n"))))


def len_counts(length: int, values: List[List[str]]):
    return sum(keyfilter(lambda x: len(x) == length,
                         frequencies(
                             map(lambda s: "".join(sorted(s)),
                                 concat(values)))).values())


output_values = input_format(digits)

print(sum(map(lambda v: len_counts(v, output_values), [digi[1], digi[4], digi[7], digi[8]])))
