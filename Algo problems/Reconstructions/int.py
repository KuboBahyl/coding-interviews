"""
Recontruct int() for str input
Include also method call "base" with default = 10
In: "13", "+14", "-12", "023", ("+11111111", base=2)
Out: 12, 14, -12, 23, 255
"""

def string_to_int(string: str, base=10):
    N = len(string)
    if N < 1:
        return 'Bad input'

    first_idx = 0
    first = string[0]
    multiplier = 1

    if first < '0' or first > '9':
        if first == '-':
            multiplier = -1
        elif first == '+':
            multiplier = 1
        else:
            return 'Bad input'

        first_idx += 1
        first = string[1]

        if N == 1:
            return 'Bad input'

    # string >= '+1'
    out_num = 0
    for i in range(first_idx, N):
        temp_char = string[i]
        if '0' <= temp_char <= '9':
            ascii_shift = ord(temp_char) - ord('0')
            out_num += ascii_shift * base**(N-1 - i)

    return multiplier * out_num

test = ['0', '-1', '-00012', '+01', '90009']
test_input(test, string_to_int, int)