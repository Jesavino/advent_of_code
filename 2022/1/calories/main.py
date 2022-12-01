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

    values = list(running_sum.values())
    values.sort(reverse=True)

    print(values[0])

    top3 = 0
    for i in range(3):
        top3 += values[i]
    print(top3)


if __name__ == "__main__":
    main()
