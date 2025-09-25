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

def unfold_left(array):
    return array + ['?'] + array + ['?'] + array + ['?'] + array + ['?'] + array

def unfold_right(array):
    return array + array + array + array + array

def resolve_part_1(rows):
    sum = 0
    for row in rows:
        memo = {}
        sum+= count_arrangement(memo, row, 0, 0)
    return sum

def place_for_block(row, position, block_index):
    spring, block = row
    block_size = block[block_index]
    for i in range(position, position + block_size):
        if spring[i] == '.':
            return False
    if position + block_size < len(spring):
        if spring[position + block_size] == '#':
            return False
    return True

def no_more_broken(springs : List[char], position : int):
    for spring in springs[position:]:
        if spring == '#':
            #print("Il reste un broken, raté")
            return 0
    return 1


def count_arrangement(memo, row, position, block_index):
    if (position, block_index) in memo:
        return memo[(position, block_index)]

    springs, blocks = row

    #Si on a parcouru tous les springs, on vérifie qu'on a placé tous les blocs
    if position >= len(springs):
        if block_index >= len(blocks):
            memo[(position, block_index)] = 1
            return 1
        else:
            memo[(position, block_index)] = 0
            return 0

    #Si on a placé tous les blocs, on vérifie qu'il ne reste plus de broken springs
    if block_index >= len(blocks):
        result = no_more_broken(springs, position)
        memo[(position, block_index)] = result
        return result

    #On vérifie qu'il reste suffisamment de place pour tous les blocs restants (Sum = nombre de brokens à placer ; en ajoutant les '.' minimaux entre chaque groupe de brokens
    if sum(blocks[block_index:]) + len(blocks) - 1 - block_index > len(springs) - position:
        memo[(position, block_index)] = 0
        return 0

    #Si '.' on regarde le spring suivant
    if springs[position] == '.':
        return count_arrangement(memo, row, position + 1, block_index)

    #Si # on regarde après le bloc de '#' suivi de '.'
    if springs[position] == '#':
        if place_for_block(row, position, block_index):
            return count_arrangement(memo, row, position + blocks[block_index] + 1, block_index + 1)
        else:
            memo[(position, block_index)] = 0
            return 0

    #Si '?' on additionne les deux arrangements possibles.
    if springs[position] == '?':
        if place_for_block(row, position, block_index):
            return count_arrangement(memo, row, position + 1, block_index) + count_arrangement(memo, row, position + blocks[block_index] + 1, block_index + 1)
        else:
            return count_arrangement(memo, row, position + 1, block_index)

def resolve_part_2(rows):
    unfold_rows = [(unfold_left(row[0]), unfold_right(row[1])) for row in rows]
    sum = 0
    for i in range(len(unfold_rows)):
        memo = {}
        s = count_arrangement(memo, unfold_rows[i], 0, 0)
        print(f"ligne {i} = {s}")
        sum += s
    return sum

if __name__ == "__main__":
    rows = parse_puzzle("puzzle.txt")
    print(resolve_part_1(rows))
    #print(resolve_part_2(rows))