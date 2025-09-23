from typing import Tuple, List

import char

from Year2023.utils import read_file, split


def parse_puzzle(path: str):
    rows: List[Tuple[List[char], List[int]]] = []
    for line in read_file(path):
        parts = split(line, ' ')
        left = parts[0]
        right = parts[1]
        springs = [c for c in left]
        nums = [int(x) for x in split(right, ',')]
        rows.append((springs, nums))
    return rows


def get_right(springs: str):
    right = []
    damaged = 0
    for i in range(len(springs)):
        if springs[i] == '#':
            damaged += 1
        else:
            if damaged > 0:
                right.append(damaged)
                damaged = 0
    if damaged > 0:
        right.append(damaged)
    return right


def check_arrangement(row: Tuple[str, List[int]]):
    left, right = row
    return right == get_right(left)


def list_arrangement(left):
    try:
        i = left.index('?')
        return list_arrangement([*left[:i], '.', *left[i + 1:]]) + list_arrangement([*left[:i], '#', *left[i + 1:]])
    except ValueError:
        return [left]


if __name__ == "__main__":
    rows = parse_puzzle("puzzle.txt")

    sum = 0
    for row in rows:
        for arrangement in list_arrangement(row[0]):
            if check_arrangement((arrangement, row[1])):
                sum += 1
    print(sum)
