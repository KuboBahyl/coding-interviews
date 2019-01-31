# Merge k Sorted Arrays of length N
# Input:
list_nums = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]


# 1. approach: create N*k empty arr, copy data, sort
# O(nk log(nk))
# 2. approach: merge two, then add next till the end
# (N+N) + (2N+N) + (3N+N) +... = (sum 1 -> k)N + kN = O(k^2 N)
# 3. approach: merge twos, then merge twos, till the end
# k/2*(N+N) + k/4(2N+2N) +... = O(kN log(k))
# 4. approach: min heap, add values
#

def merge_sorted(list_nums, N, K):
    def merge_two(nums1, len1, nums2, len2):
        merged = [0] * (len1 + len2)
        i = j = 0
        while i < len1 and j < len2:
            idx = i + j
            if nums1[i] <= nums2[j]:
                merged[idx] = nums1[i]
                i += 1
            else:
                merged[idx] = nums2[j]
                j += 1

        if i == len1:
            merged[i + j:] = nums2[j:]
        else:
            merged[i + j:] = nums1[i:]

        return merged

    # main
    merged = []
    for i in range(N):
        merged_len = i * K
        nums = list_nums[i]
        merged = merge_two(merged, merged_len, nums, K)

    return merged


merge_sorted(list_nums, N=5, K=3)