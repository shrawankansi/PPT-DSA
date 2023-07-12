def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


n = 27
result = is_power_of_three(n)
print(result)  # Output: True

n = 45
result = is_power_of_three(n)
print(result)  # Output: False
