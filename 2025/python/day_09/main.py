def part_one(tiles: list[list[int]]):
    largest_rectangle = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            width = tiles[j][0] - tiles[i][0] + 1
            length = tiles[j][1] - tiles[i][1] + 1
            rectangle_area = width * length

            if rectangle_area > largest_rectangle:
                largest_rectangle = rectangle_area
    
    print(largest_rectangle)

def part_two(tiles: list[list[int]]):
    lines = []
    for i in range(len(tiles)):
        p1 = tiles[i]
        p2 = tiles[(i + 1) % len(tiles)]
        lines.append((p1, p2))


if __name__ == "__main__":
    tiles = list()
    with open("2025/python/day_09/sample.txt", "r") as file:
        for line in file.readlines():
            tile = line.strip().split(",")
            tile = list(map(int, tile))
            tiles.append(tile)

    part_one_tiles = sorted(tiles)
    part_one(part_one_tiles)
    part_two(tiles)

    