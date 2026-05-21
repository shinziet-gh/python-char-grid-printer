import pandas as pd


# function to find maximum value in a list
def find_max(lst):
    max_val = lst[0]
    for n in lst:
        if n > max_val:
            max_val = n
    return max_val


# function to create a grid of characters
def create_character_grid(x_col, char_col, y_col):
    # create 2d array
    row = find_max(x_col) + 1
    col = find_max(y_col) + 1

    # initialize 2d array with empty spaces
    two_d_array = [[" " for _ in range(row)] for _ in range(col)]

    for i, c in enumerate(char_col):
        x = x_col[i]
        y = y_col[i]
        two_d_array[y][x] = c

    return two_d_array


# function to print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))


# read the file
def read_file(filename):
    doc = pd.read_csv(filename, header=0)

    x_col = [int(x) for x in doc["x-coordinate"]]
    char_col = [str(c) for c in doc["Character"]]
    y_col = [int(y) for y in doc["y-coordinate"]]

    return x_col, char_col, y_col


if __name__ == "__main__":
    x_col, char_col, y_col = read_file("example.csv")
    grid = create_character_grid(x_col, char_col, y_col)
    print_grid(grid)
