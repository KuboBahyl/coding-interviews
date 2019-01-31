# Pancake sort - use the flip function (reversing first k elems) to sort the array
# Logic: find the max value, flip it to the front and then back
def pancake_sort(arr):
    def flip(arr, k):
        for i in range(k // 2):
            arr[i], arr[k - 1 - i] = arr[k - 1 - i], arr[i]
        return arr

    def find_max(arr):
        max_idx = 0
        for j in range(len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        return max_idx

    pancake = len(arr)
    while pancake > 0:
        max_idx = find_max(arr[:pancake])
        arr = flip(arr, k=max_idx + 1)
        arr = flip(arr, k=pancake)
        pancake -= 1

    return arr


pancake_sort([3, 4, 8, 2, 9, 0, 6, 5, 1])