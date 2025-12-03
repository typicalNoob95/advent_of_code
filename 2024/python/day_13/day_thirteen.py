import re

def get_machines(filepath: str) -> list[tuple[int,int]]:
    machines = []
    with open(filepath) as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            button_a = list(map(int, re.findall("\\d+", lines[i])))
            button_b = list(map(int, re.findall("\\d+", lines[i + 1])))
            prize = list(map(int, re.findall("\\d+", lines[i + 2])))
            machine = {
                "A": button_a,
                "B": button_b,
                "Prize": prize
            }
            machines.append(machine)
    return machines

def get_button_presses(machine: dict):
    """
    This is a problem of geometry.  To find the number of a and be presses, we need to find were the slopes of counts
    intersects on a plane.

    Since we try to determine i*a[x] + j*b[x]  = prize[x] and i*a[y] + j*b[y] = prize[y] we need to solve for both.
    With algebra, we can determine that i = p[x]*b[y] - p[y]*b[x] / a[x]*b[y] - a[y]*b[x] and
    j = prize[x] - a[x]*i / b[x]
    :param machine:
    :return:
    """

    a_button_presses = ((machine["Prize"][0] * machine["B"][1]) - (machine["Prize"][1] * machine["B"][0])) / ((machine["A"][0] * machine["B"][1]) - (machine["A"][1] * machine["B"][0]))
    b_button_presses = (machine["Prize"][0] - (machine["A"][0] * a_button_presses)) / machine["B"][0]

    if a_button_presses % 1 == b_button_presses % 1 == 0:
        return a_button_presses, b_button_presses
    return 0, 0


if __name__ == "__main__":
    machines = get_machines("input.txt")
    total_tokens = 0
    for machine in machines:
        a, b = get_button_presses(machine)
        total_tokens += a * 3
        total_tokens += b

    print(f"[PART ONE] - Total tokens = {int(total_tokens)}")

    total_tokens = 0
    for machine in machines:
        machine["Prize"][0] += 10000000000000
        machine["Prize"][1] += 10000000000000

        a, b = get_button_presses(machine)
        total_tokens += a * 3
        total_tokens += b

    print(f"[PART TWO] - Total tokens = {int(total_tokens)}")