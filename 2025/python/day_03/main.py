def part_one(banks):
    max_jolts = 0
    for bank in banks:
        bank = bank.strip()

        tenths = 0
        tenths_index = 0
        units = 0

        # get the tenths
        for i in range(len(bank) - 1):
            jolts = int(bank[i])
            if jolts > tenths:
                tenths = jolts
                tenths_index = i

        # get the units
        for j in range(tenths_index+1, len(bank)):
            jolts = int(bank[j])
            if jolts > units:
                units = jolts

        result = tenths * 10 + units
        max_jolts += result

    print(f"Maximum jolts: {max_jolts}")

def part_two(banks):
    for bank in banks:
        bank = bank.strip()
        max_value_index = 0
        max_jolts_str = str()
        remaining_char = 12

        for i in range(12):
            possible_next_values = bank[max_value_index : len(bank) - remaining_char + 1 : 1]
            possible_next_values_ints = list(map(lambda x: int(x), possible_next_values))
            max_value = max(possible_next_values_ints)
            max_value_index = bank[max_value_index : len(bank): 1].index(str(max_value)) + 1
            max_jolts_str += (str(max_value))
            remaining_char -= 1

        print(f"Max value: {max_jolts_str}")
            


with open("2025/python/day_03/sample.txt", "r") as file:
    banks = file.readlines()

part_one(banks)
part_two(banks)


    
