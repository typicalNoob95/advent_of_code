import re

instruction_pattern = "mul\\(\\d+,\\d+\\)"

def part_one(oneliner):
    result = 0
    instructions = (re.findall(instruction_pattern, oneliner))

    for inst in instructions:
        inst = inst.replace("mul", "").replace("(", "").replace(")", "")
        numbers = [int(number) for number in inst.split(",")]
        product = numbers[0] * numbers[1]
        result += product

    print(f"[PART ONE] - The result is {result}")

def part_two(oneliner):
    result = 0

    compiled_instruction_pattern = re.compile(instruction_pattern)
    matched_instructions = compiled_instruction_pattern.finditer(oneliner)
    matched_instructions_indexes = [match.span()[0] for match in matched_instructions]

    compiled_do_pattern = re.compile("do\\(\\)")
    matched_dos = compiled_do_pattern.finditer(oneliner)
    matched_dos_indexes = [match.span()[0] for match in matched_dos]

    compiled_dont_pattern = re.compile("don't\\(\\)")
    matched_donts = compiled_dont_pattern.finditer(oneliner)
    matched_dont_indexes = [match.span()[0] for match in matched_donts]

    enabled = True
    enabled_instructions_indexes = []
    for i in range(len(oneliner)):
        if i in matched_dont_indexes and enabled:
            enabled = False
        elif i in matched_dos_indexes and not enabled:
            enabled = True
        elif i in matched_instructions_indexes and enabled:
            enabled_instructions_indexes.append(i)

    matched_instructions = compiled_instruction_pattern.finditer(oneliner)  # Had to do it a second time.  I think the iterator gets emptied when accessing the data inside.
    enabled_instructions = [match.group() for match in matched_instructions if match.span()[0] in enabled_instructions_indexes]
    for inst in enabled_instructions:
        inst = inst.replace("mul", "").replace("(", "").replace(")", "")
        numbers = [int(number) for number in inst.split(",")]
        product = numbers[0] * numbers[1]
        result += product

    print(f"[PART TWO] - The result is {result}")

if __name__ == "__main__":
    filepath = "/home/fl/PycharmProjects/AOC2024/day_three/input.txt"

    oneliner = ""  # We select all the text into a single string to use the regex only once
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines:
            oneliner += line

    part_one(oneliner)
    part_two(oneliner)


