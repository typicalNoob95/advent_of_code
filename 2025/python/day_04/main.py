PAPER_ROLL_LIMIT = 3
PAPER_ROLL = "@"

def remove_rolls_from_grid(grid:  list[list[str]]) -> tuple[list[list[str]], int]:
    grid_height = len(grid)
    grid_width = len(grid[0])

    number_of_accessible_paper_rolls = 0
    accessible_paper_rolls_positions = list()

    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x] == "@":
                number_of_adjcent_paper_rolls = 0

                # Upper row
                if y != 0:
                    if x != 0:
                        if grid[y-1][x-1] == "@":
                            number_of_adjcent_paper_rolls += 1
                    
                    if grid[y-1][x] == "@":
                        number_of_adjcent_paper_rolls += 1
                    
                    if x < grid_width - 1:
                        if grid[y-1][x+1] == "@":
                            number_of_adjcent_paper_rolls += 1

                # actual row
                if x != 0:
                    if grid[y][x-1] == "@":
                        number_of_adjcent_paper_rolls += 1
                if x != grid_width - 1:
                    if grid[y][x+1] == "@":
                            number_of_adjcent_paper_rolls += 1

                # lower row
                if y != grid_height - 1:
                    if x != 0:
                        if grid[y+1][x-1] == "@":
                            number_of_adjcent_paper_rolls += 1
                    
                    if grid[y+1][x] == "@":
                        number_of_adjcent_paper_rolls += 1
                    
                    if x < grid_width - 1:
                        if grid[y+1][x+1] == "@":
                            number_of_adjcent_paper_rolls += 1

                if number_of_adjcent_paper_rolls <= PAPER_ROLL_LIMIT:
                    number_of_accessible_paper_rolls += 1
                    accessible_paper_rolls_positions.append((y,x))

    for pos in accessible_paper_rolls_positions:
        grid[pos[0]][pos[1]] = "."
    for line in grid:
        print(line)
    print()

    return grid, number_of_accessible_paper_rolls

def part_one(grid: list[list[str]]) -> None:
    grid_height = len(grid)
    grid_width = len(grid[0])

    number_of_accessible_paper_rolls = 0
    accessible_paper_rolls_positions = list()

    for y in range(grid_height):
        for x in range(grid_width):
            if grid[y][x] == "@":
                number_of_adjcent_paper_rolls = 0

                # Upper row
                if y != 0:
                    if x != 0:
                        if grid[y-1][x-1] == "@":
                            number_of_adjcent_paper_rolls += 1
                    
                    if grid[y-1][x] == "@":
                        number_of_adjcent_paper_rolls += 1
                    
                    if x < grid_width - 1:
                        if grid[y-1][x+1] == "@":
                            number_of_adjcent_paper_rolls += 1

                # actual row
                if x != 0:
                    if grid[y][x-1] == "@":
                        number_of_adjcent_paper_rolls += 1
                if x != grid_width - 1:
                    if grid[y][x+1] == "@":
                            number_of_adjcent_paper_rolls += 1

                # lower row
                if y != grid_height - 1:
                    if x != 0:
                        if grid[y+1][x-1] == "@":
                            number_of_adjcent_paper_rolls += 1
                    
                    if grid[y+1][x] == "@":
                        number_of_adjcent_paper_rolls += 1
                    
                    if x < grid_width - 1:
                        if grid[y+1][x+1] == "@":
                            number_of_adjcent_paper_rolls += 1

                if number_of_adjcent_paper_rolls <= PAPER_ROLL_LIMIT:
                    number_of_accessible_paper_rolls += 1
                    accessible_paper_rolls_positions.append((y,x))

    for pos in accessible_paper_rolls_positions:
        grid[pos[0]][pos[1]] = "X"
    for line in grid:
        print(line)
    print(number_of_accessible_paper_rolls)

def part_two(grid: list[list[str]]) -> None:
    total_removed_paper_rolls = 0 
    grid, removed_paper_rolls = remove_rolls_from_grid(grid)
    total_removed_paper_rolls += removed_paper_rolls
    while removed_paper_rolls != 0:
        grid, removed_paper_rolls = remove_rolls_from_grid(grid)
        total_removed_paper_rolls += removed_paper_rolls

    print(total_removed_paper_rolls)
    

if __name__ == "__main__":
    grid = []
    with open("2025/python/day_04/input.txt", "r") as file:
        for line in file.readlines():
            grid.append([char for char in line.strip()])

    for line in grid:
        print(line)
    print()

    #part_one(grid)
    part_two(grid)