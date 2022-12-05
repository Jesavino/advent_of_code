import re
from venv import create


"""
[H]                 [Z]         [J]
[L]     [W] [B]     [G]         [R]
[R]     [G] [S]     [J] [H]     [Q]
[F]     [N] [T] [J] [P] [R]     [F]
[B]     [C] [M] [R] [Q] [F] [G] [P]
[C] [D] [F] [D] [D] [D] [T] [M] [G]
[J] [C] [J] [J] [C] [L] [Z] [V] [B]
[M] [Z] [H] [P] [N] [W] [P] [L] [C]
 1   2   3   4   5   6   7   8   9 
"""

STACK = {
    1: ["M", "J", "C", "B", "F", "R", "L", "H"],
    2: ["Z", "C", "D"],
    3: ["H", "J", "F", "C", "N", "G", "W"],
    4: ["P", "J", "D", "M", "T", "S", "B"],
    5: ["N", "C", "D", "R", "J"],
    6: ["W", "L", "D", "Q", "P", "J", "G", "Z"],
    7: ["P", "Z", "T", "F", "R", "H"],
    8: ["L", "V", "M", "G"],
    9: ["C", "B", "G", "P", "F", "Q", "R", "J"],
}


def find_ints(string):
    ints = re.findall(r"\d+", string)
    return [int(s) for s in ints]


def move_crates(start, end, times):
    crates = STACK[start][-times:]
    del STACK[start][-times:]

    for crate in crates:
        STACK[end].append(crate)


def main():
    with open("input.txt") as f:
        for row in f.read().split("\n"):
            ints = find_ints(row)
            move_crates(ints[1], ints[2], ints[0])

    result = ""
    for i in range(1, 10):
        try:
            result += STACK[i][-1]
        except:
            pass
    print(result)


if __name__ == "__main__":
    main()
