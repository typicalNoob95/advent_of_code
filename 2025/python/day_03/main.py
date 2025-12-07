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

def find_next_highest(bank_list: list[int], start_index: int) -> tuple[int, int]:
    bank_slice = bank_list[start_index::]
    highest = max(bank_slice)
    index = bank_list.index(highest)
    return index, highest

def enough_char_left(bank_list: list[int], index_to_check: int, remaining_char: int) -> bool:
    slice = bank_list[index_to_check : ]
    return len(slice) + 1 >= remaining_char

def part_two(banks):
    sum = 0
    for bank in banks:
        bank = bank.strip()
        wanted_length = 12
        index = 0
        highest_number_str = str()
        
        for i in range(wanted_length):
            last_possible_index = len(bank) - (wanted_length - (i + 1))

            max_index  = index
            max_digit = -1

            for j in range(index, last_possible_index):
                current_digit = int(bank[j])

                if current_digit > max_digit:
                    max_digit = current_digit
                    max_index = j

                if max_digit == 9:
                    break
            
            highest_number_str += str(max_digit)
            index = max_index + 1

        sum += int(highest_number_str)
        print(f"Max value: {highest_number_str}")

    print(sum)
            


with open("2025/python/day_03/input.txt", "r") as file:
    banks = file.readlines()

part_one(banks)
part_two(banks)


    
