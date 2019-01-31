# Find count subarr of given sum
arr = [1, 4, 20, 3, 10, 5]
summ = 33


def find_count_sum(arr, summ):
    start = end = 0
    queue_sum = arr[0]

    while end < len(arr):
        if queue_sum == summ:
            return arr[start:end + 1]

        if queue_sum < summ:
            end += 1
            if end == len(arr):
                return 'No subarray with a sum ' + str(summ)
            queue_sum += arr[end]
        elif queue_sum > summ:
            queue_sum -= arr[start]
            start += 1


find_count_sum(arr, summ)