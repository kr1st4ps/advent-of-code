calories = max_calories = 0

with open('input.txt', 'r') as file:
    for line in file:
        if line == "\n":
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(line.strip())

print(max_calories)