# Longest sorted subsequence 1 - return the longest consecutive sublist

def find_longest(myList: list):
    counter_max = idx_max = counter = prev = 0
    for i in range(len(myList)):
        num = myList[i]
        if num >= prev:
            counter += 1
        else:
            counter = 1

        if counter > counter_max:
            counter_max = counter
            idx_max = i

        prev = num

    return myList[idx_max + 1 - counter_max: idx_max + 1]


find_longest([50, 3, 10, 7, 40, 80])