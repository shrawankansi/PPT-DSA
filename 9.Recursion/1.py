def isPowerOfTwo(n):
    if n <= 0:
        return False

    return n & (n - 1) == 0
n = 1
print(isPowerOfTwo(n))

n = 16
print(isPowerOfTwo(n))

n = 3
print(isPowerOfTwo(n))
