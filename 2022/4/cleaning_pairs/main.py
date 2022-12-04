from posixpath import split


def get_upper_and_lower_bounds(assignement):
    """Gets lower and upper bounds of "5-10" as lower: 5, upper: 10"""
    bounds = assignement.split("-")
    return {
        "lower": int(bounds[0].strip()),
        "upper": int(bounds[1].strip()),
    }


def is_range_subset(first, second):
    if (first["lower"] >= second["lower"]) and (first["lower"] <= second["upper"]):
        return True
    else:
        return False


def main():

    count = 0
    with open("input.txt") as f:
        for line in f.read().split("\n"):
            pairs = line.split(",")
            first = get_upper_and_lower_bounds(pairs[0])
            second = get_upper_and_lower_bounds(pairs[1])

            if is_range_subset(first, second) or is_range_subset(second, first):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
