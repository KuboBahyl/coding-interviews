# find elements from arr1 and arr2 that sum up to given_sum
# a) most time-efficiently
# b) most space-efficiently
a = [1, 6, 3, 7]
b = [3, 8, 5, 1, 7, 0]
given_sum = 13


def find_pair_time(arr1, arr2, given_sum):
    smaller, bigger = arr1, arr2
    if len(bigger) < len(smaller):
        smaller, bigger = bigger, smaller

    bigger_hash = set(bigger)
    for num in smaller:
        diff = given_sum - num
        if diff in bigger_hash:
            return num, dif

    return False


print(find_pair_asap(a, b, given_sum))


# M < N
# Time: worst O(N + M)
# Space: O(N)

def find_pair_space(arr1, arr2, given_sum):
    smaller, bigger = arr1, arr2
    if len(bigger) < len(smaller):
        smaller, bigger = bigger, smaller

    bigger.sort()
    for num in smaller:
        diff = given_sum - num
        start = 0
        end = len(bigger) - 1
        while start < end:
            mid_idx = (start + end) // 2
            mid_val = bigger[mid_idx]
            if diff == mid_val:
                return num, diff
            elif diff > mid_val:
                start = mid_idx + 1
            else:
                end = mid_idx - 1

    return False


print(find_pair_space(a, b, given_sum))
# M < N
# Time: O(N*log(N) + M*log(N)) = O((M+N) log(N))
# Space: O(1)