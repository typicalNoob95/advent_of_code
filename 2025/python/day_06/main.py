import re
from typing import Any
import math

def part_one():
    equations: list[int] = []
    operations: list[str] = []
    with open("2025/python/day_06/input.txt", "r") as file:
        pattern = r"\d+"
        
        first_pass = True
        for line in file.readlines():
            numbers = list(map(int, re.findall(pattern, line)))
            operations = re.findall(r"[\+\*]", line)

            if first_pass:
                for number in numbers:
                    equations.append([number])
                first_pass = False
            else:
                for i in range(len(numbers)):
                    equations[i].append(numbers[i])

    total = 0
    for i in range(len(equations)):
        if operations[i] == "+":
            result = sum(equations[i])
        else:
            result = math.prod(equations[i])
        print(result)
        total+= result

    print(f"Part One: {total}")

def part_two():
    grid =[]
    operations: list[str] = []
    with open("2025/python/day_06/sample.txt", "r") as file:
        lines = file.readlines()
        number_of_lines = len(lines)
        for index, line in enumerate(lines):
            if index != number_of_lines -1:
                grid.append([char for char in line if char != "\n"])
            else:
                operations = re.findall(r"[\+\*]", line)

    for line in grid:
        print(line)
    print()
    print(operations)

    max_length_of_number = len(grid[0]) // len(operations)
    print(max_length_of_number)

    for i in range(max_length_of_number, len(grid[0])):
        pass





if __name__ == "__main__":
    #part_one()
    part_two()

