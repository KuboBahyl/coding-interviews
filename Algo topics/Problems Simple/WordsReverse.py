# Reverse words in a string
def reverse_words(string: str):
    words = string.split()
    N = len(words)
    i = 0
    while i < N // 2:
        words[i], words[N - 1 - i] = words[N - 1 - i], words[i]
        i += 1

    return ' '.join(words)


reverse_words('a and b and c and d and e')