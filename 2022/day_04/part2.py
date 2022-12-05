def find_errors_in_lists(group):
    for letter in group[0]:
        for letter2 in group[1]:
            for letter3 in group[2]:   
                if letter == letter2 == letter3:
                    return letter
    print("ERROR")

f = open("input.txt", "r")

lines = f.readlines()

alphabet ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
counter = 0

for i in range(0, len(lines), 3):
    group = []

    group.append(lines[i].strip())
    group.append(lines[i+1].strip())
    group.append(lines[i+2].strip())

    letter = find_errors_in_lists(group)
    print(letter, alphabet.index(letter)+1)

    result += alphabet.index(letter) +1


print(result)
# print(alphabet.index("Z"))
