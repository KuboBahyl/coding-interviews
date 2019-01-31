# Activity selection problem
# choose the max count of activites given start and finish times
# greedy choice is to always pick the closest activity
# if not sorted input, just sort it according to finish times
def greedyActivity(starts: list, finishes: list):
    n = len(starts)

    i = 0
    print(i)

    for j in range(n):
        if starts[j] >= finishes[i]:
            print(j)
            i = j