from operator import eq, add
from typing import Callable, List, Dict
from toolz import concat, first, second, frequencies, keyfilter, valmap, itemmap, curry

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
    digits = f.read().strip()

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

# part 2
# result is based on proportion matching our 'atomic' numbers, [1, 4, 7, 8]
# 0 contains 6/7 of 8, all of 1, 3/4 of 4
# 2 contains 5/7 of 8, 1/2 of 1, 2/4 of 4
# 3 contains 5/7 of 8, all of 1, 3/4 of 4
# 5 contains 5/7 of 8, 1/2 of 1, 3/4 of 4
# 6 contains 6/7 of 8, 1/2 of 1, 3/4 of 4
# 9 contains 6/7 of 8, all of 1, all of 4

sort_str = lambda s: "".join(sorted(s))         # sort dict vals
ls_int = lambda ls: int("".join(map(str, ls)))  # turn a list of ints into a concatenated int


def decoder(message: str) -> int:
    inp, out = [s.split() for s in message.split('|')]
    cipher = get_cipher(inp)
    result = ls_int(map(lambda s: cipher[sort_str(s)], out))
    return result


def get_cipher(inp: List[str]) -> Dict[str, int]:
    @curry
    def compare(inp: str, to: int) -> str:
        """get a str containing the proportion of coverage between inp and to. Easier than dealing with floats"""
        overlap = sum(map(lambda s: 1 if s in inp else 0, cipher[to]))
        return f"{overlap}/{len(cipher[to])}"

    def get_atoms(signal_patterns: List[str], cipher: Dict[int, str]):
        """Gets the atoms of matching, 1, 4, 7, 8 and adds them to the cipher"""
        fil = lambda ln: first(filter(lambda s: len(s) == ln, signal_patterns))
        for i in [1, 4, 7, 8]:
            cipher[i] = fil(digi[i])
        return cipher

    cipher = get_atoms(inp, {})

    # use the 'atoms' to match the rest of the strings. Based on proportion
    for s in inp:
        match list(map(compare(s), [1, 4, 8])):
            case ["2/2", "3/4", "6/7"]:  # 0
                cipher[0] = s
            case ["1/2", "2/4", "5/7"]:  # 2
                cipher[2] = s
            case ["2/2", "3/4", "5/7"]:  # 3
                cipher[3] = s
            case ["1/2", "3/4", "5/7"]:  # 5
                cipher[5] = s
            case ["1/2", "3/4", "6/7"]:  # 6
                cipher[6] = s
            case ["2/2", "4/4", "6/7"]:  # 9
                cipher[9] = s

    # sort all the strings in the cipher
    cipher = valmap(sort_str, cipher)
    # swap keys with vals
    cipher = itemmap(reversed, cipher)
    return cipher

# get results
sum(map(decoder, digits.split('\n')))
