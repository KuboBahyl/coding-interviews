"""
Reconstruct .lower() method
In: 'abcA BC123///'
Out: 'abca bc123///'
"""
def str_to_lower(string):
    def is_capital(character):
        return ord('A') <= ord(character) <= ord('Z')

    out_arr = [None] * len(string)
    for i in range(len(string)):
        character = string[i]
        if is_capital(character):
            out_arr[i] = chr(ord(character) + (ord('a') - ord('A')))
        else:
            out_arr[i] = character

    return ''.join(out_arr)

test = ['Abc', '', ' a ', 'ABCD', 'abcd', 'a1B2C3d']

def lower(arg):
    return arg.lower()
test_input(test, str_to_lower, lower)