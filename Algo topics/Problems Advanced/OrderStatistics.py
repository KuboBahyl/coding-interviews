# order statistics - find the nth minimum value in array
def nth_min(arr, n):
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        return arr

    def find_position(arr):
        pivot = arr[0]  # elem we care about
        lower_idx = 0  # how many lower values we have
        for j in range(1, len(arr)):
            if arr[j] < pivot:
                lower_idx += 1
                arr = swap(arr, lower_idx, j)

        # swap pivot to the correct position
        arr = swap(arr, 0, lower_idx)
        return arr, lower_idx + 1

    arr, position = find_position(arr)

    while position + 1 != n:
        if min_idx + 1 < n:
            arr, min_idx = find_position(arr[min_idx + 1:])
        elif min_idx + 1 > n:
            arr, min_idx = find_position(arr[:min_idx])

    return arr[min_idx]


nth_min([5, 7, 8, 1, 2, 9, 3, 6], 1)