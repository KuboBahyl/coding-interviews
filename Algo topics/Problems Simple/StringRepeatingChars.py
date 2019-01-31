# Given a string as input, delete any repeating character, and return the new string.
# In: 'aabbcc'
# Out: 'abc'
def delete_repeating_chars(string):
    seen = set()
    out = ''

    for char in string:
        if char in seen:
            continue

        seen.add(char)
        out += char

    return out


delete_repeating_chars('aabbbcccddeeeeabcde')