from functools import cache

def get_stones(filepath):
    with open(filepath) as file:
        return [int(stone) for stone in [line for line in file.readline().strip().split(" ")]]

def blink(stones):
    new_stones = []
    for index, stone in enumerate(stones):
        # Rule #1
        if stone == 0:
            new_stones.append(1)

        # Rule #2
        elif len(str(stone)) % 2 == 0:
            str_stone_number = str(stone)
            number_of_digits = len(str_stone_number)
            half = number_of_digits // 2
            left_stone = int(str_stone_number[0 : half]) # First half digits
            right_stone = int(str_stone_number[half : ]) # Rest of the stone number

            new_stones.append(left_stone)
            new_stones.append(right_stone)

        # Rule #3
        else:
            new_stones.append(stone * 2024)

    return new_stones

def part_one(stones):
    new_stones = blink(stones)
    for i in range(24):
        new_stones = blink(new_stones)

    print(f"[PART ONE] - There are {len(new_stones)} stones")

@cache
def count_the_number_of_stones_created(stone, steps):
    # if it's the last step, we have only one stone
    if steps == 0:
        return 1
    if stone == 0:
        return count_the_number_of_stones_created(1, steps -1)
    str_stone_number = str(stone)
    number_of_digits = len(str_stone_number)
    if number_of_digits % 2 == 0:
        half = number_of_digits // 2
        left_stone = int(str_stone_number[0: half])  # First half digits
        right_stone = int(str_stone_number[half:])  # Rest of the stone number
        return count_the_number_of_stones_created(left_stone, steps - 1) + count_the_number_of_stones_created(right_stone, steps - 1)
    return count_the_number_of_stones_created(stone * 2024, steps - 1)

def fast_solve(stones, number_of_steps):
    return sum(count_the_number_of_stones_created(stone, number_of_steps) for stone in stones)


def part_two(stones):
    print(f"[PART TWO] - There are {fast_solve(stones, 75)} stones")


if __name__ == "__main__":
    stones = get_stones("input.txt")
    part_one(stones)
    part_two(stones)

