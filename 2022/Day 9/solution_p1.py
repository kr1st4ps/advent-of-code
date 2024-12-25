visited = [(0,0)]
curr_pos_h = (0,0)
curr_pos_t = (0,0)

with open("input.txt", "r") as file:
    for line in file:
        direction, steps = line.split()

        for i in range(int(steps)):
            last_pos_h = curr_pos_h

            if direction == "R":
                curr_pos_h = (curr_pos_h[0]+1, curr_pos_h[1])
            elif direction == "U":
                curr_pos_h = (curr_pos_h[0], curr_pos_h[1]+1)
            elif direction == "L":
                curr_pos_h = (curr_pos_h[0]-1, curr_pos_h[1])
            elif direction == "D":
                curr_pos_h = (curr_pos_h[0], curr_pos_h[1]-1)
            
            if curr_pos_h[0] - curr_pos_t[0] in [-1,0,1] and curr_pos_h[1] - curr_pos_t[1] in [-1,0,1]:
                None
            else:
                curr_pos_t = last_pos_h
                if curr_pos_t not in visited:
                    visited.append(curr_pos_t)

print(len(visited))