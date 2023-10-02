sum = 0

with open('input.txt', 'r') as file:
    for pair in file:
        elf1, elf2 = pair.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")

        elf1_sections = set(range(int(elf1_start), int(elf1_end) + 1))
        elf2_sections = set(range(int(elf2_start), int(elf2_end) + 1))

        duplicate_sections_count = len(elf1_sections.intersection(elf2_sections))

        if duplicate_sections_count > 0:
            sum += 1
        
print(sum)