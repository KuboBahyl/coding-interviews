# Stack - parenthesis balancing
def par_checker(par):
    stack = []

    for symbol in par:
        if symbol == "(":
            stack.append(symbol)
        elif stack and stack[-1] == "(":
            stack = stack[:-1]
        else:
            return print("Not balanced!")

    if len(stack) == 0:
        return print("Balanced")
    else:
        return print("Not balanced!")


par_checker("()(())")