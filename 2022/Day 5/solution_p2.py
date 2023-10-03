first = True
supply_stacks = []
top_crates = ""

with open('input.txt', 'r') as file:
    #   Starts by reading lines of the starting position of crates
    for line in file:
        if line == "\n":
           break
        elif line[1] == "1":
            continue
        
        #   For each level collects crates for each stack in lists
        for loop, index in enumerate(range(1, len(line), 4)):
            #   Creates lists when collecting crates from top level
            if first:
                if line[index] != " ":
                    supply_stacks.append([line[index]])
                else:
                    supply_stacks.append([])
            #   Adds to already initiated lists on lower levels
            else:
                if line[index] != " ":
                    supply_stacks[loop].append(line[index])
        
        if first:
            first = False

    #   Given instructions, moves crates around
    for line in file:
        _, amount, _, start, _, end = line.strip().split()

        #   First collects all crates from one stack that will be moved
        crane = []
        for i in range(int(amount)):
            crane.append(supply_stacks[int(start)-1].pop(0))

        #   Second - reverses the list of crates on crane to have the correct order
        crane.reverse()
            
        #   Third - adds crates from crane to target stack
        for crate in crane:
            supply_stacks[int(end)-1].insert(0, crate)

#   Collects top level crates for each stack
for stack in supply_stacks:
    top_crates += stack[0]
print(top_crates)