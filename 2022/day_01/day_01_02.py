f = open("input.txt", "r")

lines = f.readlines()

highest_elf_index = 0
highest_calorie = 0

second_highest_elf_index = 0
second_highest_calorie = 0

third_highest_elf_index = 0
third_highest_calorie = 0

current = 0
current_index = 1

for line in lines:
    line = line.strip()
    if line == "" or line == "\n":
        if current > highest_calorie:
            third_highest_calorie = second_highest_calorie
            second_highest_calorie = highest_calorie
            highest_calorie = current
            highest_elf_index = current_index
        elif current > second_highest_calorie:
            third_highest_calorie = second_highest_calorie
            second_highest_elf_index = current_index
            second_highest_calorie = current
        elif current > third_highest_calorie:
            third_highest_elf_index = current_index
            third_highest_calorie = current
        current = 0
        current_index += 1
    else:
        current += int(line)


print(highest_calorie + second_highest_calorie + third_highest_calorie)
