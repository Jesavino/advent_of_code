SEEN = {}


def track_seen(char):
    if char in SEEN:
        SEEN[char] += 1
    else:
        SEEN[char] = 1


def remove_seen(char):
    if SEEN[char] > 1:
        SEEN[char] -= 1
    else:
        del SEEN[char]


def main():

    with open("input.txt") as f:
        input = f.read()

        count = 0
        seen = {}
        buffer = []
        for char in input:
            count += 1
            if len(buffer) < 14:
                buffer.append(char)
                track_seen(char)
            else:
                el = buffer.pop(0)
                remove_seen(el)
                buffer.append(char)
                track_seen(char)

            if len(SEEN) == 14:
                print(count)
                exit()


if __name__ == "__main__":
    main()
