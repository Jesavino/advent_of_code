def main():

    running_sum = {}
    with open("input.txt") as file:
        sum = 0
        elf_number = 1
        for row in file.read().split("\n"):
            try:
                sum += int(row)
            except:
                running_sum[elf_number] = sum
                elf_number += 1
                sum = 0

    max = 0
    max_elf = 0
    for elf, value in running_sum.items():
        if value > max:
            max = value
            max_elf = elf

    values = list(running_sum.values())
    values.sort(reverse=True)

    print(values[0])

    top3 = 0
    for i in range(3):
        top3 += values[i]
    print(top3)


if __name__ == "__main__":
    main()
