def position_is_valid(x_position, y_position, x_size, y_size):
    return x_position >= 0 and x_position < x_size and y_position >= 0 and y_position < y_size

def check_surrondings_for_xmas(x_position: int, y_position: int, letters: []) -> int:
    # We verify that we start with an X
    if letters[y_position][x_position] != "X":
        return 0

    # Counter to accumulate the number of XMAS found with this starting point.
    total_xmas = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    found_letters = ""
    x_size = len(letters[0])
    y_size = len(letters)
    for direction in directions:
        found = True
        for i in range(4):
            x_position_to_verify = x_position + (i * direction[1])
            y_position_to_verify = y_position + (i * direction[0])

            if (not position_is_valid(x_position_to_verify, y_position_to_verify, x_size, y_size)
                    or letters[y_position_to_verify][x_position_to_verify] != "XMAS"[i]):
                    found = False
                    break
        if found:
            total_xmas += 1

    return total_xmas

def part_one(letters: []) -> int:
    total_xmas = 0
    for y in range(len(letters)):
        for x in range(len(letters[y])):
            total_xmas += check_surrondings_for_xmas(x, y, letters)

    return total_xmas

def cross_positions_are_valid(x_position: int, y_position: int, x_size: int, y_size: int) -> bool:
    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    cross_is_valid = True

    for direction in directions:
        if not position_is_valid(x_position + direction[0], y_position + direction[1], x_size, y_size):
            cross_is_valid = False

    return cross_is_valid

def number_of_m_and_s_is_valid(x_position: int, y_position: int, x_size: int, y_size: int, letters: []) -> bool:
    number_of_m = 0
    number_of_s = 0

    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
    for direction in directions:
        if letters[y_position + direction[1]][x_position + direction[0]] == "M":
            number_of_m += 1
        elif letters[y_position + direction[1]][x_position + direction[0]] == "S":
            number_of_s += 1
        else:
            return False

    # Verify that the diagonals are not the same letters
    if letters[y_position + directions[0][1]][x_position + directions[0][0]] == letters[y_position + directions[3][1]][x_position + directions[3][0]]:
        return False
    if letters[y_position + directions[1][1]][x_position + directions[1][0]] == letters[y_position + directions[2][1]][x_position + directions[2][0]]:
        return False

    return number_of_m == 2 and number_of_s == 2


def part_two(letters: []) -> int:
    total_x_mas = 0

    directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]

    y_size = len(letters)
    x_size = len(letters[0])

    for y in range(y_size):
        for x in range(x_size):
            if letters[y][x] == "A" and cross_positions_are_valid(x, y, x_size, y_size) and number_of_m_and_s_is_valid(x, y, x_size, y_size, letters):
                total_x_mas += 1


    return total_x_mas


if __name__ == "__main__":
    letters = []
    with open("/home/fl/PycharmProjects/AOC2024/day_four/input.txt") as file:
        for line in file.readlines():
            line_characters = [char for char in line if char != "\n"]
            letters.append(line_characters)

    total_xmas = part_one(letters)
    total_x_mas = part_two(letters)



    print(f"[PART ONE] - {total_xmas}")
    print(f"[PART TWO] - {total_x_mas}")