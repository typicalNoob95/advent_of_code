from aoc_utils.performance import print_duration


def get_both_lists(filepath):
    left_list = []
    right_list = []

    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.split("   ")
            left_list.append(int(numbers[0]))
            right_list.append(int(numbers[1].replace(" ", "")))

    return sorted(left_list), sorted(right_list)

def calculate_distance(location_ids):
    return abs(location_ids[0] - location_ids[1])

def part_one():
    left_list, right_list = get_both_lists("/home/fl/PycharmProjects/AOC2024/day_one/input.txt")
    total_distance = 0
    for i in range(len(left_list)):
        #print(f"left: {left_list[i]}, right: {right_list[i]}")
        distance = abs(left_list[i] - right_list[i])
        total_distance += distance
        #print(f"distance: {distance}")

    print(f"total distance = {total_distance}")

def count_occurences_in_rgiht_list(right_list):
    similarity_dict = {}
    for number in right_list:
        try:
            similarity_dict[number] += 1
        except KeyError:
            similarity_dict[number] = 1
    return  similarity_dict

def part_two():
    left_list, right_list = get_both_lists("/home/fl/PycharmProjects/AOC2024/day_one/input.txt")
    similarity_dict = count_occurences_in_rgiht_list(right_list)
    #print(similarity_dict)
    similarity_score = 0

    for location_id in left_list:
        try:
            similarity_score += similarity_dict[location_id] * location_id
        except Exception:
            pass

    print(f"similarity score: {similarity_score}")


if __name__ == "__main__":
    import aoc_utils.performance

    print_duration(part_one, "one")
    print_duration(part_two, "two")
