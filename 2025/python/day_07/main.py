from collections import deque

def print_grid(grid):
    for line in grid:
        print(line)

def part_one():
    with open("2025/python/day_07/sample.txt", "r") as file:
        grid = []
        for line in file.readlines():
            grid.append([char for char in line.strip()])

    grid[1][grid[0].index("S")] = "|"
    
    number_of_split = 0
    for y in range(1, len(grid)):
        if y != len(grid) -1:
            for x in range(len(grid[y])):
                if grid[y][x] == "|":
                    if grid[y + 1][x] == "^":
                        grid[y+1][x-1] = "|"
                        grid[y+1][x+1] = "|"
                        number_of_split += 1
                    else:
                        grid[y+1][x] = "|"
    
    print(number_of_split)


def set_grid_value(char: str) -> int | str:
    if char == ".":
        return 0
    else:
        return char

def part_two():
    with open("2025/python/day_07/input.txt", "r") as file:
        grid = []
        for line in file.readlines():
            grid.append([set_grid_value(char) for char in line.strip()])

    grid_height = len(grid)
    grid_width = len(grid[0])

    grid[1][grid[0].index("S")] = 1
    for y in range(grid_height-1):
        for x in range(grid_width):
            if type(grid[y][x]) == int and grid[y][x] > 0:
                if grid[y+1][x] == "^":
                    grid[y+1][x-1] += grid[y][x]
                    grid[y+1][x+1] += grid[y][x]
                else:
                    grid[y+1][x] += grid[y][x]
            #print_grid(grid)
    timelines = sum(grid[grid_height-1])
    print(timelines)




if __name__ == "__main__":
    part_one()
    part_two()
    

