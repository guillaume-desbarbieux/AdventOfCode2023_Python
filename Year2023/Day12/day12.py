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


def place_for_block(row, position, block_index):
    spring, block = row
    for i in range(position, position + block[block_index] + 1):
        if spring[i] == '.':
            return False
    return True


def no_more_broken(springs : List[char], position : int):
    for spring in springs[:position]:
        if spring == '#':
            #print("Il reste un broken, raté")
            return 0
    #print("Pas de broken restant, super")
    return 1


def sum_from(blocks, block_index):
    sum = 0
    for i in range(block_index, len(blocks)):
        sum += blocks[i]
    return sum


def count_arrangement(row, position, block_index):
    springs, blocks = row
    #print("".join(springs))
    #print(" ".join(map(str,blocks)))
    #print(f"Position {position}, Block index {block_index}")


    #Si on a parcouru tous les springs, on vérifie qu'on a placé tous les blocs
    if position >= len(springs):
        if block_index >= len(blocks):
            #print("plus, de springs, plus de blocs, on a fini")
            return 1
        else:
            #print("plus de springs, mais encore des blocs")
            return 0

    #Si on a placé tous les blocs, on vérifie qu'il ne reste plus de broken springs
    if block_index >= len(blocks):
        #print("plus de blocs, regardons les springs restants")
        return no_more_broken(springs, position)

    #On vérifie qu'il reste suffisamment de place pour tous les blocs restants (Sum = nombre de brokens à placer ; en ajoutant les '.' minimaux entre chaque groupe de brokens
    #print(f"poser {sum_from(blocks, block_index)} + {len(blocks) - block_index - 1} dans {len(springs) - position}")

    if sum_from(blocks, block_index) + len(blocks) - 1 - block_index > len(springs) - position:
        #print("la places restante est insuffisante")
        return 0

    #Si '.' on regarde le spring suivant
    if springs[position] == '.':
        "Le spring est un '.', on passe au suivant"
        return count_arrangement(row, position + 1, block_index)

    #Si # on regarde après le bloc de '#' suivi de '.'
    if springs[position] == '#':
        if place_for_block(row, position, block_index):
            #print("Le spring est '#', on pose le bloc")
            return count_arrangement(row, position + blocks[block_index] + 1, block_index + 1)
        else:
            return 0

    #Si '?' on additionne les deux arrangements possibles.
    if springs[position] == '?':
        if place_for_block(row, position, block_index):
            #print("Le spring est '?', on regarde les deux arrangements possibles")
            return count_arrangement(row, position + 1, block_index) + count_arrangement(row, position + blocks[block_index] + 1, block_index + 1)
        else:
            return count_arrangement(row, position + 1, block_index)



def resolve_part_2(rows):
    unfold_rows = [(unfold_left(row[0]), unfold_right(row[1])) for row in rows]
    sum = 0
    memo = {}
    print(count_arrangement(unfold_rows[0], 0, 0))
    print(count_arrangement(unfold_rows[1], 0, 0))

    #for row in unfold_rows:
    #    sum+= count_arrangement(row, 0, 0)
    #return sum

if __name__ == "__main__":
    rows = parse_puzzle("puzzle.txt")
    #print(resolve_part_1(rows))
    print(resolve_part_2(rows))


