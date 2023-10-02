#   A is Rock
#   B is Paper
#   C is Scissors

#   X is lose
#   Y is draw
#   Z is win

win_conditions =  {"A":"C",
                   "B":"A",
                   "C":"B"}
points = {"A":1,
          "B":2,
          "C":3}
my_points = 0

with open('input.txt', 'r') as file:
    for game in file:
        opponent, result = game.strip().split(" ")

        if result == "X":
            result = 0
            me = win_conditions[opponent]
        elif result == "Z":
            result = 6
            me = list(win_conditions.keys())[list(win_conditions.values()).index(opponent)]
        elif result == "Y":
            result = 3
            me = opponent

        my_points += result + points[me]

print(my_points)