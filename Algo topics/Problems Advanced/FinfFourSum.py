# Find four numbers that sum up to the summ
arr = [10, 2, 3, 4, 5, 9, 7, 8]
summ = 26


class Pair_sum(object):
    def __init__(self, num1, num2):
        self.sum = num1 + num2
        self.first = num1
        self.second = num2


def find_four_nums(arr, summ):
    N = len(arr)
    two_sums = [0] * (N * N - N)

    i = 0
    while i < N - 1:
        j = 1
        while j < N:
            if i != j:
                two_sums[i * N + j] = Pair_sum(arr[i], arr[j])
            j += 1
        i += 1

    two_sums = list(filter(lambda x: x != 0, two_sums))
    two_sums = sorted(two_sums, key=lambda x: x.sum)

    start = 0
    end = len(two_sums) - 1

    while start < end:
        start_pair = two_sums[start]
        end_pair = two_sums[end]

        if start_pair.sum + end_pair.sum == summ:
            if start_pair.first != end_pair.first and start_pair.first != end_pair.second \
                    and start_pair.second != end_pair.first and start_pair.second != end_pair.second:
                return start_pair.first, start_pair.second, end_pair.first, end_pair.second

            start += 1

        elif start_pair.sum + end_pair.sum > summ:
            end -= 1
        else:
            start += 1

    return 'no such sum'


find_four_nums(arr, summ)

# complexity: pair_sum + filter + sort + whil ~= sort = O(N^2 log(N^2)) = O(N^2 log(N))