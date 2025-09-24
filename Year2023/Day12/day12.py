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


def unfold_left(array):
    return array + ['?'] + array + ['?'] + array + ['?'] + array + ['?'] + array


def unfold_right(array):
    return array + array + array + array + array


def resolve_part_1(rows):
    sum = 0
    for row in rows:
        for arrangement in list_arrangement(row[0]):
            if check_arrangement((arrangement, row[1])):
                sum += 1
    return sum


def place_for_block(spring, block):
    for i in range(block):
        if spring[i] == '.':
            return False
    return True


def count_arrangement(springs, blocks, indexBlock):
    if blocks[indexBlock] > len(springs):
        return 0

    for i in range(len(springs)):
        if blocks[indexBlock] > len(springs) - i:
            return 0
        char = springs[i]
        if char == '#':
            if place_for_block(springs[i:], blocks[indexBlock]):
                i += blocks[indexBlock] ### peut-être -1 ou pas ?
                indexBlock += 1
                if indexBlock >= len(blocks):
                    return 1
                continue
            else:
                return 0
        if char == '?':
            return count_arrangement([*springs[i + 1:]], blocks, indexBlock) + count_arrangement(['#', *springs[i+1:]], blocks, indexBlock)



def resolve_part_2(rows):
    unfold_rows = [(unfold_left(row[0]), unfold_right(row[1])) for row in rows]

    for row in unfold_rows:
        springs,blocks = row
        print(count_arrangement(springs, blocks, 0))



if __name__ == "__main__":
    rows = parse_puzzle("puzzle.txt")
    #print(resolve_part_1(rows))
    print(resolve_part_2(rows))


