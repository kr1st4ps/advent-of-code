score = 0
best_score = 0

with open("input.txt", "r") as file:
    
    #   Reads in the forest as a list
    forest = [list(line.strip()) for line in file]
    edge = len(forest) - 1

    #   Iterates through each tree in forest
    for row_id, row in enumerate(forest):
        for col_id, tree in enumerate(row):

            #   If tree is at the edge - count it as visible
            if row_id in [0, edge] or col_id in [0, edge]:
                continue

            #   Iterate through all trees up, down, left, right from the current one to check visibility
            visible = True
            check_row = row_id
            check_col = col_id
            check = 1
            score = 1
            mul = 0
            while True:

                #   Checks 1,2,3,4 are up, down, left, right
                if check == 1:
                    check_col -= 1
                elif check == 2:
                    check_col += 1
                elif check == 3:
                    check_row -= 1
                elif check == 4:
                    check_row += 1
                else:
                    break

                #   If edge is reached, that means the tree is visible from at least one side
                if check_row in [-1, edge + 1] or check_col in [-1, edge + 1]:
                    score *= mul
                    mul = 0
                    check += 1
                    check_col = col_id
                    check_row = row_id
                    continue

                mul += 1

                #   Checks if tree is higher
                check_tree = forest[check_row][check_col]
                if check_tree >= tree:
                    score *= mul
                    mul = 0

                    check += 1
                    check_col = col_id
                    check_row = row_id

            if score > best_score:
                best_score = score

print(best_score)