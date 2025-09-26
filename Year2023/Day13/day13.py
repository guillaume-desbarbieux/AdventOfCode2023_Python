from Year2023.utils import read_file

def test_vertical_reflection(rows, left):
    right = len(rows[0]) - 1 - left

    if left < 0 or right < 0:
        return False

    for row in rows:
        for i in range(min(left, right) + 1):
            if row[left - i] != row[left + i]:
                print(f"left: {left}, right: {right}, i: {i}")
                return False
    return True

if __name__ == "__main__":
    rows = read_file("puzzle.txt")
    for i in range(len(rows)-1):
        if test_vertical_reflection(rows, i):
            print(i)