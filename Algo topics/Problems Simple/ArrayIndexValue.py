# Array - lowest index equaling value
def index_equals_value_search(arr):
    # binary search
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid_idx = (end + start) // 2

        if arr[mid_idx] < mid_idx:
            start = mid_idx + 1

        # match & positive &
        elif arr[mid_idx] == mid_idx and mid_idx > 0 and arr[mid_idx - 1] != mid_idx - 1:
            return mid_idx

        else:
            end = mid_idx - 1

    return -1


index_equals_value_search([-1, 1, 2, 5, 8, 9])
