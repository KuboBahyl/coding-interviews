# Stack - decimal to binary
def dec2bin(num):
    binary = []
    while num > 0:
        binary.append(num % 2)
        num //= 2

    for i in range(len(binary)-1, -1, -1):
        print(binary[i], end="")

dec2bin(17)