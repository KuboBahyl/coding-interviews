# Reverse string in-place
def reverse_string(string: str):
    N = len(string)
    for i in range(N):
        string = string[:i] + string[-1] + string[i:N - 1]

    return string


reverse_string('abcdefgh')