from os import MFD_ALLOW_SEALING

from Year2023.utils import read_file


def path(coord1, coord2) -> int:
    a, b = coord1
    c, d = coord2
    return abs(a - c) + abs(b - d)


def expand(sky):
    empty_lines = []
    empty_columns = []
    for i in range(len(sky)):
        if is_empty(sky[i]):
            empty_lines.append(i)
    for j in range(len(sky[0])):
        empty = True
        for i in range(len(sky)):
            if sky[i][j] == '#':
                empty = False
                break
        if empty:
            empty_columns.append(j)
    return empty_lines, empty_columns

def is_empty(line):
    for i in line:
        if i == '#':
            return False
    return True


if __name__ == "__main__":
    sky = read_file("puzzle.txt")
    a,b = expand(sky)
    print(a,b)

    galaxies = []
    for i in range(len(sky)):
        for j in range(len(sky[i])):
            if sky[i][j] == '#':
                galaxies.append((i, j))

    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            sum += path(galaxies[i], galaxies[j])

    print(sum)
