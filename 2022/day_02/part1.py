f = open("input.txt", "r")

lines = f.readlines()

shape_points = {"X": 1, "Y": 2, "Z":3}

outcome = {'X' : {"A" : 3, "B" : 0, "C" : 6 },
          'Y' : {"B" : 3, "C" : 0, "A" : 6 },
          'Z' : {"C" : 3, "A" : 0, "B" : 6 }}

result = 0

for line in lines:
    line = line.strip()
    choices = line.split()
    opponent = choices[0]
    my_choice = choices[1]
    result += shape_points[my_choice]
    result += outcome[my_choice][opponent]

print(result)


