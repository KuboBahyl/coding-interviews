# Fibonacci - memoization technique

def fibonacci_mem(num):
    def recursion(num):
        if mem[num] is None:
            if num <= 1:
                val = num
            else:
                val = recursion(num - 2) + recursion(num - 1)

            mem[num] = val

        return mem[num]

    mem = [None] * (num + 1)
    return recursion(num)


fibonacci_mem(35)