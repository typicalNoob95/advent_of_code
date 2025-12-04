with open("2025\python\day_03\sample.txt", "r") as file:
    banks = file.readlines()

bank_joltages = list()
for bank in banks:
    bank = bank.strip()
    joltages = list()

    for str_joltage in bank:
        joltages.append(int(str_joltage))

    bank_joltages.append(joltages)

for joltages in bank_joltages:
    sorted_joltages = sorted(joltages)
    highest_joltages = sorted_joltages[-2:]
    
    first_indexes = joltages.index(highest_joltages[0])
    second_indexes = joltages.index(highest_joltages[1])

    print(first_indexes)
    print(second_indexes)

   
print(banks)
print(bank_joltages)