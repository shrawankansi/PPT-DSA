def factorial(N):
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    return fact


N = 5
result = factorial(N)
print(result)  # Output: 120

N = 4
result = factorial(N)
print(result)  # Output: 24
