import math

SAMPLE_GRID_SIZE = (11, 7)
INPUT_GRID_SIZE = (101, 103)

def get_robots(use_sample: bool = True) -> list:
    if use_sample:
        filepath = "sample.txt"
    else:
        filepath = "input.txt"

    robots = []
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip().replace("p=", "").replace("v=", "").split(" ")
            initial_position = [int(value) for value in line[0].split(",")]
            velocity = tuple(int(value) for value in line[1].split(","))
            robots.append([initial_position, velocity])
    return robots

def move_robots(robots, use_sample = True):
    if use_sample:
        grid_size = SAMPLE_GRID_SIZE
    else:
        grid_size = INPUT_GRID_SIZE

    for robot in robots:
        robot[0] = [robot[0][0] + robot[1][0], robot[0][1] + robot[1][1]]
        if robot[0][0] < 0:
            robot[0][0] = grid_size[0] + robot[0][0]
        elif robot[0][0] >= grid_size[0]:
            robot[0][0] = 0 + robot[0][0] - grid_size[0]

        if robot[0][1] < 0:
            robot[0][1] = grid_size[1] + robot[0][1]
        elif robot[0][1] >= grid_size[1]:
            robot[0][1] = 0 + robot[0][1] - grid_size[1]

    return robots

def calculate_robots_in_quadrants(robots, use_sample = True):
    if use_sample:
        grid_size = SAMPLE_GRID_SIZE
    else:
        grid_size = INPUT_GRID_SIZE

    middle_column = math.floor(grid_size[0]/2)
    middle_row = math.floor(grid_size[1]/2)

    quadrant_one = 0
    quadrant_two = 0
    quadrant_three = 0
    quadrant_four = 0

    for robot in robots:
        if robot[0][0] < middle_column and robot[0][1] < middle_row:
            quadrant_one += 1
        elif robot[0][0] > middle_column and robot[0][1] < middle_row:
            quadrant_two += 1
        elif robot[0][0] < middle_column and robot[0][1] > middle_row:
            quadrant_three += 1
        elif robot[0][0] > middle_column and robot[0][1] > middle_row:
            quadrant_four += 1

    return (quadrant_one, quadrant_two, quadrant_three, quadrant_four)

def put_robots_on_grid(robots: list[tuple[tuple[int, int]]], use_sample: bool = True):
    if use_sample:
        grid = [[0 for _ in range(SAMPLE_GRID_SIZE[0])] for _ in range(SAMPLE_GRID_SIZE[1])]
    else:
        grid = [[0 for _ in range(INPUT_GRID_SIZE[0])] for _ in range(INPUT_GRID_SIZE[1])]

    for robot in robots:
        grid[robot[0][1]][robot[0][0]] += 1

    return grid

def part_one(robots, use_sample: bool = True):
    for _ in range(100):
       robots = move_robots(robots, use_sample)

    robots_per_quadrant = calculate_robots_in_quadrants(robots, use_sample)
    print(f"[PART ONE] - Number of robots per quadrant: 1 = {robots_per_quadrant[0]}, 2 = {robots_per_quadrant[1]}, 3 = {robots_per_quadrant[2]}, 4 = {robots_per_quadrant[3]}")
    print(f"[PART ONE] - Safety factor: {math.prod(robots_per_quadrant)}")

def part_two(robots):
    safety_score = 1000000000000
    number_of_seconds = 1
    for i in range(1, (101 * 103)):
        robots = move_robots(robots, use_sample = False)
        actual_safety_score = math.prod(calculate_robots_in_quadrants(robots, False))
        if actual_safety_score < safety_score:
            safety_score = actual_safety_score
            number_of_seconds = i

    print(f"[PART TWO] - The minimum number of seconds to get a tree is: {number_of_seconds}")



if __name__ == "__main__":
    use_sample = False
    robots = get_robots(use_sample)
    part_one(robots, use_sample)
    part_two(get_robots(use_sample))