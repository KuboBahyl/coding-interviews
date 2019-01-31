# Fibonacci - return the n-th Fibonacci number

def recursive_fibonacci(num):
    if num <= 1:
        return num
    else:
        return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)

recursive_fibonacci(35)