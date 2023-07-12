def reverseNumber(num):
    num_str = str(num)
    stack = []

    
    for digit in num_str:
        stack.append(digit)

    result = ""

    
    while stack:
        result += stack.pop()

    reversed_num = int(result)

    return reversed_num



num = 365

reversed_num = reverseNumber(num)


print(reversed_num)
