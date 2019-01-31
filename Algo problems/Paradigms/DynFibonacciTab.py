# Fibonacci - tabulation technique

def fibonacci_tab(num):
    mem = [None] * num
    mem[0] = 0
    mem[1] = 1

    for i in range(num):
        mem[i] = mem[i - 1] + mem[i - 1]

    return mem[-1]


fibonacci(35)