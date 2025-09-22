from typing import List

def read_file(path: str) -> List[str]:
    """
    Lit le fichier situé à 'path' et retourne une liste de chaînes,
    une par ligne, sans les caractères de fin de ligne.
    """
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\r\n") for line in f]