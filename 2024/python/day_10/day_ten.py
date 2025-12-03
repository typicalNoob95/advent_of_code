from collections import deque

def get_trail_map(filepath):
    with open(filepath) as file:
        return [[int(char) for char in line.strip()] for line in file.readlines()]

def get_trailhead_positions(trail_map):
    trailhead_starting_positions = []
    for y, line in enumerate(trail_map):
        for x, level in enumerate(line):
            if trail_map[y][x] == 0:
                trailhead_starting_positions.append((x, y))
    return trailhead_starting_positions

def position_is_valid(trail_map, position):
    return 0 <= position[0] < len(trail_map[0]) and 0 <= position[1] < len(trail_map)

def get_trailhead_score(trail_map, trailhead_position):
    bfs_queue = deque([trailhead_position])
    # We keep the seen positions and the number of ways to reach it.
    seen_positions = {
        trailhead_position: 1
    }
    seen_summits = 0
    possible_trails = 0

    while len(bfs_queue) > 0:
        position = bfs_queue.popleft()
        if trail_map[position[1]][position[0]] == 9:
            possible_trails += seen_positions[position]
            seen_summits += 1
        for next_position in [
            (position[0] + 1, position[1]),
            (position[0] - 1, position[1]),
            (position[0], position[1] + 1),
            (position[0], position[1] - 1)
        ]:
            if position_is_valid(trail_map, next_position) and trail_map[next_position[1]][next_position[0]] == trail_map[position[1]][position[0]] + 1:
                if next_position in seen_positions:
                    seen_positions[next_position] += seen_positions[position]
                    continue
                seen_positions[next_position] = seen_positions[position]
                bfs_queue.append(next_position)

    return seen_summits, possible_trails

if __name__ == "__main__":
    trail_map = get_trail_map("input.txt")
    trailhead_starting_positions = get_trailhead_positions(trail_map)
    trailhead_score_sum = 0
    trailhead_possible_trails = 0
    for position in trailhead_starting_positions:
        summits, trails = get_trailhead_score(trail_map, position)
        trailhead_score_sum += summits
        trailhead_possible_trails += trails

    print(trailhead_score_sum, trailhead_possible_trails)
