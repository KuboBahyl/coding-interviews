# MERGE SORT
# Divide and Conquer
# O(nlog(n))
def merge_sort(arr):
    def merge_sorted(arr, left, right):
        pos, left_pos, right_pos = 0, 0, 0

        while left_pos < len(left) and right_pos < len(right):
            left_val = left[left_pos]
            right_val = right[right_pos]

            if left_val <= right_val:
                arr[pos] = left_val
                left_pos += 1

            else:
                arr[pos] = right_val
                right_pos += 1

            pos += 1

        for left_pos in range(left_pos, len(left)):
            arr[pos] = left[left_pos]
            pos += 1

        for right_pos in range(right_pos, len(right)):
            arr[pos] = right[right_pos]
            pos += 1

        return arr

    n = len(arr)
    if n > 1:
        mid = n // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge_sorted(arr, left, right)

    else:
        return arr