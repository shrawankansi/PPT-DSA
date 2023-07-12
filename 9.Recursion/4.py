def exponentiation(N, P):
    result = N ** P
    return result


N = 5
P = 2
result = exponentiation(N, P)
print(result)  # Output: 25

N = 2
P = 5
result = exponentiation(N, P)
print(result)  # Output: 32


# ////////////////////////////////////////////////////////////////

def exponentiation(N, P):
    result = pow(N, P)
    return result


N = 5
P = 2
result = exponentiation(N, P)
print(result)  # Output: 25

N = 2
P = 5
result = exponentiation(N, P)
print(result)  # Output: 32
