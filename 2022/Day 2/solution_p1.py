#   A,X are Rock
#   B,Y are Paper
#   C,Z are Scissors

win_conditions =  {"A":"Z",
                   "B":"X",
                   "C":"Y"}
loss_conditions = {"C":"X",
                   "A":"Y",
                   "B":"Z"}
points = {"X":1,
          "Y":2,
          "Z":3}
my_points = 0
result = None

with open('input.txt', 'r') as file:
    for game in file:
        opponent, me = game.strip().split(" ")

        if loss_conditions[opponent] == me:
            result = 6
        elif win_conditions[opponent] == me:
            result = 0
        else:
            result = 3

        my_points += result + points[me]

print(my_points)