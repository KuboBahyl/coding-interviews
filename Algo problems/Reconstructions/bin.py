"""
Reconstruct bin()
In: 20, -2
Out: '0b10100', '-0b10'
"""


def int_to_bin(num: int):
    out = '0b'
    if num < 0:
        out = '-' + out
        num = abs(num)

    if num == 0:
        return out + '0'

    # num > 0
    exp_max = 0
    while 2 ** exp_max <= num:
        exp_max += 1

    for i in range(exp_max - 1, -1, -1):
        if 2 ** i <= num:
            out += '1'
            num -= 2 ** i
        else:
            out += '0'

    return out


# test
test = [-1234, -15, -1, 0, 1, 2, 5, 123456]
test_input(test, int_to_bin, bin)