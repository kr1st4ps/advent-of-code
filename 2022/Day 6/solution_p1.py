window = []
count = 0

with open('input.txt', 'r') as file:
    while True:
        char = file.read(1)
        
        # Check EOF
        if not char:
            break
        
        if len(window) == 4:
            if len(set(window)) == 4:
                break
            else:
                window.pop(0)

        window.append(char)

        count += 1
        
print(count)