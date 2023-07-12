def add_strings(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        current_sum = digit1 + digit2 + carry
        result = str(current_sum % 10) + result
        carry = current_sum // 10

        i -= 1
        j -= 1

    if carry != 0:
        result = str(carry) + result

    return result
num1 = "11"
num2 = "123"
result = add_strings(num1, num2)
print(result) 