SELECTION_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

NORMALIZED_SELECTIONS = {
    "A": 0,
    "B": 1,
    "C": 2,
    "X": 0,
    "Y": 1,
    "Z": 2,
}

THEIRS_TO_MINE_MAP = {
    0: "X",
    1: "Y",
    2: "Z",
}

TIE = 3
LOSS = 0
WIN = 6


def determine_selection(theirs, mine):
    theirs = normalize_selection(theirs)
    mine = normalize_selection(mine)
    if mine == 0:
        return THEIRS_TO_MINE_MAP[(theirs - 1) % 3]
    elif mine == 1:
        return THEIRS_TO_MINE_MAP[theirs]
    else:
        return THEIRS_TO_MINE_MAP[(theirs + 1) % 3]


def score_selection(selection):
    return SELECTION_SCORES[selection]


def normalize_selection(theirs):
    return NORMALIZED_SELECTIONS[theirs]


def compute_winner(theirs, mine):
    theirs = normalize_selection(theirs)
    mine = normalize_selection(mine)
    if theirs == mine:
        return TIE
    if mine == (theirs + 1) % 3:
        return WIN
    else:
        return LOSS


def compute_score(theirs, mine):
    score = 0
    score += score_selection(mine)
    score += compute_winner(theirs, mine)
    return score


def main():
    score = 0
    with open("input.txt") as f:
        for row in f.read().split("\n"):
            scores = row.split(" ")
            theirs, mine = scores[0], scores[1]
            mine = determine_selection(theirs, mine)
            score += compute_score(theirs, mine)

    print(score)


if __name__ == "__main__":
    main()
