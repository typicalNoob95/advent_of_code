FILE_TO_OPEN: str = "2025/python/day_02/sample.txt"

def generate_invalid_ids(start: str, stop: str, pattern_length = 2):
    max_pattern_lenght = len(stop) / 2




if __name__ == "__main__":
    with open(FILE_TO_OPEN, "r") as f:
        line = f.readline()
        string_ranges = line.split(",")

        ranges = []
        for rang in string_ranges:
            start, stop = rang.split("-")
            start = int(start)
            stop = int(stop)

            ranges.append((start, stop))

    print(ranges)