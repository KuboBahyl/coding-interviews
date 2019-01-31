# Overlapping intervals - given various intervals, return the overlapped areas
# prop: it's sorted on starting intervals
intervals = [[1, 3], [2, 4], [5, 7], [6, 8], [9, 15], [10, 12], [13, 14], [9, 15]]


# out: [1,4], [5,8], [9,15]

def merge_all(intervals):
    if len(intervals) == 0:
        return []

    merged_all = [intervals[0]]
    for new_int in intervals[1:]:
        # take last int
        merged_int = merged_all[-1]

        # overlapping
        if new_int[0] <= merged_int[1] and new_int[1] > merged_int[1]:
            merged_int[1] = new_int[1]

        # not overlapping
        elif new_int[0] > merged_int[1]:
            merged_all.append(new_int)

    return merged_all


merge_all(intervals)