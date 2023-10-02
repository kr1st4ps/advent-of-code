priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

with open('input.txt', 'r') as file:
    while True:
        elf1 = set(file.readline().strip())
        elf2 = set(file.readline().strip())
        elf3 = set(file.readline().strip())

        if not elf1 or not elf2 or not elf3:
            break

        badge = next(iter(elf1.intersection(elf2).intersection(elf3)))
        
        sum += priorities.index(badge) + 1
    
print(sum)