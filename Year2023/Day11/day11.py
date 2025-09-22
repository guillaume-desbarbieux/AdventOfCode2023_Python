from os import MFD_ALLOW_SEALING
from pickletools import read_stringnl_noescape

from Year2023.utils import read_file


def path(coord1, coord2) -> int:
    a, b = coord1
    c, d = coord2
    return abs(a - c) + abs(b - d)


def get_empty_rows_ans_cols(sky):
    empty_rows = []
    empty_columns = []
    for i in range(len(sky)):
        if is_empty(sky[i]):
            empty_rows.append(i)
    for j in range(len(sky[0])):
        col_is_empty= True
        for i in range(len(sky)):
            if sky[i][j] == '#':
                col_is_empty = False
                break
        if col_is_empty:
            empty_columns.append(j)
    return empty_rows, empty_columns

def is_empty(row):
    for i in row:
        if i == '#':
            return False
    return True


def extend_rows(sky, rows):
    extended_sky = []
    for i in range(len(sky)-1, -1, -1):
        extended_sky.append(sky[i])
        if i in rows:
            extended_sky.append(sky[i])
    return extended_sky


def extend_cols(sky, cols):
    extended_sky = []
    for i in range(len(sky)):
        extended_sky.append([])

    for j in range(len(sky[0])-1, -1, -1):
        for i in range(len(sky)):
            extended_sky[i].append(sky[i][j])
            if j in cols:
                extended_sky[i].append(sky[i][j])
    return extended_sky


def extend(sky, rows, cols):
    rows_extended_sky = extend_rows(sky, rows)
    return extend_cols(rows_extended_sky, cols)




if __name__ == "__main__":
    sky = read_file("puzzle.txt")
    rows,cols = get_empty_rows_ans_cols(sky)
    extended_sky = extend(sky, rows, cols)

    galaxies = []
    for i in range(len(extended_sky)):
        for j in range(len(extended_sky[i])):
            if extended_sky[i][j] == '#':
                galaxies.append((i, j))

    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            sum += path(galaxies[i], galaxies[j])

    print(sum)
