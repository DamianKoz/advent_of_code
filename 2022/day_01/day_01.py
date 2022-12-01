f = open("input.txt", "r")

lines = f.readlines()

elf_index = 1
highest_calorie = 0
current = 0
current_index = 1

for line in lines:
    line = line.strip()
    if line == "" or line == "\n":
        if current > highest_calorie:
            elf_index = current_index
            highest_calorie = current
        current = 0
        current_index += 1
    else:
        current += int(line)


print(highest_calorie)
print(elf_index)
print(current_index)
