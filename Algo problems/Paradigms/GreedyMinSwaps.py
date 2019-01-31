# Minimum swaps in bracket balancing
# given 2N brackets, decide how many swaps are needed in order to return balanced brackets

def greedySwaps(brackets: str):
    brackets = list(brackets)
    swaps = 0
    opened = 0

    for i in range(len(brackets)):
        if brackets[i] == "[":
            if opened < 0:
                brackets[i], brackets[i + opened] = brackets[i + opened], brackets[i]
                swaps += 1

            opened += 1

        elif brackets[i] == "]":
            opened -= 1

    if opened == 0:
        return swaps, ''.join(brackets)
    else:
        return "not balanced"
