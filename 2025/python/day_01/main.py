DIAL_INITIAL_POSITION: int = 50
FILE_TO_OPEN: str = "2025/python/day_01/sample.txt"

if __name__ == "__main__":
    dial_position: int = DIAL_INITIAL_POSITION
    number_of_zeros = 0

    with open(FILE_TO_OPEN, "r") as f:
        for line in f.readlines():
            orientation = line[0]
            clicks = int(line[1::], base=10)

            if orientation == "L":
                for click in range(clicks):
                    dial_position -= 1

                    if dial_position < 0:
                        dial_position = 99

                    # for part two
                    if dial_position == 0:
                        number_of_zeros += 1
            else:
                for click in range(clicks):
                    dial_position += 1

                    if dial_position > 99:
                        dial_position = 0

                    # for part two
                    if dial_position == 0:
                        number_of_zeros += 1
            
            # for part one
            #if dial_position == 0:
            #            number_of_zeros += 1

    print(f"Dial position: {dial_position}, Number of zeros: {number_of_zeros}")

        
