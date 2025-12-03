def get_reports_from_file(filepath):
    with open(filepath) as file:
        lines = file.readlines()
        reports_as_string =  [line.replace("\n", "").split(" ") for line in lines]
        reports = []
        for ras in reports_as_string:
            reports.append(list(map(int, ras)))
        return reports

def levels_are_increasing(actual_level, next_level):
    return actual_level - next_level < 0

def levels_difference_in_specs(actual_level, next_level):
    difference_range = range(1,4)
    return abs(actual_level - next_level) in difference_range

def report_is_safe(report):
    increasing = levels_are_increasing(report[0], report[1])
    safe = True
    for i in range(len(report) - 1):
        if levels_are_increasing(report[i], report[i + 1]) != increasing or not levels_difference_in_specs(report[i], report[i + 1]):
            safe = False
            return safe
    return safe

def report_is_safe_with_one_less_level(report):
    # We will start by brute forcing it and see if we can improve later.pop
    for i in range(len(report)):
        test_report = report.copy()
        test_report.pop(i)
        if report_is_safe(test_report):
            return True
    return False

def part_one():
    reports = get_reports_from_file("/home/fl/PycharmProjects/AOC2024/day_two/input.txt")
    nb_of_safe_reports = 0
    for report in reports:
        if report_is_safe(report):
            nb_of_safe_reports += 1

    print(f"[PART ONE] - There are {nb_of_safe_reports} safe reports.")

def part_two():
    reports = get_reports_from_file("/home/fl/PycharmProjects/AOC2024/day_two/input.txt")
    safe_reports = []
    for report in reports:
        if report_is_safe(report):
            safe_reports.append(report)
        else:
            if report_is_safe_with_one_less_level(report):
                safe_reports.append(report)

    print(f"[PART TWO] - There are {len(safe_reports)} using the Problem Dampener")




if __name__ == "__main__":
    part_one()
    part_two()

