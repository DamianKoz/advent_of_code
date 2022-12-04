def find_errors_in_lists(half1, half2):
    for letter in half1:
        for letter2 in half2:
            if letter == letter2:
                return letter
    print("ERROR")

f = open("input.txt", "r")

lines = f.readlines()

alphabet ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
counter = 0

for line in lines:
    counter += 1
    halves = []
    line = line.strip()
    half = len(line) // 2

    halves.append(line[:half])
    halves.append(line[half:len(line)])

    letter = find_errors_in_lists(halves[0], halves[1])

    result += alphabet.index(letter) +1


print(result)
print(alphabet.index("Z"))
