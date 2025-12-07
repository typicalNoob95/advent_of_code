def part_one(fresh_ranges: set[int], ids: list[int]) -> set[int]:
    fresh_ids = set()
    for ingredient in ids:
        for fresh in fresh_ranges:
            if ingredient < fresh[0] or ingredient > fresh[1]:
                continue
            else:
                fresh_ids.add(ingredient)
    
    print(f"Part One: {len(fresh_ids)}")

def part_two(fresh_ranges):
    total_ids = 0

    for i in range(len(fresh_ranges)):
        actual_range = fresh_ranges[i]
        if i < len(fresh_ranges) -1:
            if actual_range[1] >= fresh_ranges[i+1][0]:
                fresh_ranges[i+1][0] = actual_range[0]
                i += 1
                continue

        number_of_ids = actual_range[1] - actual_range[0] + 1
        total_ids += number_of_ids

        print(f"range: {actual_range}, number of ids: {number_of_ids}")

    print(f"Part Two: {total_ids}")

if __name__ == "__main__":
    fresh_ingredients = list()
    ingredients_ids = list()

    with open("2025/python/day_05/input.txt", "r") as file:
        reading_ranges = True
        for line in file.readlines():
            if reading_ranges:
                if line == "\n":
                    reading_ranges = False
                    continue
                start, stop = line.strip().split("-")
                fresh_ingredients.append([int(start), int(stop)])
            else:
                ingredients_ids.append(int(line.strip()))
    fresh_ingredients = sorted(fresh_ingredients, key = lambda x: x[0])
    print(fresh_ingredients)
    print("read the file")

    #part_one(fresh_ingredients, ingredients_ids)
    part_two(fresh_ingredients)