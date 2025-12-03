import copy

def get_disk_configuration(filepath: str) -> list[str]:
    disk = []
    with open(filepath) as file:
        numbers = [int(char) for char in file.readline()]
        file_id = 0
        for index, size in enumerate(numbers):
            # For the size of the file, we input the file ID number to keep track of the positions
            if index % 2 == 0:
                disk.extend([file_id for i in range(size)])
                file_id += 1
            else:
                disk.extend(["." for i in range(size)])
    return disk

def rearange_files(disk):
    for i in range(len(disk)):
        # Verify that all free space is at the end.
        if all([index == "." for index in disk[i:]]):
            break

        if disk[i] == ".":
            last_file_block_index = -1
            while disk[last_file_block_index] == ".":
                last_file_block_index -= 1
            file_block = disk.pop(last_file_block_index)
            disk.append(".")
            disk[i] = file_block

    return disk

def get_files_and_free_spaces(disk):
    free_spaces = {}
    files = {}
    last_file_block = None
    last_starting_index = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            if last_file_block != ".":
                free_spaces[i] = 1
                last_starting_index = i
                last_file_block = "."
            else:
                free_spaces[last_starting_index] += 1
        else:
            file_index = disk[i]
            if last_file_block != file_index:
                files[i] = {
                    "size": 1,
                    "id": file_index
                }
                last_starting_index = i
                last_file_block = file_index
            else:
                files[last_starting_index]["size"] += 1

    return files, free_spaces

def find_available_space(file_index, file, free_spaces):
    lower_free_spaces_indexes = sorted([index for index in free_spaces.keys() if index < file_index])
    for index in lower_free_spaces_indexes:
        if free_spaces[index] >= file["size"]:
            return index
    return None

def move_file_to_free_space(file_index, files, available_free_space_index, free_spaces):
    files[available_free_space_index] = copy.deepcopy(files[file_index])

    if free_spaces[available_free_space_index] == files[file_index]["size"]:
        free_spaces.pop(available_free_space_index)
        free_spaces[file_index] = files[file_index]["size"]
    else:
        remaining_free_space = free_spaces[available_free_space_index] - files[available_free_space_index]["size"]
        free_spaces[available_free_space_index + files[available_free_space_index]["size"]] = remaining_free_space
        free_spaces[file_index] = free_spaces[available_free_space_index] - remaining_free_space
        free_spaces.pop(available_free_space_index)
    files.pop(file_index)
    return files, free_spaces

def rearange_files_together(files, free_spaces):
    file_keys = sorted(files.keys(), reverse=True)
    for file_index in file_keys:
        available_free_space_index = find_available_space(file_index, files[file_index], free_spaces)
        if available_free_space_index is not None:
            files, free_spaces = move_file_to_free_space(file_index, files, available_free_space_index, free_spaces)

    files.update(free_spaces)
    disk = []
    for index in sorted(files):
        if type(files[index]) == dict:
            disk[index : index + files[index]["size"]] = [files[index]["id"] for i in range(files[index]["size"])]
        else:
            disk[index : index + files[index]] = ["." for i in range(files[index])]
    return disk

def calculate_checksum(disk):
    checksum = 0
    for index, file_block in enumerate(disk):
        if file_block != ".":
            checksum += index * file_block
    return checksum

def part_one(disk):
    rearanged_disk = rearange_files(disk)
    checksum = calculate_checksum(rearanged_disk)
    print(f"[PART ONE] - The disk checksum is: {checksum}")

def part_two(disk):
    files, free_spaces = get_files_and_free_spaces(disk)
    disk = rearange_files_together(files, free_spaces)
    checksum = calculate_checksum(disk)
    print(f"[PART TWO] - The disk checksum is: {checksum}")

if __name__ == "__main__":
    disk = get_disk_configuration("/home/fl/PycharmProjects/AOC2024/day_nine/input.txt")
    part_one_disk = copy.deepcopy(disk)
    part_two_disk = copy.deepcopy(disk)
    part_one(part_one_disk)
    part_two(part_two_disk)