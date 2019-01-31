# Given MxN bitmap, invert it as a mirror would do
bitmap = [
    [1, 2],
    [4, 5],
    [7, 8],
]


def flip_whole(bitmap):
    def print_bitmap(bitmap):
        for row in bitmap:
            print(row)

    def flip_arr(arr, N):
        start = 0
        end = N - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def flip_str(string):
        str_len = len(string)
        for i in range(str_len):
            string = string[:i] + string[-1] + string[i:str_len - 1]
        return string

    M = len(bitmap)
    N = len(bitmap[0])
    bitmap = [[bin(i)[2:] for i in row] for row in bitmap]

    for row in bitmap:
        flip_arr(row, N)
        for i in range(N):
            row[i] = flip_str(row[i])

    return print_bitmap(bitmap)


# Time: O(M*N + N*str_len)
# Space: O(1)
flip_whole(bitmap)