# Array - rotation
def rotate_array(arr, shift):
    def rotate_once(arr):
        for i in range(len(arr) - 1, 0, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        return arr

    for i in range(shift):
        rotate_once(arr)

    return arr


rotate_array([0, 1, 2, 3, 4, 5, 6], 3)