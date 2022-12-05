def create_list(pair):
    return [num for num in range(pair[0], pair[1]+1)]

def check_overlap(pair1, pair2):
    list1 = create_list(pair1)
    list2 = create_list(pair2)
    set_a = set(range(list1[0], list1[len(list1)-1]))
    set_b = set(range(list2[0], list2[len(list2)-1]))
    return set_a.issubset(set_b) or set_b.issubset(set_a)
    # if list1[0] <= list2[0]:
    #     for num in list2:
    #         if num not in list1:
    #             return False
    #     return True
    # else:
    #     for num in list1:
    #         if num not in list2:
    #             return False
    #     return True


    print(pair1, list1)
    print(pair2, list2)


f = open("input.txt", "r")

lines = f.readlines()

counter = 0


for line in lines:
    line = line.strip()
    pair1, pair2= line.split(",")
    pair1 = pair1.split("-")
    pair2 = pair2.split("-")
    pair1 = list(map(int, pair1))
    pair2 = list(map(int, pair2))
    print(check_overlap(pair1, pair2))
    if check_overlap(pair1, pair2):
        counter += 1

print(counter)
