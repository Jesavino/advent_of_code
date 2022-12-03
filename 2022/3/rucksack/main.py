def calc_priority(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def calc_occurences(string):
    occurences = {}
    for letter in string:
        occurences[letter] = 1
    return occurences


def find_overlap(first, second):
    overlap = []
    for element in first.keys():
        if element in second:
            overlap.append(element)
    return overlap


def main():

    score = 0
    lines = []
    with open("input.txt") as f:
        for line in f.read().split("\n"):
            lines.append(line)

    for i in range(0, len(lines), 3):
        first = lines[i]
        second = lines[i + 1]
        third = lines[i + 2]

        first_occurances = calc_occurences(first)
        second_occurances = calc_occurences(second)
        third_occurances = calc_occurences(third)

        one_two_overlap = find_overlap(first_occurances, second_occurances)
        two_three_overlap = find_overlap(second_occurances, third_occurances)

        one_two_occurances = calc_occurences(one_two_overlap)
        two_three_occurances = calc_occurences(two_three_overlap)
        final_overlap = find_overlap(one_two_occurances, two_three_occurances)

        score += calc_priority(final_overlap[0])

    print(score)


if __name__ == "__main__":
    main()
