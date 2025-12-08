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

def part_two():
    with open("2025/python/day_07/sample.txt", "r") as file:
        grid = []
        for line in file.readlines():
            grid.append([char for char in line.strip()])

    grid[1][grid[0].index("S")] = "|"



if __name__ == "__main__":
    part_one()
    part_two()
    

