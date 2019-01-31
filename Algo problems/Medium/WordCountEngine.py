# Sentences - list of lists of sorted unique words with occurencies
def word_count_engine(document):
    words_list = document.split(' ')
    N = len(words_list)
    words_dict = dict()
    max_occ = 0

    for word in words_list:
        word = ''.join([char for char in word.lower() if 97 <= ord(char) <= 122])

        if len(word) < 1:
            continue

        if words_dict.get(word):
            words_dict[word] += 1
        else:
            words_dict[word] = 1

        if words_dict[word] > max_occ:
            max_occ = words_dict[word]

    agg_list = [None] * (max_occ + 1)
    for word, occ in words_dict.items():
        if agg_list[occ] is None:
            agg_list[occ] = []

        agg_list[occ].append(word)

    out_list = []
    #     for i in range(len(agg_list) -1, 0, -1):
    #         for word in agg_list[i]:
    #             out_list.append([word, str(i)])

    return agg_list


word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")