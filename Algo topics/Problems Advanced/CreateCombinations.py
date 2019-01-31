# Create combinations from given string
# In: "a{bb,c}dd{e,fff}"
# Out: "abbdde", "abbddfff", "acdde", "acddfff"

def print_combinations(string):
    N = len(string)
    big_arr = []
    in_bucket = False
    temp_arr = []
    temp_bucket = ''
    i = 0
    while i < N:
        character = string[i]
        if character == "{":
            in_bucket = True
        elif character == "}":
            in_bucket = False
            big_arr.append(temp_arr)
            temp_arr = []
        elif character == ",":
            i += 1
            continue
        else:
            temp_bucket = character
            while i < N - 1 and string[i + 1] not in ("{", "}", ","):
                temp_bucket += string[i]
                i += 1

            if in_bucket:
                temp_arr.append(temp_bucket)
            else:
                big_arr.append([temp_bucket])
            temp_bucket = ''

        i += 1

    # combinations
    M = len(big_arr)

    def comb_rec(arr, idx=0, word=''):
        if idx == M:
            print(word)
            return

        for elem in arr[idx]:
            comb_rec(arr, idx + 1, word + elem)

    comb_rec(big_arr)


string = "a{bb,c}dd{e,fff}"
print_combinations(string)