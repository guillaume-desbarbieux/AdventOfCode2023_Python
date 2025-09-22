from typing import List

def read_file(path: str) -> List[str]:
      with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\r\n") for line in f]

def split(string, char):
    split_string = []
    current = ""
    for i in range(len(string)):
        if string[i] == char:
            split_string.append(current)
            current = ""
        else :
            current += string[i]
    split_string.append(current)
    return split_string
