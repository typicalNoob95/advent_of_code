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
    merged_ranges = [fresh_ranges[0]]

    for current_start, current_end in fresh_ranges[1:]:
        last_start, last_end = merged_ranges[-1]

        if current_start <= last_end:
            merged_ranges[-1][1] = max(last_end, current_end)
        else:
            merged_ranges.append([current_start, current_end])

    for mr in merged_ranges:
        number_of_ids = mr[1] - mr[0] + 1
        total_ids += number_of_ids

        print(f"range: {mr}, number of ids: {number_of_ids}")

    print(f"Part Two: {total_ids}")

if __name__ == "__main__":
    fresh_ingredients = list()
    ingredients_ids = list()

    with open("2025/python/day_05/sample.txt", "r") as file:
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