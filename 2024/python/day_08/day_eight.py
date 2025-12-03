import copy
from typing import Tuple, Any

def find_antennas(grid: list[list[str]]) -> dict[str, list[tuple[int]]]:
    antennas = {}
    for y, row in enumerate(grid):
        for x, frequency in enumerate(row):
            if frequency != '.':
                if frequency not in antennas:
                    antennas[frequency] = []
                antennas[frequency].append((x, y))
    return antennas

def make_a_vector(point1: tuple[int], point2: tuple[int]) -> tuple[int, Any]:
    return point2[0] - point1[0], point2[1] - point1[1]

def position_is_valid(grid: list[list[str]], position: tuple[int, int]) -> bool:
    grid_width = len(grid[0])
    grid_length = len(grid)

    x, y = position

    return 0 <= x < grid_width and 0 <=  y < grid_length

def calculate_antinode_positions(position1, position2):
    vector = make_a_vector(position1, position2)  # This helps me to know where to put the antinodes
    antinode_position_1 = (position1[0] - vector[0], position1[1] - vector[1])
    antinode_position_2 = (position2[0] + vector[0], position2[1] + vector[1])
    return antinode_position_1, antinode_position_2

def add_antinode(grid, antinodes, antinode) -> bool:
    if position_is_valid(grid, antinode):
        antinodes[antinode] = True
        return True
    return False

def part_one(grid):
    antennas = find_antennas(grid)
    antinodes = {}
    for frequency, positions in antennas.items():
        for i in range(len(positions)):
            other_positions = copy.deepcopy(positions)
            position = other_positions.pop(i)
            for other_position in other_positions:
                antinode1, antinode2 = calculate_antinode_positions(position, other_position)
                add_antinode(grid, antinodes, antinode1)
                add_antinode(grid, antinodes, antinode2)

    print(f"[PART ONE] - There are {len(antinodes)} antinodes placed on the map.")

def part_two(grid):
    antennas = find_antennas(grid)
    antinodes = {}

    for frequency, positions in antennas.items():
        if len(positions) > 1:
            for position in positions:
                antinodes[position] = True
        for i in range(len(positions)):
            other_positions = copy.deepcopy(positions)
            position = other_positions.pop(i)
            for other_position in other_positions:
                vector = make_a_vector(position, other_position)  # This helps me to know where to put the antinodes
                antinode1, antinode2 = calculate_antinode_positions(position, other_position)
                while add_antinode(grid, antinodes, antinode1):
                    antinode1 = (antinode1[0] - vector[0], antinode1[1] - vector[1])
                while add_antinode(grid, antinodes, antinode2):
                    antinode2 = (antinode2[0] - vector[0], antinode2[1] - vector[1])

    print(f"[PART TWO] - There are {len(antinodes)} antinodes placed on the map.")

if __name__ == "__main__":
    grid = []
    with open("/home/fl/PycharmProjects/AOC2024/day_eight/input.txt") as file:
        for line in file.readlines():
            grid.append([char for char in line if char != "\n"])

    part_one(grid)

    part_two(grid)