# 88. Merge Sorted Arrays
# Input:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


# Output: [1,2,2,3,5,6]

def merge_sorted(nums1, m, nums2, n):
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        idx = i + j + 1
        if nums1[i] >= nums2[j]:
            nums1[idx] = nums1[i]
            i -= 1
        else:
            nums1[idx] = nums2[j]
            j -= 1

    if j > 0:
        nums1[:j + 1] = nums2[:j + 1]

    return nums1


merge_sorted(nums1, m, nums2, n)