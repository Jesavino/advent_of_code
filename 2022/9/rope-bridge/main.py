def calc_distance(head, tail):
    distance = (head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2
    return distance


def is_tail_adjacent(head, tail):
    distance = calc_distance(head, tail)
    if distance <= 1:
        return True

    # diag is distance 2 but considered adjacent for this problem
    if (abs(head[0] - tail[0]) == 1) and (abs(head[1] - tail[1]) == 1):
        return True
    else:
        return False


def move_head(head, direction):
    if direction == "L":
        head[1] -= 1
    elif direction == "R":
        head[1] += 1
    elif direction == "U":
        head[0] += 1
    elif direction == "D":
        head[0] -= 1

    return head


def move_tail_linearly(head, tail):
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    else:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1
    return head, tail


def move_tail_diag(head, tail):
    if head[0] > tail[0]:
        tail[0] += 1
    else:
        tail[0] -= 1

    if head[1] > tail[1]:
        tail[1] += 1
    else:
        tail[1] -= 1

    return head, tail


def move_tail(head, tail):
    if head[0] == tail[0] or head[1] == tail[1]:
        head, tail = move_tail_linearly(head, tail)
    else:
        head, tail = move_tail_diag(head, tail)

    return head, tail


def main():

    with open("input.txt") as file:

        head = [0, 0]
        tail = [0, 0]
        position_map = {}
        position_map[(tail[0], tail[1])] = True
        for instruction in file.read().split("\n"):
            [dir, times] = instruction.split(" ")
            for i in range(int(times)):
                head = move_head(head, dir)

                if is_tail_adjacent(head, tail):
                    continue
                else:
                    head, tail = move_tail(head, tail)
                    position_map[(tail[0], tail[1])] = True

        print(len(position_map))

    # part 2
    with open("input.txt") as file:

        head = [0, 0]
        tails = []
        for i in range(9):
            tails.append([0, 0])
        position_map = {}
        position_map[(0, 0)] = True
        for instruction in file.read().split("\n"):
            [dir, times] = instruction.split(" ")
            for i in range(int(times)):
                head = move_head(head, dir)

                tmp_head = head
                for tail in tails:
                    if is_tail_adjacent(tmp_head, tail):
                        tmp_head = tail
                        continue
                    else:
                        tmp_head, tail = move_tail(tmp_head, tail)
                        tmp_head = tail

                position_map[(tails[8][0], tails[8][1])] = True

        print(len(position_map))


if __name__ == "__main__":
    main()
