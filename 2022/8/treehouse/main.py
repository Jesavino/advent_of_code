NORTH = 0
EAST = 3
SOUTH = 2
WEST = 1


def is_tree_visable(row, col, grid):
    visable = [True, True, True, True]

    tree_height = grid[row][col]

    for left in range(0, col):
        if grid[row][left] >= tree_height:
            visable[WEST] = False
            break

    for right in range(col + 1, len(grid[0])):
        if grid[row][right] >= tree_height:
            visable[EAST] = False
            break

    for up in range(0, row):
        if grid[up][col] >= tree_height:
            visable[NORTH] = False
            break

    for down in range(row + 1, len(grid)):
        if grid[down][col] >= tree_height:
            visable[SOUTH] = False
            break

    if all(dir is False for dir in visable):
        return False
    else:
        return True


def calc_scenic_score(row, col, grid):

    scores = [0, 0, 0, 0]

    tree_height = grid[row][col]

    score = 0
    for left in range(col - 1, 0 - 1, -1):
        if grid[row][left] < tree_height:
            score += 1
        elif grid[row][left] >= tree_height:
            score += 1
            break
        else:
            break
    scores[WEST] = score

    score = 0
    for right in range(col + 1, len(grid[0])):
        if grid[row][right] < tree_height:
            score += 1
        elif grid[row][right] >= tree_height:
            score += 1
            break
        else:
            break
    scores[EAST] = score

    score = 0
    for up in range(row - 1, 0 - 1, -1):
        if grid[up][col] < tree_height:
            score += 1
        elif grid[up][col] >= tree_height:
            score += 1
            break
        else:
            break
    scores[NORTH] = score

    score = 0
    for down in range(row + 1, len(grid)):
        if grid[down][col] < tree_height:
            score += 1
        elif grid[down][col] >= tree_height:
            score += 1
            break
        else:
            break
    scores[SOUTH] = score

    total = 1
    for score in scores:
        total = total * score
    return total


def main():

    grid = []
    with open("input.txt") as file:
        for row in file.read().split("\n"):
            trees = [int(height) for height in row]
            grid.append(trees)

    sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_tree_visable(row, col, grid):
                sum += 1

    print(sum)

    score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            tree_score = calc_scenic_score(row, col, grid)
            if tree_score > score:
                score = tree_score

    print(score)


if __name__ == "__main__":
    main()
