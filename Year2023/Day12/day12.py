from typing import Tuple, List

from Year2023.utils import read_file, split

def parse_puzzle(path:str):
    rows: List[Tuple[str, List[int]]] = []
    for line in read_file(path):
        parts = split(line, ' ')
        left = parts[0]
        right = parts[1]
        nums = [int(x) for x in split(right, ',')]
        rows.append((left, nums))
    return rows

def get_right(springs:str):
    right = []
    damaged = 0
    for i in range(len(springs)):
        if springs[i] == '#':
            damaged +=1
        else:
            if damaged > 0:
                right.append(damaged)
                damaged = 0
    if damaged > 0:
        right.append(damaged)
    return right

def check_arrangement(row: Tuple[str,List[int]]):
    left, right = row
    return right == get_right(left)

if __name__ == "__main__":
    rows = parse_puzzle("puzzle.txt")

    for row in rows:
        print(row)
        print(check_arrangement(row))