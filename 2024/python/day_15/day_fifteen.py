from collections import deque
from copy import deepcopy


def get_grid_and_moves(filepath):
    grid = {
        "walls": [],
        "boxes": [],
        "robot": None
    }

    moves = deque()

    with open(filepath) as file:
        is_grid = True

        for y, line in enumerate(file.readlines()):
            if line == "\n":
                is_grid = False
            for x, column in enumerate(line):
                if is_grid:
                    if column == "#":
                        grid["walls"].append((x, y))
                    elif column == "O":
                        grid["boxes"].append((x,y))
                    elif column == "@":
                        grid["robot"] = (x, y)
                else:
                    if column != "\n":
                        moves.append(column)
    return grid, moves

def prepare_part_two_grid_and_moves(filepath):
    replacements = {
        ".": "..",
        "#": "##",
        "@": "@.",
        "O": "[]"
    }

    moves = deque()

    new_grid = []
    is_grid = True
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            if line == "\n":
                is_grid = False
            elif is_grid:
                chars = "".join([replacements[char] for char in line.strip()])
                new_grid.append([char for char in chars])
            else:
                for char in line.strip():
                    moves.append(char)

    for row in new_grid:
        print(row)
    print(moves)

    return new_grid, moves

def move_robot(grid, direction):
    next_position = grid["robot"][0] + direction[0], grid["robot"][1] + direction[1]
    if next_position in grid["walls"]:
        return
    elif next_position in grid["boxes"]:
        moved = move_boxe(grid, direction, next_position)
        if not moved:
            return

    grid["robot"] = next_position

def move_boxe(grid, direction, box_position):
    next_position = box_position[0] + direction[0], box_position[1] + direction[1]
    if next_position in grid["walls"]:
        return False

    if next_position in grid["boxes"]:
        next_box_position = next_position
        moved = move_boxe(grid, direction, next_box_position)
        if not moved:
            return False

    grid["boxes"].remove(box_position)
    grid["boxes"].append(next_position)
    return True


def part_one(grid, moves, directions):
    while len(moves) > 0:
        move = moves.popleft()
        direction = directions[move]
        move_robot(grid, direction)

    print(f"[PART ONE] - The sum of all GPS coordinates is: {sum([(100 * box[1]) + box[0] for box in grid["boxes"]])}")

def part_two(filepath, directions):
    grid, moves = prepare_part_two_grid_and_moves(filepath)
    robot_position = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                robot_position = (x, y)
    print(len(moves))
    while len(moves) > 0:
        move = moves.popleft()
        row_direction = directions[move][1]
        column_direction = directions[move][0]
        positions_to_move = [robot_position]
        should_move = True
        for position in positions_to_move:
            next_position = (position[0] + column_direction, position[1] + row_direction)
            if next_position in positions_to_move:
                continue # If this position is already checked, don't bother.
            item = grid[next_position[1]][next_position[0]]
            if item == "#":
                should_move = False
                break
            elif item == "[":
                positions_to_move.append(next_position)
                other_box_side = (next_position[0] + 1, next_position[1])
                positions_to_move.append(other_box_side)
            elif item == "]":
                positions_to_move.append(next_position)
                other_box_side = (next_position[0] - 1, next_position[1])
                positions_to_move.append(other_box_side)
        if not should_move:
            continue

        # Copy the grid to keep the places of the items
        copied_grid = [list(row) for row in grid]
        # Move the robot
        grid[robot_position[1]][robot_position[0]] = "."
        grid[robot_position[1] + row_direction][robot_position[0] + column_direction] = "@"
        #for row in grid:
        #    print(row)
        # Move the boxes
        for position_to_move in positions_to_move[1:]:
            grid[position_to_move[1]][position_to_move[0]] = "." # The last position of the object is changed to a dot
        for position_to_move in positions_to_move[1:]:
            # Move boxes with the copied grid
            grid[position_to_move[1] + row_direction][position_to_move[0] + column_direction] = copied_grid[position_to_move[1]][position_to_move[0]]

        robot_position = (robot_position[0] + column_direction, robot_position[1] + row_direction)


    sum_of_gps_coordinates = sum(100 * y + x for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == "[")
    print(f"[PART TWO] - The sum of all GPS coordinates is: {sum_of_gps_coordinates}")

if __name__ == "__main__":
    directions = {
        "<": (-1, 0),
        ">": (1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }

    #grid, moves = get_grid_and_moves("input.txt")
    #part_one(grid, moves, directions)

    part_two("input.txt", directions)



