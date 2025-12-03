import copy

if __name__ == "__main__":
    from mapping.Grid import Grid
    from mapping.Obstacle import Obstacle

    filepath = "/home/fl/PycharmProjects/AOC2024/day_six/input.txt"
    grid = Grid(filepath)

    while grid.guard_position_is_valid():
        grid.move_guard()

    position_visited_on_part_one = grid.guard.position_visited
    print(f"[PART ONE] - Number of position visited by the guard: {len(position_visited_on_part_one.keys())}")

    number_of_obstacles_to_loop = 0
    initial_grid = Grid(filepath)
    for index, position in enumerate(position_visited_on_part_one):
        temp_grid = copy.deepcopy(initial_grid)
        obstacle_added = False
        # print(f"Obstacle added on x: {temp_obstacle.x_position}, y: {temp_obstacle.y_position}")

        while temp_grid.guard_position_is_valid() and not temp_grid.guard.in_a_loop:
            temp_grid.move_guard()
            if index < temp_grid.number_of_guard_moves and not obstacle_added:
                temp_grid.obstacles.append(Obstacle(position[0], position[1]))
                obstacle_added = True

        number_of_obstacles_to_loop += temp_grid.obstructions_for_loop
        # print(number_of_obstacles_to_loop)

    print(f"[PART TWO] - Number of position where an obstruction creates a loop: {number_of_obstacles_to_loop}")



