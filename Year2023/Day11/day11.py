from Year2023.utils import read_file

def extended_path(coord1, coord2, extended_rows, extended_cols, expansion):
    i1, j1 = coord1
    i2, j2 = coord2
    path = abs(i1 - i2) + abs(j1-j2)
    for row in extended_rows:
        if (i1 <= row <= i2) or (i2 <= row <= i1):
            path += expansion - 1
    for col in extended_cols:
        if (j1 <= col <= j2) or (j2 <= col <= j1):
            path += expansion - 1
    return path

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

if __name__ == "__main__":
    sky = read_file("puzzle.txt")
    rows,cols = get_empty_rows_ans_cols(sky)

    galaxies = []
    for i in range(len(sky)):
        for j in range(len(sky[i])):
            if sky[i][j] == '#':
                galaxies.append((i, j))

    sum = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            sum += extended_path(galaxies[i], galaxies[j], rows, cols, 1000000)

    print(sum)
