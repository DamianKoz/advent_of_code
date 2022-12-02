f = open("input.txt", "r")

lines = f.readlines()

# Second Column in input is the Outcome. X = Lose / Y = Draw / Z = Win
outcome_points = {"X": 0, "Y": 3, "Z":6}

# Enemy Choices: A = Rock / B = Paper / C = Scissors
# My Choices: X = Rock / Y = Paper / Z = Scissors

# First letter is the second column of input (desired outcome) 
# and inside is what the opponent played and what points I get for playing my answer
what_i_need_to_play = {
            'X' : {"A" : 3, "B" : 1, "C" : 2 },
            'Y' : {"B" : 2, "C" : 3, "A" : 1 },
            'Z' : {"C" : 1, "A" : 2, "B" : 3 }
            }

result = 0

for line in lines:
    line = line.strip()
    choices = line.split()
    opponent = choices[0]
    my_choice = choices[1]
    result += outcome_points[my_choice]
    result += what_i_need_to_play[my_choice][opponent]

print(result)


