import numpy as np
import numpy.ma as ma
from typing import List, Tuple
import re

# IO
with open('input.txt') as f:
    bingo = f.read()


bingo_list = bingo.split('\n\n')
numbers = [int(i) for i in bingo_list[0].split(',')]
boards = [to_np_array(b) for b in bingo_list[1:]]


def to_np_array(board: str) -> np.array:
    # replace double space
    board = (board
             .replace('  ', ' ')
             .replace('\n ', '\n')
             .strip())
    # split twice, coerce to int, and then place in a 2d array
    return np.array([list(map(int, i)) for i in
                     [line.split(' ') for line in board.split('\n')]])


def index(array, item):
    for idx, val in np.ndenumerate(array):
        if val == item:
            return idx


def get_wins(numbers: List[int], boards: List[np.array]):
    def check_boards(boards: List[np.array], number: int, check_cards: List[np.array]):
        for board, card in zip(boards, check_cards):
            found = index(board, number)
            if found:
                card[found[0], found[1]] = 1
                if card[found[0], :].sum() == 5:
                    print(f'Winner! {num} on board {board} and card {card}')
                    return num, board, card
                if card[:, found[1]].sum() == 5:
                    print(f'Winner! {num} on board {board} and card {card}')
                    return num, board, card
        return
    # make blank score cards
    check_cards = [np.zeros((5, 5)) for _ in boards]
    for num in numbers:
        try:
            num_out, board_out, card_out = check_boards(boards, num, check_cards)
            break
        except Exception:
            continue
    # now get the result
    board_sum = ma.masked_array(board_out, mask=card_out).sum()
    return board_sum * num_out

get_wins(numbers, boards)


# part 2
def get_wins(numbers: List[int], boards: List[np.array]):
    def check_boards(boards: List[np.array], number: int, check_cards: List[np.array]):
        for board, card in zip(boards, check_cards):
            found = index(board, number)
            if found:
                card[found[0], found[1]] = 1
                if card[found[0], :].sum() == 5:
                    print(f'Winner! {num} on board {board} and card {card}')
                    return num, board, card
                if card[:, found[1]].sum() == 5:
                    print(f'Winner! {num} on board {board} and card {card}')
                    return num, board, card
        return
    # make blank score cards
    check_cards = [np.zeros((5, 5)) for _ in boards]
    for num in numbers:
        print(len(boards))
        try:
            num_out, board_out, card_out = check_boards(boards, num, check_cards)
            boards = [b for b in boards if not np.array_equal(b, board_out)]
            board_sum = ma.masked_array(board_out, mask=card_out).sum()
            print(board_sum * num_out)
        except Exception:
            continue
    # now get the result
    board_sum = ma.masked_array(board_out, mask=card_out).sum()
    return board_sum * num_out

get_wins(numbers, boards)


example = boards[50]
print(example)

print([np.array_equal(example, x) for x in boards].index(True))
