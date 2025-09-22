from typing import Tuple, List

import char

from Year2023.utils import read_file, split

def parse_puzzle(path:str):
    rows: List[Tuple[List[char], List[int]]] = []
    for line in read_file(path):
        parts = split(line, ' ')
        left = parts[0]
        right = parts[1]
        springs = [c for c in left]
        nums = [int(x) for x in split(right, ',')]
        rows.append((springs, nums))
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

def list_arrangement(left):
    # trouver l'index du permier ? et renvoyer les deux possibilités si trouvé
    for i in range(len(left)):
        if left[i] == '?':
            left1 = left
            left1[i] = '.'
            left2 = left
            left2[i] = '#'
            return [left1,left2]
    return left

if __name__ == "__main__":
    rows = parse_puzzle("puzzle.txt")

    print(list_arrangement([".", ".", "?", "."]))

    for row in rows:
        print(row)
        print(check_arrangement(row))