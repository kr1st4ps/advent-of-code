visited = [(0,0)]
curr_pos_h = (0,0)
curr_pos_t = (0,0)
snake = []

for i in range(10):
    snake.append((0,0))

with open("input.txt", "r") as file:
    for line in file:
        direction, steps = line.split()

        for i in range(int(steps)):
            last_pos = snake[0]

            if direction == "R":
                snake[0] = (snake[0][0]+1, snake[0][1])
            elif direction == "U":
                snake[0] = (snake[0][0], snake[0][1]+1)
            elif direction == "L":
                snake[0] = (snake[0][0]-1, snake[0][1])
            elif direction == "D":
                snake[0] = (snake[0][0], snake[0][1]-1)
            
            for i in range(1, len(snake)):
                
                if len(snake) > i+1:
                    break

                first = snake[i]
                second = snake[i+1]

            
                if first[0] - curr_pos_t[0] in [-1,0,1] and first[1] - curr_pos_t[1] in [-1,0,1]:
                    None
                else:
                    curr_pos_t = last_pos_h
                    if curr_pos_t not in visited:
                        visited.append(curr_pos_t)

print(len(visited))
print(snake)