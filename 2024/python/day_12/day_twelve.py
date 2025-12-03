# References: https://en.wikipedia.org/wiki/Flood_fill

from collections import deque

def get_garden(filepath: str):
    with open(filepath) as file:
        garden = []
        for line in file.readlines():
            line = line.strip()
            garden.append([char for char in line])

        return garden

def position_is_valid(garden: list[list[str]], position: tuple[int, int]) -> bool:
    length = len(garden)
    width = len(garden[0])

    return 0 <= position[0] < width and 0 <= position[1] < length

def get_region(garden: list[list[str]], starting_point: tuple[int, int], plant_type: str):
    region  = set()
    flood_fill_queue = deque()
    flood_fill_queue.append(starting_point)
    while len(flood_fill_queue) > 0:
        position = flood_fill_queue.popleft()
        if position in region: continue
        if garden[position[1]][position[0]] == plant_type:
            region.add(position)
            for next_position in [
                (position[0] + 1, position[1]),
                (position[0] - 1, position[1]),
                (position[0], position[1] + 1),
                (position[0], position[1] - 1),
            ]:
                if position_is_valid(garden, next_position) and garden[next_position[1]][next_position[0]] == plant_type:
                    if next_position not in region:
                        flood_fill_queue.append(next_position)
    return region

def get_regions(garden):
    regions = []
    visited_position = set()
    for y in range(len(garden)):
        for x in range(len(garden[0])):
            if (x, y) not in visited_position:
                region = get_region(garden, (x, y), garden[y][x])
                for position in region:
                    if position not in visited_position:
                        visited_position.add(position)
                if len(region) > 0:
                    regions.append(sorted(region, key=lambda pos: [pos[1], pos[0]]))
    return regions

def get_region_perimeter(region: list[tuple[int]]) -> int:
    # Should not happen, but let's put it in anyway
    if len(region) == 0:
        return 0
    # If the region only has one position, then we don't need to calculate the orthogonal convex hull
    if len(region) == 1:
        return 4

    perimeter = 4 * len(region)
    for position in region:
        if (position[0] + 1, position[1]) in region:
            perimeter -= 1
        if (position[0] - 1, position[1]) in region:
            perimeter -= 1
        if (position[0], position[1] + 1) in region:
            perimeter -= 1
        if (position[0], position[1] - 1) in region:
            perimeter -= 1

    return perimeter

def get_region_sides(region):
    pass

def get_region_corners(region: list[tuple[int, int]]) -> int:
    corner_positions = set()
    number_of_corners = 0
    for position in region:
        for x, y in [
            (position[0] + 0.5, position[1] + 0.5),
            (position[0] + 0.5, position[1] - 0.5),
            (position[0] - 0.5, position[1] - 0.5),
            (position[0] - 0.5, position[1] + 0.5)
        ]:
            corner_positions.add((x,y))

    for position in corner_positions:
        are_adjacent_positions = [(x, y) in region for x, y in [(position[0] + 0.5, position[1] + 0.5), (position[0] + 0.5, position[1] - 0.5), (position[0] - 0.5, position[1] - 0.5), (position[0] - 0.5, position[1] + 0.5)]]
        number_of_adjacent_positions = sum(are_adjacent_positions)
        if number_of_adjacent_positions == 1 or number_of_adjacent_positions == 3:
            number_of_corners += 1
        elif number_of_adjacent_positions == 2:
            if are_adjacent_positions == [True, False, True, False] or are_adjacent_positions == [False, True, False, True]:
                number_of_corners += 2

    return number_of_corners



def part_one(garde):
    regions = get_regions(garden)
    print(f"[PART ONE] - Total cost of fence is: {sum([len(region) * get_region_perimeter(region) for region in regions])}")

def part_two(garden):
    regions = get_regions(garden)
    print(f"[PART TWO] - Total cost of fence is: {sum([len(region) * get_region_corners(region) for region in regions])}")

if __name__ == "__main__":
    garden = get_garden("input.txt")
    part_one(garden)
    part_two(garden)

