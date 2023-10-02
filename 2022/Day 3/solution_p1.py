priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

with open('input.txt', 'r') as file:
    for backpack in file:
        backpack = backpack.strip()

        halfpoint = len(backpack) // 2
        first_compartment = backpack[:halfpoint]
        second_compartment = backpack[halfpoint:]

        duplicate_items = []
        for item in first_compartment:
            if item in second_compartment and item not in duplicate_items:
                duplicate_items.append(item)

        for item in duplicate_items:
            sum += priorities.index(item) + 1
    
print(sum)