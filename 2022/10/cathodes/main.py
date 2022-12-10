def is_special_cycle(cycle):
    special = [20, 60, 100, 140, 180, 220]
    if cycle in special:
        return True
    else:
        return False


def check_cycle_count(cycle_count, x_register, sum):
    if is_special_cycle(cycle_count):
        sum += cycle_count * x_register
    return sum


def draw_on_screen(cycle_count, x_register, screen):
    row = (cycle_count - 1) // 40
    pixel_index = (cycle_count % 40) - 1

    if abs(x_register - pixel_index) > 1:
        screen[row].append(".")
    else:
        screen[row].append("#")

    return screen


def print_screen(screen):
    for row in screen:
        string = "".join(row)
        print(string)


def main():
    with open("input.txt") as file:

        sum = 0
        cycle_count = 1
        x_register = 1
        pixel = 1
        screen = [[] for i in range(7)]
        for line in file.read().split("\n"):
            sum = check_cycle_count(cycle_count, x_register, sum)
            screen = draw_on_screen(cycle_count, x_register, screen)

            if line == "noop":
                cycle_count += 1
            else:
                cycle_count += 1
                sum = check_cycle_count(cycle_count, x_register, sum)
                screen = draw_on_screen(cycle_count, x_register, screen)
                cycle_count += 1
                value = line.split(" ")[1]
                x_register += int(value)
        print(sum)

    print_screen(screen)


if __name__ == "__main__":
    main()
