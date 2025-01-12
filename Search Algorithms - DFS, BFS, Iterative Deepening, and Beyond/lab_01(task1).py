from copy import deepcopy

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
stack = []


def move_up(zeroi, zeroj):
    i = zeroi - 1
    if i >= 0:
        return i, zeroj
    return None, None


def move_down(zeroi, zeroj):
    i = zeroi + 1
    if i <= 2:
        return i, zeroj
    return None, None


def move_right(zeroi, zeroj):
    j = zeroj + 1
    if j <= 2:
        return zeroi, j
    return None, None


def move_left(zeroi, zeroj):
    j = zeroj - 1
    if j >= 0:
        return zeroi, j
    return None, None


def dfs1(grid, depth_limit):
    if check_if_it_is_goal(grid):
        return stack
    if depth_limit == 0:
        return None

    zeroi, zeroj = index_of_zero(grid)

    for move_func in [move_up, move_down, move_right, move_left]:
        i, j = move_func(zeroi, zeroj)
        if i is not None and j is not None:
            stack.append(deepcopy(grid))  # Make a deep copy before pushing to stack
            swap(grid, i, j, zeroi, zeroj)

            result = dfs1(grid, depth_limit - 1)
            if result is not None:
                return result

            grid = stack.pop()  # Restore the grid from the stack

    return None


def swap(grid, a, b, c, d):
    grid[a][b], grid[c][d] = grid[c][d], grid[a][b]


def check_if_it_is_goal(start):
    return start == goal


def index_of_zero(start):
    for i in range(3):
        for j in range(3):
            if start[i][j] == 0:
                return i, j


def iddfs1(grid):
    depth = 0
    lim = 20
    while depth <= lim:
        result = dfs1(grid, depth)
        if result is not None:
            return result
        depth += 1
    return None


def main():
    start = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    result = iddfs1(start)
    if result:
        print('Found')
    else:
        print('Not found!')


main()
