# solution with python 3.10
from typing import List
from toolz import first, second, drop
import sys
# Ouroboros should be ashamed of python's recursion limit being 1000
sys.setrecursionlimit(5000)

# io
with open('input.txt') as f:
    cmds = f.read().splitlines()

# part 2
def dive(commands: List[str], position: int = 0, depth: int = 0, aim: int = 0) -> int:
    structure = lambda ls: [first(ls), int(second(ls))]  # ['text', 'text'] -> ['text', int]
    if len(commands) == 0:
        return position * depth
    else:
        rest_cmds = list(drop(1, commands))
        match structure(first(commands).split()):
            case ['forward', mag]:
                return dive(rest_cmds, position+mag, depth+(aim*mag), aim)
            case ['down', mag]:
                return dive(rest_cmds, position, depth, aim+mag)
            case ['up', mag]:
                return dive(rest_cmds, position, depth, aim-mag)
            case _:
                raise ValueError

dive(cmds)
