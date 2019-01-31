# binary search - search num in sorted array in log(N) time
# if val is not present, return -1
def binary_search(arr, val):
    def divide(arr, val, start, end):
        # do this for each subarr
        if end >= start:
            search_idx = (end + start) // 2
            mid = arr[search_idx]

            if mid == val:
                return search_idx
            if mid < val:
                return divide(arr, val, search_idx + 1, end)
            else:
                return divide(arr, val, start, search_idx - 1)

        else:
            return -1

    N = len(arr)
    result = divide(arr, val, 0, N - 1)

    if result == -1:
        return "Element not present in the list!"
    else:
        return "Element present at index {}".format(result)


arr = [1, 2, 3, 4, 6, 7, 8, 9]
binary_search(arr, 9)