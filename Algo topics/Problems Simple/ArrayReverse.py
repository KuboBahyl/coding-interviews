# Array - reversing
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


reverse_array([0, 1, 2, 3, 4, 5, 6], 2, 4)