

if __name__ == '__main__':

    records = []

    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, float(score)])

    list1 = []
    set1 = set()
    for i in range(len(records)):
        list1.append(records[i][1])

    for i in range(len(list1)):
        set1.add(list1[i])

    sorted_set = sorted(set1)

    sec_min = list(sorted_set)[1]

    list2 = []
    for i in range(len(records)):
        if records[i][1] == sec_min:
            list2.append(records[i][0])

    list2.sort()

    for i in range(len(list2)):
        print(list2[i])

